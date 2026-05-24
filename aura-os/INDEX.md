# 🎯 AURA OS - WHERE TO START?

Choose your situation below 👇

---

## 🆕 First Time? (Never seen Aura OS before)

**Read this first:** [`START_HERE.md`](START_HERE.md)
- 5 minute overview
- Simple installation
- What you'll see
- Quick walkthrough

---

## ⚡ Just Want to Run It NOW?

**Use this:** [`COPY_PASTE_START.md`](COPY_PASTE_START.md)
- Copy-paste commands
- 3 launch options
- Troubleshooting
- No fluff

**Or just:**
1. Double-click: `launch-dev.bat`
2. Open: http://localhost:9000

Done! 🚀

---

## 🔧 Developer Setup

**Full development guide:** [`DEV_QUICKSTART.md`](DEV_QUICKSTART.md)
- Python setup
- Node.js setup
- Manual startup
- Customization

---

## 📱 Visual Reference

**Quick cheat sheet:** [`QUICK_REFERENCE.txt`](QUICK_REFERENCE.txt)
- All ports and URLs
- File structure
- Commands
- Troubleshooting tips
- Print-friendly format

---

## 🐧 Linux / Lenovo Deployment

**Production deployment guide:** [`DEPLOYMENT.md`](DEPLOYMENT.md)
- Full setup on Lenovo Neo 50q
- Auto-launch on boot
- Systemd services
- Backup & restore
- Troubleshooting

---

## 📚 Documentation

### By Role:

| You are... | Read... |
|-----------|---------|
| Curious | [`START_HERE.md`](START_HERE.md) |
| In a hurry | [`COPY_PASTE_START.md`](COPY_PASTE_START.md) |
| Developer | [`DEV_QUICKSTART.md`](DEV_QUICKSTART.md) |
| System Admin | [`DEPLOYMENT.md`](DEPLOYMENT.md) |
| Need quick ref | [`QUICK_REFERENCE.txt`](QUICK_REFERENCE.txt) |

### By Topic:

| Topic | File |
|-------|------|
| Frontend UI/UX | [`frontend/README.md`](frontend/README.md) |
| Backend API | [`backend/README.md`](backend/README.md) |
| Project overview | [`README.md`](README.md) |
| Quick reference | [`QUICK_REFERENCE.txt`](QUICK_REFERENCE.txt) |

---

## 🚀 Super Quick Start (Windows)

### Option 1: One Click
```
Double-click: launch-dev.bat
Opens: http://localhost:9000
```

### Option 2: PowerShell
```powershell
cd C:\Users\meagh\aura-os
.\launch-dev.ps1
```

### Option 3: Manual
```powershell
# Terminal 1
cd C:\Users\meagh\aura-os\backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python core_server.py

# Terminal 2
cd C:\Users\meagh\aura-os\frontend
npm install
npm run dev
```

Then open: **http://localhost:9000**

---

## 🎨 What You'll See

```
1. Loading Screen (3-5 sec)
   ✨ Animated Aura logo
   📊 Boot sequence
   🔗 System connecting

2. Professional Dashboard
   📈 Real-time metrics
   🎪 App launcher
   ⏰ Live clock
   🌐 Network status

3. Live Updates
   🔄 Every 2 seconds
   💻 CPU/RAM/Storage
   📊 Professional design
```

---

## 🔌 Important Ports

| Service | Port | URL |
|---------|------|-----|
| Frontend | 9000 | http://localhost:9000 |
| Backend | 9500 | http://localhost:9500 |
| Health | 9500 | http://localhost:9500/health |
| Metrics | 9500 | http://localhost:9500/api/system/metrics |

---

## 🛠️ Prerequisites (Install Once)

- ✅ Python 3.10+ (add to PATH)
- ✅ Node.js 18+ LTS
- ✅ Restart computer

---

## ❓ Common Questions

**Q: Does it work on Windows?**
A: Yes! This guide is for Windows. Linux deployment guide is [`DEPLOYMENT.md`](DEPLOYMENT.md)

**Q: Can I customize colors?**
A: Yes! Edit `frontend/src/components/Dashboard.css`

**Q: Can I add features?**
A: Yes! Add React components in `frontend/src/components/` and Python endpoints in `backend/core_server.py`

**Q: What if port 9000 or 9500 is already used?**
A: Edit the port numbers in config files, or kill the process using the port.

**Q: Does it work on Mac?**
A: Most of it, yes. Some system monitoring might differ. Linux deployment is recommended.

---

## 📞 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Python not found | Reinstall with "Add to PATH" ✓ |
| npm not found | Restart terminal/computer |
| Port in use | `Get-NetTCPConnection -LocalPort 9500 \| Stop-Process` |
| Backend won't connect | Wait 3-5 seconds, check http://localhost:9500/health |
| Blank page | Press F12, check console, clear cache |

More troubleshooting in: [`COPY_PASTE_START.md`](COPY_PASTE_START.md)

---

## 📂 File Structure

```
aura-os/
├── 📄 START_HERE.md .................. 👈 First-time users
├── 📄 COPY_PASTE_START.md ........... Copy-paste commands
├── 📄 QUICK_REFERENCE.txt .......... Cheat sheet
│
├── 🚀 launch-dev.bat ................ Windows launcher
├── 🚀 launch-dev.ps1 ............... PowerShell launcher
│
├── 📂 frontend/ ..................... React app
│   └── README.md ................... Frontend docs
│
├── 📂 backend/ ..................... Python API
│   └── README.md ................... Backend docs
│
├── 📂 system/ ...................... Linux files
│
├── README.md ....................... Project overview
├── DEPLOYMENT.md ................... Linux/Lenovo guide
└── This file ........................ Navigation guide
```

---

## ✅ Next Steps

1. **Choose your path above** 👆
2. **Follow the appropriate guide**
3. **Run one of the launch commands**
4. **Open http://localhost:9000**
5. **See the professional dashboard!** 🎉

---

## 🎓 Learning Path

### Beginner (New to Aura OS)
```
1. Read: START_HERE.md
2. Run: launch-dev.bat
3. Explore: UI in browser
4. Check: Code in frontend/src/
```

### Developer (Want to customize)
```
1. Read: DEV_QUICKSTART.md
2. Manual setup: COPY_PASTE_START.md
3. Edit: frontend/src/components/
4. Add: New React components
5. Edit: backend/core_server.py
6. Add: New API endpoints
```

### DevOps (Lenovo deployment)
```
1. Read: DEPLOYMENT.md
2. Reset: CMOS or replace SSD
3. Install: Ubuntu 22.04 LTS
4. Run: system/setup.sh
5. Auto-launch: On boot
```

---

## 🎯 Your Mission

Choose one:

- [ ] **Just see it run** → Use `launch-dev.bat`
- [ ] **Learn the code** → Read `frontend/README.md` and `backend/README.md`
- [ ] **Customize it** → Edit CSS/JS files and add features
- [ ] **Deploy on Lenovo** → Follow `DEPLOYMENT.md`
- [ ] **All of the above** → You're awesome! 🚀

---

## 🎉 Ready?

### The Absolute Quickest Way:

```
Go to: C:\Users\meagh\aura-os
Double-click: launch-dev.bat
```

That's it! Browser will open automatically to:
### **http://localhost:9000**

---

**Made with 💙 for awesome builders!**

*Questions? Check the docs. Code has comments. You got this!* 🚀
