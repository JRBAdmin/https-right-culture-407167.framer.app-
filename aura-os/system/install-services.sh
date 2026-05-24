#!/bin/bash

# Aura OS Service Installation Script
# Run with: sudo ./install-services.sh

set -e

echo "Installing Aura OS services..."

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Copy service files
echo "Installing systemd services..."
cp "$SCRIPT_DIR/aura-core.service" /etc/systemd/system/
cp "$SCRIPT_DIR/aura-frontend.service" /etc/systemd/system/

# Reload systemd
systemctl daemon-reload

# Enable services
echo "Enabling services..."
systemctl enable aura-core.service
systemctl enable aura-frontend.service

echo "Services installed successfully!"
echo ""
echo "To start the services:"
echo "  systemctl start aura-core"
echo "  systemctl start aura-frontend"
echo ""
echo "To check status:"
echo "  systemctl status aura-core"
echo "  systemctl status aura-frontend"
echo ""
echo "To view logs:"
echo "  journalctl -u aura-core -f"
echo "  journalctl -u aura-frontend -f"
