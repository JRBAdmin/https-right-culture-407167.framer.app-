#!/usr/bin/env python3
"""
Aura OS Core Server
Professional-grade backend with WebSocket support and system monitoring
"""

import asyncio
import psutil
import logging
from datetime import datetime, timedelta
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from python_socketio import AsyncServer, ASGIApp
import uvicorn

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('aura_core.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('AuraCore')

# FastAPI app
app = FastAPI(
    title='Aura OS Core',
    description='Professional Dashboard System',
    version='1.0.0'
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Socket.IO setup
sio = AsyncServer(
    async_mode='asgi',
    cors_allowed_origins='*',
    logger=False,
    engineio_logger=False,
)

# Combine FastAPI and Socket.IO
asgi_app = ASGIApp(sio, app)

# System state tracking
class SystemState:
    """Track system metrics and state"""
    boot_time = datetime.now()
    start_time = None
    last_update = None
    
    @staticmethod
    def get_uptime():
        """Get system uptime"""
        elapsed = datetime.now() - SystemState.boot_time
        days = elapsed.days
        hours = elapsed.seconds // 3600
        minutes = (elapsed.seconds % 3600) // 60
        
        if days > 0:
            return f"{days}d {hours}h"
        elif hours > 0:
            return f"{hours}h {minutes}m"
        else:
            return f"{minutes}m"
    
    @staticmethod
    def get_system_metrics():
        """Gather system metrics"""
        try:
            # CPU usage
            cpu_percent = psutil.cpu_percent(interval=1)
            
            # Memory usage
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            
            # Disk usage
            disk = psutil.disk_usage('/')
            disk_percent = disk.percent
            
            # Temperature (Linux only)
            try:
                temps = psutil.sensors_temperatures()
                temp = list(temps.values())[0][0].current if temps else 35
            except:
                temp = 35
            
            # Network
            try:
                # Check if online by trying to get network info
                net_if_addrs = psutil.net_if_addrs()
                online = len(net_if_addrs) > 0
            except:
                online = False
            
            return {
                'cpu': round(cpu_percent, 1),
                'memory': round(memory_percent, 1),
                'storage': round(disk_percent, 1),
                'temperature': round(temp, 1),
                'online': online,
                'uptime': SystemState.get_uptime(),
                'timestamp': datetime.now().isoformat(),
            }
        except Exception as e:
            logger.error(f"Error gathering system metrics: {e}")
            return {
                'cpu': 0,
                'memory': 0,
                'storage': 0,
                'temperature': 35,
                'online': False,
                'uptime': '0m',
                'timestamp': datetime.now().isoformat(),
            }

# Socket.IO event handlers
@sio.event
async def connect(sid, environ):
    """Handle client connection"""
    logger.info(f'Client connected: {sid}')
    # Send initial system state
    await sio.emit('system-update', SystemState.get_system_metrics(), to=sid)

@sio.event
async def disconnect(sid):
    """Handle client disconnection"""
    logger.info(f'Client disconnected: {sid}')

# Background task to emit system updates
async def emit_system_updates():
    """Emit system updates to all connected clients"""
    while True:
        try:
            metrics = SystemState.get_system_metrics()
            await sio.emit('system-update', metrics)
            await asyncio.sleep(2)  # Update every 2 seconds
        except Exception as e:
            logger.error(f"Error emitting system updates: {e}")
            await asyncio.sleep(5)

# FastAPI routes
@app.get('/health')
async def health_check():
    """Health check endpoint"""
    return JSONResponse({
        'status': 'healthy',
        'service': 'Aura Core',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat(),
    })

@app.get('/api/system/metrics')
async def get_system_metrics():
    """Get current system metrics"""
    return JSONResponse(SystemState.get_system_metrics())

@app.get('/api/system/info')
async def get_system_info():
    """Get system information"""
    try:
        return JSONResponse({
            'hostname': psutil.getenv('HOSTNAME', 'Aura System'),
            'platform': psutil.os.name,
            'boot_time': SystemState.boot_time.isoformat(),
            'cpu_count': psutil.cpu_count(),
            'memory_total_gb': round(psutil.virtual_memory().total / (1024**3), 2),
            'disk_total_gb': round(psutil.disk_usage('/').total / (1024**3), 2),
        })
    except Exception as e:
        logger.error(f"Error getting system info: {e}")
        return JSONResponse({'error': str(e)}, status_code=500)

@app.get('/api/network/status')
async def get_network_status():
    """Get network status"""
    try:
        net_connections = psutil.net_connections()
        established = len([c for c in net_connections if c.status == 'ESTABLISHED'])
        
        return JSONResponse({
            'online': len(psutil.net_if_addrs()) > 0,
            'connections': established,
            'interfaces': list(psutil.net_if_addrs().keys()),
        })
    except Exception as e:
        logger.error(f"Error getting network status: {e}")
        return JSONResponse({'error': str(e)}, status_code=500)

@app.post('/api/system/shutdown')
async def shutdown():
    """Shutdown system (requires proper permissions)"""
    logger.warning('Shutdown request received')
    # In production, implement proper authorization
    return JSONResponse({'message': 'Shutdown initiated'})

@app.post('/api/system/reboot')
async def reboot():
    """Reboot system (requires proper permissions)"""
    logger.warning('Reboot request received')
    # In production, implement proper authorization
    return JSONResponse({'message': 'Reboot initiated'})

# Startup and shutdown events
@app.on_event('startup')
async def startup_event():
    """Initialize on startup"""
    logger.info('Aura Core starting up...')
    SystemState.start_time = datetime.now()
    # Start background task for system updates
    asyncio.create_task(emit_system_updates())
    logger.info('Aura Core ready!')

@app.on_event('shutdown')
async def shutdown_event():
    """Cleanup on shutdown"""
    logger.info('Aura Core shutting down...')

# Root endpoint
@app.get('/')
async def root():
    """Root endpoint"""
    return JSONResponse({
        'service': 'Aura OS Core',
        'version': '1.0.0',
        'status': 'running',
        'message': 'Professional Dashboard Backend',
    })

if __name__ == '__main__':
    logger.info('Starting Aura OS Core Server')
    logger.info('Listening on http://0.0.0.0:9500')
    
    uvicorn.run(
        asgi_app,
        host='0.0.0.0',
        port=9500,
        log_level='info',
        access_log=True,
    )
