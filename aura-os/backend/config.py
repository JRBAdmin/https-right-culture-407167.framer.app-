#!/usr/bin/env python3
"""
Aura OS Configuration
Central configuration management
"""

import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class AuraConfig:
    """Aura OS Configuration"""
    
    # System
    SYSTEM_NAME = "Aura OS"
    VERSION = "1.0.0"
    DEBUG = os.getenv('AURA_DEBUG', 'false').lower() == 'true'
    
    # Server
    BACKEND_HOST = os.getenv('AURA_BACKEND_HOST', '0.0.0.0')
    BACKEND_PORT = int(os.getenv('AURA_BACKEND_PORT', 9500))
    FRONTEND_HOST = os.getenv('AURA_FRONTEND_HOST', 'localhost')
    FRONTEND_PORT = int(os.getenv('AURA_FRONTEND_PORT', 9000))
    
    # Paths
    AURA_HOME = os.getenv('AURA_HOME', '/opt/aura')
    LOG_DIR = os.path.join(AURA_HOME, 'logs')
    CONFIG_DIR = os.path.join(AURA_HOME, 'config')
    DATA_DIR = os.path.join(AURA_HOME, 'data')
    
    # Frontend
    FULLSCREEN = True
    KIOSK_MODE = True
    AUTO_LAUNCH = True
    
    # System Monitoring
    MONITOR_INTERVAL = 2  # seconds
    CPU_THRESHOLD = 80  # percent
    MEMORY_THRESHOLD = 80  # percent
    DISK_THRESHOLD = 90  # percent
    TEMP_THRESHOLD = 80  # celsius
    
    # Network
    ENABLE_NETWORK_MESH = True
    NETWORK_PORT = 9000
    BROADCAST_INTERVAL = 5  # seconds
    
    # Security
    CORS_ORIGINS = ['*']
    ALLOW_SHUTDOWN = False  # Require authorization
    ALLOW_REBOOT = False  # Require authorization
    
    # Features
    FEATURES = {
        'dashboard': True,
        'network_monitor': True,
        'system_monitor': True,
        'security_panel': True,
        'settings': True,
        'auto_update': False,
    }
    
    @classmethod
    def to_dict(cls) -> Dict[str, Any]:
        """Convert config to dictionary"""
        return {
            'system_name': cls.SYSTEM_NAME,
            'version': cls.VERSION,
            'debug': cls.DEBUG,
            'backend_host': cls.BACKEND_HOST,
            'backend_port': cls.BACKEND_PORT,
            'frontend_host': cls.FRONTEND_HOST,
            'frontend_port': cls.FRONTEND_PORT,
            'aura_home': cls.AURA_HOME,
            'features': cls.FEATURES,
        }

# Export configuration
config = AuraConfig()
