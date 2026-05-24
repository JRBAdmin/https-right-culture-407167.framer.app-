#!/bin/bash

# Aura OS System Setup Script
# Run with: sudo ./setup.sh

set -e

echo "================================"
echo "  Aura OS System Setup"
echo "================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}This script must be run as root${NC}"
   echo "Run with: sudo ./setup.sh"
   exit 1
fi

AURA_HOME="/opt/aura"
AURA_USER="aura"

echo -e "${YELLOW}[*] Creating Aura OS system user...${NC}"
if ! id "$AURA_USER" &>/dev/null; then
    useradd -m -s /bin/bash -G sudo "$AURA_USER" 2>/dev/null || true
    echo -e "${GREEN}[✓] User created${NC}"
else
    echo -e "${GREEN}[✓] User already exists${NC}"
fi

echo -e "${YELLOW}[*] Setting up directories...${NC}"
mkdir -p "$AURA_HOME"
mkdir -p "$AURA_HOME/logs"
mkdir -p "$AURA_HOME/config"
chown -R "$AURA_USER:$AURA_USER" "$AURA_HOME"
chmod 755 "$AURA_HOME"
echo -e "${GREEN}[✓] Directories created${NC}"

echo -e "${YELLOW}[*] Installing system dependencies...${NC}"
apt-get update -qq
apt-get install -y -qq \
    curl \
    wget \
    git \
    python3.10 \
    python3-pip \
    python3-venv \
    nodejs \
    npm \
    chromium-browser \
    xvfb \
    xinit \
    lightdm \
    2>&1 | grep -v "^Setting up" || true
echo -e "${GREEN}[✓] Dependencies installed${NC}"

echo -e "${YELLOW}[*] Setting up auto-login...${NC}"
mkdir -p /etc/lightdm/lightdm.conf.d
cat > /etc/lightdm/lightdm.conf.d/99-aura.conf << EOF
[General]
autologin-user=$AURA_USER
autologin-session=xfce
session-wrapper=/etc/X11/Xsession
EOF
chmod 644 /etc/lightdm/lightdm.conf.d/99-aura.conf
echo -e "${GREEN}[✓] Auto-login configured${NC}"

echo -e "${YELLOW}[*] Creating Aura startup scripts...${NC}"
mkdir -p /home/$AURA_USER/.config/autostart
cat > /home/$AURA_USER/.aura_startup.sh << 'EOF'
#!/bin/bash
# Aura OS Startup Script

export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"

# Wait for X server
sleep 3

# Start Aura Python backend
/opt/aura/venv/bin/python /opt/aura/backend/core_server.py &
sleep 3

# Start Aura Electron app in kiosk mode
/opt/aura/frontend/aura-os &

# Keep script running
wait
EOF

chmod +x /home/$AURA_USER/.aura_startup.sh
chown $AURA_USER:$AURA_USER /home/$AURA_USER/.aura_startup.sh

# Add to .bashrc for auto-launch on shell login
echo "exec /home/$AURA_USER/.aura_startup.sh" >> /home/$AURA_USER/.bashrc
echo -e "${GREEN}[✓] Startup scripts created${NC}"

echo -e "${YELLOW}[*] Setting up Aura directories...${NC}"
# Copy frontend and backend to Aura home
if [ -d "./frontend" ] && [ -d "./backend" ]; then
    cp -r frontend "$AURA_HOME/"
    cp -r backend "$AURA_HOME/"
    chown -R "$AURA_USER:$AURA_USER" "$AURA_HOME/frontend" "$AURA_HOME/backend"
    echo -e "${GREEN}[✓] Application files copied${NC}"
else
    echo -e "${YELLOW}[!] Please run this script from Aura OS root directory${NC}"
fi

echo -e "${YELLOW}[*] Creating Python virtual environment...${NC}"
cd "$AURA_HOME"
sudo -u "$AURA_USER" python3 -m venv venv
sudo -u "$AURA_USER" "$AURA_HOME/venv/bin/pip" install --upgrade pip setuptools wheel
echo -e "${GREEN}[✓] Virtual environment created${NC}"

echo -e "${YELLOW}[*] Installing Python dependencies...${NC}"
if [ -f "$AURA_HOME/backend/requirements.txt" ]; then
    sudo -u "$AURA_USER" "$AURA_HOME/venv/bin/pip" install -r "$AURA_HOME/backend/requirements.txt"
    echo -e "${GREEN}[✓] Python dependencies installed${NC}"
fi

echo -e "${YELLOW}[*] Installing Node.js dependencies...${NC}"
if [ -f "$AURA_HOME/frontend/package.json" ]; then
    cd "$AURA_HOME/frontend"
    sudo -u "$AURA_USER" npm ci
    echo -e "${GREEN}[✓] Node.js dependencies installed${NC}"
fi

echo -e "${YELLOW}[*] Building frontend...${NC}"
cd "$AURA_HOME/frontend"
sudo -u "$AURA_USER" npm run build
sudo -u "$AURA_USER" npm run electron-build
echo -e "${GREEN}[✓] Frontend built${NC}"

echo ""
echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}  Aura OS Setup Complete!${NC}"
echo -e "${GREEN}================================${NC}"
echo ""
echo "Next steps:"
echo "1. Reboot the system: sudo reboot"
echo "2. Aura OS will auto-launch on boot"
echo "3. Access logs: tail -f $AURA_HOME/logs/aura_core.log"
echo ""
