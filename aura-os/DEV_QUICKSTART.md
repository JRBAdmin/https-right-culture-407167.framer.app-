# Quick Start - Windows Development

## Ports Used

- **Backend**: http://localhost:9500
- **Frontend**: http://localhost:9000

## Prerequisites

Install these first:

### 1. Python 3.10+
Download: https://www.python.org/downloads/
- Check "Add Python to PATH" during install

### 2. Node.js 18+
Download: https://nodejs.org/
- Choose LTS version
- Check "Automatically install necessary tools" during install

### 3. Git (Optional, for cloning)
Download: https://git-scm.com/

## Quick Start (Windows)

### Option 1: Using PowerShell Script (Recommended)

```powershell
# 1. Navigate to project
cd C:\Users\meagh\aura-os

# 2. Run launch script
.\launch-dev.ps1

# Wait for both to start...
# Backend will show: "Listening on http://0.0.0.0:9500"
# Frontend will show: "Compiled successfully!"
```

### Option 2: Manual Start

**Terminal 1 - Backend:**
```powershell
cd C:\Users\meagh\aura-os\backend

# Create virtual environment (first time only)
python -m venv venv

# Activate
.\venv\Scripts\activate

# Install dependencies (first time only)
pip install -r requirements.txt

# Run
python core_server.py
```

**Terminal 2 - Frontend:**
```powershell
cd C:\Users\meagh\aura-os\frontend

# Install dependencies (first time only)
npm install

# Run
npm run dev
```

Wait for both to show "ready" messages, then open:
**http://localhost:9000**

## What You'll See

✅ **Loading Screen** (3-5 seconds)
- Aura logo with animations
- Boot sequence steps
- System connecting indicator

✅ **Professional Dashboard**
- Real-time system metrics (CPU, RAM, Storage)
- Quick access launcher
- System status header
- Professional dark theme

## Stopping

- Press `Ctrl+C` in both terminal windows
- Or close the windows

## Troubleshooting

### Port already in use

```powershell
# Find what's using port 9500
Get-NetTCPConnection -LocalPort 9500

# Or port 9000
Get-NetTCPConnection -LocalPort 9000

# Kill the process (replace PID with actual number)
Stop-Process -Id PID -Force
```

### Python not found

```powershell
# Add Python to PATH
$env:Path += ";C:\Python310"  # Adjust version number
python --version
```

### npm install fails

```powershell
# Clear cache
npm cache clean --force

# Try again
npm install
```

### Module not found

```powershell
# Reinstall
pip install --force-reinstall -r requirements.txt
npm install
```

## Next Steps

1. **Explore the UI** - Click buttons, see live updates
2. **Check backend** - Open http://localhost:9500/health
3. **View metrics** - http://localhost:9500/api/system/metrics
4. **Check logs** - Look at terminal output

## Customization

### Change Theme Colors

Edit `frontend/src/components/Dashboard.css`:
```css
--accent-color: #00d4ff;  /* Change to any color */
```

### Change Brand Name

Edit `frontend/src/App.js`:
```javascript
// Change title, logo, etc.
```

### Add New Features

Add components to `frontend/src/components/`
Add endpoints to `backend/core_server.py`

---

**Ready to see Aura OS in action!** 🚀
