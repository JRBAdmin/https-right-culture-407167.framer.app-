import React from 'react';
import { Cpu, Wifi, HardDrive } from 'lucide-react';
import './SystemStatus.css';

function SystemStatus({ systemData }) {
  if (!systemData) {
    return (
      <div className="system-status-widget">
        <span className="status-loading">Loading...</span>
      </div>
    );
  }

  return (
    <div className="system-status-widget">
      <div className="status-item">
        <Cpu size={16} />
        <span className="status-label">CPU</span>
        <span className="status-value">{systemData.cpu || '0'}%</span>
      </div>

      <div className="status-item">
        <HardDrive size={16} />
        <span className="status-label">RAM</span>
        <span className="status-value">{systemData.memory || '0'}%</span>
      </div>

      <div className="status-item">
        <Wifi size={16} />
        <span className="status-label">Network</span>
        <span className={`status-value ${systemData.online ? 'online' : 'offline'}`}>
          {systemData.online ? 'Online' : 'Offline'}
        </span>
      </div>
    </div>
  );
}

export default SystemStatus;
