# Aura OS - Professional Custom Dashboard

A sleek, professional-grade fullscreen dashboard OS for Lenovo Neo 50q Gen 4 (and compatible systems). Features Aura branding, auto-launch on boot, local network services, and enterprise-grade UI/UX.

## 🚀 Quick Start

**New to Aura OS? Start here:** [START_HERE.md](START_HERE.md)

For Windows development:
1. Install Python 3.10+ and Node.js 18+
2. Run: `launch-dev.bat` (or `.\launch-dev.ps1`)
3. Open: http://localhost:9000

For detailed development guide: [DEV_QUICKSTART.md](DEV_QUICKSTART.md)

## 📋 Features

- **Sleek UI/UX**: Modern, eye-appealing interface with professional design
- **Aura Branding**: Custom logo and branded loading screens
- **Auto-Launch**: Boots directly to fullscreen dashboard
- **Local Network**: Python backend for mesh networking and services
- **Professional Grade**: Production-ready code, error handling, logging
- **Dark/Light Theme**: Adaptive design with system preferences
- **No Login**: Direct access to dashboard on boot

## 🏗️ Architecture

```
Aura OS
├── Electron App (Fullscreen)
│   └── React Dashboard
│       └── Real-time widgets & controls
├── Python Backend (FastAPI)
│   ├── Local API Server
│   ├── Network Services
│   ├── AI/ML Engine
│   └── Device Control
└── Linux System
    ├── Auto-login
    ├── Systemd Services
    └── Kiosk Mode
```

## 🚀 Quick Start

### Prerequisites
- Ubuntu 22.04 LTS or newer
- Node.js 18+
- Python 3.10+
- npm/yarn

### Installation

```bash
# Clone or extract the project
cd aura-os

# Install frontend
cd frontend
npm install

# Install backend
cd ../backend
pip install -r requirements.txt

# Deploy system files
sudo ./system/setup.sh
```

### Development

```bash
# Terminal 1: Backend
cd backend
python core_server.py

# Terminal 2: Frontend
cd frontend
npm run dev
```

### Production Deployment

```bash
# Build Electron app
cd frontend
npm run build

# Deploy systemd services
sudo ./system/install-services.sh

# Reboot to test auto-launch
sudo reboot
```

## 📁 Project Structure

- **frontend/**: React + Electron app
- **backend/**: Python FastAPI services
- **system/**: Linux startup and systemd services
- **assets/**: Logos, icons, branding

## 🎨 Customization

Edit these files to personalize:
- `frontend/src/config/theme.js` - Colors, fonts, branding
- `frontend/src/components/` - UI components
- `backend/core_server.py` - Core services and APIs
- `system/` - Auto-startup configuration

## 📖 Documentation

See individual README files in each directory for detailed setup instructions.

---

**Aura OS v1.0** | Professional Dashboard System
