# 🚀 Aura OS - START HERE (Windows)

## ⚡ Super Quick Start (2 minutes)

### Step 1: Install Dependencies

Download and install (if not already installed):

**Python 3.10+**
- Link: https://www.python.org/downloads/
- ✅ Check "Add Python to PATH"
- ✅ Install

**Node.js 18+ (LTS)**
- Link: https://nodejs.org/
- Download LTS version
- Install with defaults

### Step 2: Run Aura OS

**Option A: Click to Launch (Easiest)**
1. Open project folder: `C:\Users\meagh\aura-os`
2. Double-click: `launch-dev.bat`
3. Wait 30 seconds for startup
4. Opens http://localhost:9000 in browser

**Option B: PowerShell (Recommended)**
1. Open PowerShell
2. Navigate: `cd C:\Users\meagh\aura-os`
3. Run: `.\launch-dev.ps1`
4. Opens http://localhost:9000 automatically

**Option C: Manual (Full Control)**

Terminal 1:
```powershell
cd C:\Users\meagh\aura-os\backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python core_server.py
```

Terminal 2:
```powershell
cd C:\Users\meagh\aura-os\frontend
npm install
npm run dev
```

### Step 3: View the Dashboard

Open browser: **http://localhost:9000**

You'll see:
- ✅ Loading screen with Aura logo
- ✅ Professional dashboard
- ✅ Live system metrics
- ✅ Real-time data from backend

---

## 🎨 What You Get

### Loading Screen
- Animated Aura logo
- Boot sequence animation
- System status indicator
- Professional branding

### Main Dashboard
- **Header**: Aura logo, current time, system status
- **Quick Access**: 4 app launcher buttons
- **Widgets**: CPU, RAM, Storage, Temperature, Network, Uptime
- **Footer**: Status indicator (Online/Offline)

### Real-time Features
- Live CPU/Memory/Storage updates
- Network connectivity indicator
- System uptime tracking
- Responsive design
- Dark professional theme

---

## 🔧 Ports

| Service | Port | URL |
|---------|------|-----|
| Backend | 9500 | http://localhost:9500 |
| Frontend | 9000 | http://localhost:9000 |
| Health Check | 9500 | http://localhost:9500/health |
| API | 9500 | http://localhost:9500/api |

**Why these ports?** Not using common ports (3000, 5000, 8080, 7000) that might be in use.

---

## ❓ Troubleshooting

### "Python not found"
```powershell
# Reinstall Python with "Add to PATH" checked
# Or manually add to PATH:
$env:Path += ";C:\Python310\Scripts"
python --version
```

### "Port already in use"
```powershell
# Kill process using port
Get-NetTCPConnection -LocalPort 9500 | Stop-Process -Force

# Or use different port:
set PORT=9100
npm run dev
```

### "npm: command not found"
- Reinstall Node.js
- Restart computer after install
- Or add to PATH manually

### "CORS or connection errors"
- Make sure backend is running first
- Check http://localhost:9500/health
- Wait 3-5 seconds after starting backend

### "Blank page"
- Check browser console (F12)
- Check backend logs
- Clear browser cache (Ctrl+Shift+Delete)

---

## 📊 Checking Everything Works

### Check Backend Health
```powershell
# Open browser or terminal
curl http://localhost:9500/health

# Should see: {"status":"healthy",...}
```

### Check System Metrics
```powershell
curl http://localhost:9500/api/system/metrics

# Should show: CPU, memory, storage, etc.
```

### Check Frontend
Open browser: http://localhost:9000
- Should see loading screen first
- Then professional dashboard
- Metrics should update every 2 seconds

---

## 🎯 Next Steps

1. ✅ Explore the dashboard
2. ✅ Click the app launcher buttons
3. ✅ Watch metrics update in real-time
4. ✅ Try fullscreen (F11)
5. ✅ Check different screen sizes
6. ✅ Read code in `frontend/src/components/`
7. ✅ Read API in `backend/core_server.py`

---

## 🛠️ Customization

### Change Ports
Edit these files:
- `backend/config.py` - BACKEND_PORT
- `frontend/package.json` - "dev" script
- `frontend/src/App.js` - fetch URL
- `frontend/src/components/Dashboard.js` - socket.io URL

### Change Colors
Edit `frontend/src/components/LoadingScreen.css`:
```css
.aura-title {
  color: #00d4ff;  /* Change this color */
}
```

### Change Theme
Edit any `.css` file in `frontend/src/components/`

### Add Features
Add components to `frontend/src/components/`
Add endpoints to `backend/core_server.py`

---

## 📁 Project Structure

```
aura-os/
├── frontend/                 # React app
│   ├── src/components/      # UI components
│   ├── public/              # Static files
│   ├── package.json
│   └── main.js              # Electron config
├── backend/                  # Python API
│   ├── core_server.py       # Main server
│   ├── config.py            # Settings
│   └── requirements.txt     # Dependencies
├── system/                   # Linux deployment
├── launch-dev.bat           # Windows launcher
├── launch-dev.ps1           # PowerShell launcher
├── DEV_QUICKSTART.md        # Dev guide
└── README.md                # Full docs
```

---

## 💡 Tips

- **Hot reload**: Edit frontend files and refresh browser
- **Backend logs**: Check terminal for errors
- **Performance**: Check Task Manager (Ctrl+Shift+Esc)
- **Network issues**: Check firewall
- **Full screen**: Press F11 or Ctrl+Alt+F
- **Dev tools**: Press F12 in frontend

---

## 🚀 Ready?

### Quick Start Commands

**Windows Batch:**
```
double-click launch-dev.bat
```

**PowerShell:**
```
.\launch-dev.ps1
```

**Manual:**
```
# Terminal 1
cd backend && python core_server.py

# Terminal 2
cd frontend && npm run dev
```

Then open: **http://localhost:9000**

---

**Aura OS is now ready to run locally!** 🎉

Questions? Check `DEV_QUICKSTART.md` for more details.
