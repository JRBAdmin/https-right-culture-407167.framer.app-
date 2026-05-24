# Aura OS Deployment Guide

Complete deployment guide for Lenovo Neo 50q Gen 4 and compatible systems.

## 📋 Prerequisites

- Lenovo Neo 50q Gen 4 (or compatible Tiny PC)
- Ubuntu 22.04 LTS installed (fresh install recommended)
- 8GB RAM minimum
- 120GB SSD minimum
- Internet connection for setup

## 🚀 Step-by-Step Deployment

### Phase 1: System Reset (If Needed)

Before deploying Aura OS, reset the machine:

```bash
# 1. Perform CMOS reset (if BIOS is locked)
# See hardware troubleshooting section below

# 2. Or replace SSD with fresh Ubuntu installation
# Use Ubuntu Server 22.04 LTS
# Download: https://ubuntu.com/download/server
```

### Phase 2: Initial System Setup

```bash
# 1. Update system
sudo apt-get update
sudo apt-get upgrade -y

# 2. Install Git
sudo apt-get install -y git

# 3. Clone or download Aura OS project
cd ~
git clone <aura-os-repo> aura-os
cd aura-os
```

### Phase 3: Run Setup Script

```bash
# 1. Make setup script executable
chmod +x system/setup.sh

# 2. Run setup (requires sudo)
sudo ./system/setup.sh

# Wait for installation to complete (5-10 minutes)
```

The setup script will:
- Create `aura` system user
- Install all dependencies
- Set up auto-login
- Create Python virtual environment
- Install Node.js and Python packages
- Build frontend and Electron app
- Create startup scripts

### Phase 4: First Boot

```bash
# 1. Reboot system
sudo reboot

# 2. Aura OS should auto-launch
# If not, check logs:
tail -f /opt/aura/logs/aura_core.log

# 3. You should see:
# - Aura loading screen
# - Professional dashboard
# - Live system metrics
```

## 🔧 Post-Installation Configuration

### Auto-Start Services

```bash
# Install systemd services
sudo ./system/install-services.sh

# Enable automatic restart
sudo systemctl enable aura-core.service
sudo systemctl enable aura-frontend.service

# Start services
sudo systemctl start aura-core.service
sudo systemctl start aura-frontend.service
```

### Customize Branding

Edit theme colors in:
- Frontend: `frontend/src/config/theme.js` (create if needed)
- Colors: `frontend/src/components/Dashboard.css`

### Configure Backend

Edit `backend/config.py`:

```python
# System name
SYSTEM_NAME = "Your Organization - Aura OS"

# Features
FEATURES = {
    'dashboard': True,
    'network_monitor': True,
    'security_panel': True,
}

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 85
DISK_THRESHOLD = 90
```

### Network Configuration

```bash
# Edit network settings
sudo nano /etc/netplan/01-netcfg.yaml

# Apply changes
sudo netplan apply

# Check status
ip addr
nmcli device show
```

## 📊 Monitoring & Logs

### View Logs

```bash
# Backend logs
sudo journalctl -u aura-core -f
# Or tail directly
tail -f /opt/aura/logs/aura_core.log

# Frontend logs
sudo journalctl -u aura-frontend -f

# System logs
sudo journalctl -f
```

### Check Services

```bash
# Status
sudo systemctl status aura-core
sudo systemctl status aura-frontend

# Restart
sudo systemctl restart aura-core
sudo systemctl restart aura-frontend

# Stop
sudo systemctl stop aura-core
sudo systemctl stop aura-frontend
```

### Performance Monitoring

```bash
# Real-time system monitoring
htop

# Network monitoring
iftop

# Disk usage
df -h

# Memory usage
free -h
```

## 🔐 Security Configuration

### Firewall Setup

```bash
# Enable UFW
sudo ufw enable

# Allow SSH (if needed)
sudo ufw allow 22/tcp

# Allow Aura backend
sudo ufw allow 5000/tcp

# Check status
sudo ufw status
```

### User Management

```bash
# Create admin user
sudo useradd -m -s /bin/bash -G sudo admin
sudo passwd admin

# Lock default account (optional)
sudo usermod -L ubuntu
```

### SSL/TLS (Optional)

```bash
# Generate self-signed cert (for HTTPS)
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/ssl/private/aura.key \
  -out /etc/ssl/certs/aura.crt

# Update FastAPI to use HTTPS
# Edit backend/core_server.py
```

## 🛠️ Hardware Troubleshooting

### BIOS Reset (Lenovo Neo 50q)

If BIOS is locked:

**Option 1: CMOS Battery Reset**
```
1. Power off completely
2. Unplug power cable
3. Remove side panel (2-4 screws)
4. Locate CMOS battery (coin cell, CR2032)
5. Disconnect battery for 30 seconds
6. Reconnect battery
7. Hold power button 15 seconds
8. Close panel and power on
```

**Option 2: Replace SSD**
```
1. Power off
2. Remove side panel
3. Locate M.2 NVMe SSD
4. Remove existing SSD
5. Install new SSD
6. Power on and install Ubuntu
```

### Network Issues

```bash
# Check connectivity
ping 8.8.8.8

# Check DNS
nslookup google.com

# Restart networking
sudo systemctl restart networking

# Check interfaces
ip link show
```

### Performance Issues

```bash
# Check CPU usage
top -o %CPU

# Check memory usage
top -o %MEM

# Check disk I/O
iostat -x 1

# Check running processes
ps aux --sort=-%cpu
```

## 📦 Backup & Restore

### Create System Backup

```bash
# Create backup
sudo tar -czf /media/backup/aura-os-backup-$(date +%Y%m%d).tar.gz \
  /opt/aura \
  /etc/lightdm/lightdm.conf.d/99-aura.conf

# Verify backup
tar -tzf /media/backup/aura-os-backup-*.tar.gz | head
```

### Restore from Backup

```bash
# Restore
sudo tar -xzf /media/backup/aura-os-backup-*.tar.gz -C /

# Restart services
sudo systemctl restart aura-core
sudo systemctl restart aura-frontend
```

## 🔄 Update & Maintenance

### System Updates

```bash
# Check for updates
sudo apt-get update
sudo apt-get upgrade

# Full upgrade
sudo apt-get dist-upgrade
```

### Aura Updates

```bash
# Pull latest changes
cd ~/aura-os
git pull

# Rebuild frontend
cd frontend
npm install
npm run build
npm run electron-build

# Restart services
sudo systemctl restart aura-frontend
```

### Clean Up

```bash
# Clear cache
sudo apt-get clean
sudo apt-get autoclean

# Remove old logs
sudo journalctl --vacuum=30d

# Clear npm cache
npm cache clean --force
```

## 📱 Remote Management

### SSH Access

```bash
# Connect remotely
ssh aura@<ip-address>

# From Windows (PowerShell)
ssh aura@<ip-address>
```

### Remote Desktop (Optional)

```bash
# Install VNC
sudo apt-get install -y tigervnc-standalone-server

# Start VNC
vncserver -geometry 1920x1080 -depth 24 :1

# Connect from remote machine
vncviewer <ip>:1
```

## 🚨 Troubleshooting Common Issues

### Dashboard Won't Load

```bash
# Check backend
curl http://localhost:5000/health

# Check frontend process
ps aux | grep electron

# Restart frontend
sudo systemctl restart aura-frontend
```

### High CPU Usage

```bash
# Identify process
top -o %CPU

# Check for loops
grep -n "while True" /opt/aura/backend/*.py

# Increase monitoring interval
# Edit backend/config.py: MONITOR_INTERVAL = 5
```

### Network Not Available

```bash
# Check network status
curl http://localhost:5000/api/network/status

# Restart networking
sudo systemctl restart networking

# Check routes
ip route show
```

### Storage Full

```bash
# Check disk usage
df -h

# Find large files
du -sh /opt/aura/*

# Clean logs
sudo journalctl --vacuum=7d
```

## 📞 Support & Resources

- **Documentation**: See README.md files
- **Logs**: `/opt/aura/logs/`
- **Config**: `/opt/aura/config/`
- **Services**: `sudo systemctl status aura-*`

---

**Aura OS v1.0 Deployment Complete** ✓
