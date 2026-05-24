# 🚀 Aura OS - Copy & Paste Quick Start

## 📋 Prerequisites (Install Once)

Before you start, make sure you have:

1. **Python 3.10+**
   - Download: https://www.python.org/downloads/
   - ✅ During install: Check "Add Python to PATH"
   - ✅ Click "Install Now"

2. **Node.js 18+ (LTS)**
   - Download: https://nodejs.org/
   - ✅ Choose LTS version
   - ✅ Install with all defaults

3. **Restart your computer** (important!)

---

## ⚡ Option A: EASIEST - Double-Click to Launch

1. Navigate to: `C:\Users\meagh\aura-os`
2. **Double-click**: `launch-dev.bat`
3. Wait 30 seconds for startup messages
4. Browser opens automatically to: **http://localhost:9000**

Done! 🎉

---

## ⚡ Option B: PowerShell Launch

**Copy and paste these commands:**

```powershell
cd C:\Users\meagh\aura-os
.\launch-dev.ps1
```

Wait for startup, then browser opens to: **http://localhost:9000**

---

## ⚡ Option C: Manual (Copy-Paste Terminal Commands)

### Terminal 1 - Backend:

```powershell
cd C:\Users\meagh\aura-os\backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python core_server.py
```

✅ You should see:
```
INFO:     Application startup complete
INFO:     Uvicorn running on http://0.0.0.0:9500
```

### Terminal 2 - Frontend:

Open a **NEW terminal/PowerShell window** and run:

```powershell
cd C:\Users\meagh\aura-os\frontend
npm install
npm run dev
```

✅ You should see:
```
Compiled successfully!
On Your Network: http://localhost:9000
```

### Browser:

Open: **http://localhost:9000**

---

## 🎯 What Happens

1. **Loading Screen** (3-5 seconds)
   - Aura logo with animations
   - Boot sequence steps
   - "System connecting..." indicator

2. **Professional Dashboard** 
   - Real-time metrics (CPU, RAM, Storage, Network)
   - Live clock with date
   - Quick access app launcher
   - System status footer

3. **Live Updates**
   - Metrics update every 2 seconds
   - WebSocket real-time connection
   - Professional animations

---

## ✅ Verification

### Check Backend is Running:

```powershell
curl http://localhost:9500/health
```

Should show: `{"status":"healthy","service":"Aura Core",...}`

### Check Metrics:

```powershell
curl http://localhost:9500/api/system/metrics
```

Should show: `{"cpu":45.2,"memory":62.5,...}`

### Check Frontend:

Open: **http://localhost:9000**

Should show: Loading screen → Dashboard

---

## 🔌 Ports

| Service | Port | URL |
|---------|------|-----|
| Backend API | 9500 | http://localhost:9500 |
| Frontend UI | 9000 | http://localhost:9000 |
| Health Check | 9500 | http://localhost:9500/health |

---

## ❌ Troubleshooting

### "python" or "python3" not found

```powershell
# Try python3
python3 --version

# Or add Python to PATH manually
$env:Path += ";C:\Users\YourUsername\AppData\Local\Programs\Python\Python310"
python --version
```

### "npm" not found

```powershell
# Restart PowerShell or command prompt
# Then try again

# Or check if Node installed
node --version
```

### "Port already in use"

```powershell
# Kill the process using the port
Get-NetTCPConnection -LocalPort 9500 | Stop-Process -Force
```

### Backend won't connect

```powershell
# Make sure backend started first
# Wait 3-5 seconds after backend starts
# Check: http://localhost:9500/health

# If still fails, check firewall
# Windows Defender Firewall might be blocking port 9500
```

### Blank page in browser

```powershell
# 1. Press F12 to open developer tools
# 2. Check Console tab for errors
# 3. Check backend terminal for error messages
# 4. Clear browser cache: Ctrl+Shift+Delete
# 5. Refresh page: Ctrl+R or F5
```

### "npm ERR!"

```powershell
# Clear npm cache
npm cache clean --force

# Try installing again
cd C:\Users\meagh\aura-os\frontend
npm install
```

---

## 🛑 Stopping

Just press: **Ctrl+C** in each terminal window

Or close the terminal windows.

---

## 🎨 Customize

### Change Port Numbers

Edit these files and search for:
- `9500` (change backend port)
- `9000` (change frontend port)

Files to edit:
- `backend/config.py`
- `backend/core_server.py`
- `frontend/package.json`
- `frontend/src/App.js`
- `frontend/src/components/Dashboard.js`

### Change Colors

Edit: `frontend/src/components/Dashboard.css`

Look for:
```css
--accent-color: #00d4ff;  /* Change to any hex color */
```

### Add Features

Edit:
- Frontend: `frontend/src/components/*.js`
- Backend: `backend/core_server.py`

---

## 📂 What Gets Created

First time you run it, these are created automatically:

```
backend/venv/               (Python virtual environment)
frontend/node_modules/      (npm dependencies)
backend/aura_core.log       (Backend logs)
```

Don't delete these! They contain important files.

---

## 📚 More Info

- **Detailed Guide**: Read `START_HERE.md`
- **Dev Guide**: Read `DEV_QUICKSTART.md`
- **Deployment**: Read `DEPLOYMENT.md`
- **Quick Reference**: See `QUICK_REFERENCE.txt`

---

## 🚀 Ready?

### Quickest Start:

```
1. cd C:\Users\meagh\aura-os
2. Double-click: launch-dev.bat
3. Open: http://localhost:9000
```

### Manual Start:

```
Terminal 1:
cd C:\Users\meagh\aura-os\backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python core_server.py

Terminal 2:
cd C:\Users\meagh\aura-os\frontend
npm install
npm run dev

Browser:
http://localhost:9000
```

---

## 🎉 SUCCESS!

If you see:
- ✅ Loading screen with Aura logo
- ✅ Professional dashboard with metrics
- ✅ Live updates every 2 seconds
- ✅ Click buttons work

**You've successfully launched Aura OS!** 🎊

Now explore the code, customize it, and build something awesome!

---

**Questions?** Check the docs or review the code comments. It's all well-documented!
