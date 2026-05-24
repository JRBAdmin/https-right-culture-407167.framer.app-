# Aura OS Backend

Python FastAPI backend with WebSocket support and system monitoring.

## Features

- **FastAPI Server**: Modern, fast Python framework
- **WebSocket Support**: Real-time communication with frontend
- **System Monitoring**: CPU, Memory, Disk, Temperature tracking
- **Network Services**: LAN discovery and mesh networking support
- **RESTful API**: JSON endpoints for all services
- **Logging**: Comprehensive error and event logging
- **CORS Enabled**: Cross-origin resource sharing

## Directory Structure

```
backend/
├── core_server.py       # Main FastAPI application
├── config.py            # Configuration management
├── network/             # Network services (planned)
│   └── mesh.py
├── ai/                  # AI services (planned)
│   └── engine.py
├── requirements.txt     # Python dependencies
└── README.md
```

## Installation

### Prerequisites

- Python 3.10+
- pip or conda

### Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
python core_server.py
```

## API Endpoints

### Health & Status

- `GET /` - Root info
- `GET /health` - Health check
- `GET /api/system/info` - System information
- `GET /api/system/metrics` - Current metrics

### System Control

- `POST /api/system/shutdown` - Shutdown
- `POST /api/system/reboot` - Reboot

### Network

- `GET /api/network/status` - Network status

### WebSocket Events

- `connect` - Client connected
- `disconnect` - Client disconnected
- `system-update` - System metrics (emitted every 2 seconds)

## Configuration

Edit `config.py`:

```python
# Server
BACKEND_HOST = '0.0.0.0'
BACKEND_PORT = 5000

# Monitoring
MONITOR_INTERVAL = 2
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
TEMP_THRESHOLD = 80

# Features
FEATURES = {
    'dashboard': True,
    'network_monitor': True,
    'system_monitor': True,
}
```

## Development

### Running Server

```bash
python core_server.py

# Or with custom settings
AURA_DEBUG=true python core_server.py
```

### Testing Endpoints

```bash
# Health check
curl http://localhost:5000/health

# System metrics
curl http://localhost:5000/api/system/metrics

# System info
curl http://localhost:5000/api/system/info
```

### Monitoring

```bash
# View logs
tail -f aura_core.log

# Check if running
lsof -i :5000

# Kill server
pkill -f core_server.py
```

## WebSocket Client

### JavaScript

```javascript
import io from 'socket.io-client';

const socket = io('http://localhost:5000');

socket.on('system-update', (data) => {
  console.log('CPU:', data.cpu);
  console.log('Memory:', data.memory);
  console.log('Online:', data.online);
});
```

### Python

```python
import socketio
import asyncio

sio = socketio.AsyncClient()

@sio.event
async def system_update(data):
    print(f"CPU: {data['cpu']}%")
    print(f"Memory: {data['memory']}%")

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

asyncio.run(main())
```

## Metrics Payload

```json
{
  "cpu": 45.2,
  "memory": 62.5,
  "storage": 35.1,
  "temperature": 52.3,
  "online": true,
  "uptime": "2d 14h",
  "timestamp": "2024-01-20T14:30:45.123456"
}
```

## Systemd Service

Run as service:

```bash
# Copy service file
sudo cp aura-core.service /etc/systemd/system/

# Enable
sudo systemctl enable aura-core

# Start
sudo systemctl start aura-core

# Status
sudo systemctl status aura-core

# Logs
sudo journalctl -u aura-core -f
```

## Production

### Performance

- Use production ASGI server (uvicorn with workers)
- Enable caching for system info
- Implement rate limiting
- Add authentication

### Security

- Implement API authentication
- Add request validation
- Enable HTTPS/TLS
- Restrict CORS origins
- Add rate limiting

### Monitoring

- Enable comprehensive logging
- Set up log rotation
- Monitor resource usage
- Track API performance

## Troubleshooting

### Port already in use

```bash
# Kill existing process
lsof -ti:5000 | xargs kill -9
```

### Import errors

```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

### Permission denied

```bash
# Run with proper permissions
sudo python core_server.py
```

## Extending

### Add Custom Service

```python
@app.get('/api/custom/endpoint')
async def custom_endpoint():
    return {'status': 'ok'}
```

### Add WebSocket Handler

```python
@sio.event
async def custom_event(sid, data):
    logger.info(f'Custom event from {sid}: {data}')
    await sio.emit('response', {'status': 'received'}, to=sid)
```

## Dependencies

- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `python-socketio` - WebSocket support
- `psutil` - System monitoring
- `python-multipart` - Form handling

See `requirements.txt` for versions.

---

**Aura OS v1.0** | Backend Service
