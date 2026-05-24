# Aura OS Frontend

React-based fullscreen dashboard with Electron integration.

## Features

- **Professional UI**: Sleek, modern design with Aura branding
- **Real-time Updates**: WebSocket connection for live system metrics
- **Responsive Design**: Works on all screen sizes
- **Dark Theme**: Eye-appealing dark interface
- **Fullscreen Kiosk**: Runs in kiosk mode for dedicated displays
- **Quick Access**: One-click app launcher
- **System Widgets**: CPU, Memory, Storage, Network monitoring

## Directory Structure

```
frontend/
├── public/               # Static files
│   └── index.html       # HTML entry point
├── src/
│   ├── components/      # React components
│   │   ├── Dashboard.js
│   │   ├── LoadingScreen.js
│   │   ├── SystemStatus.js
│   │   ├── QuickLaunch.js
│   │   ├── Widgets.js
│   │   └── *.css
│   ├── config/          # Configuration
│   ├── App.js           # Main app component
│   ├── App.css
│   ├── index.js         # Entry point
│   └── index.css
├── main.js              # Electron main process
├── package.json
└── README.md
```

## Development

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Setup

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Start Electron (in another terminal)
npm run electron
```

### Building

```bash
# Build for production
npm run build

# Build Electron app
npm run electron-build
```

## Customization

### Theme

Edit `src/config/theme.js`:

```javascript
export const theme = {
  primary: '#00d4ff',
  secondary: '#00a8cc',
  accent: '#00ff88',
  background: '#0a0e27',
  // ...
};
```

### Components

All components use modular CSS. Edit individual `.css` files:

- `Dashboard.css` - Main layout
- `LoadingScreen.css` - Boot animation
- `QuickLaunch.css` - App launcher
- `Widgets.css` - System metrics
- `SystemStatus.css` - Status bar

### Colors & Branding

- **Primary**: `#00d4ff` (Cyan)
- **Secondary**: `#00a8cc` (Dark Cyan)
- **Accent**: `#00ff88` (Green) or `#ffd60a` (Gold)
- **Danger**: `#ff6b35` (Orange)

## API Endpoints

Connect to backend at `http://localhost:5000`:

- `GET /health` - Health check
- `GET /api/system/metrics` - Current metrics
- `GET /api/system/info` - System information
- `GET /api/network/status` - Network status
- `WebSocket` - Real-time updates

## Electron Configuration

### Kiosk Mode

Set in `main.js`:

```javascript
mainWindow = new BrowserWindow({
  kiosk: true,  // Fullscreen, no exit
});
```

### Auto-Launch

Edit systemd service or startup script to auto-launch on boot.

## Troubleshooting

### Backend not connecting

- Ensure backend is running: `python core_server.py`
- Check firewall: `sudo ufw allow 5000`
- Check logs: `journalctl -u aura-core -f`

### Rendering issues

- Clear cache: `npm cache clean --force`
- Reinstall: `rm -rf node_modules && npm install`

### Performance

- Check system resources: `top`, `htop`
- Monitor network: `iftop`
- Check logs: `tail -f ~/aura_core.log`

## Production Deployment

See [DEPLOYMENT.md](../DEPLOYMENT.md) for full deployment guide.

---

**Aura OS v1.0** | Professional Dashboard
