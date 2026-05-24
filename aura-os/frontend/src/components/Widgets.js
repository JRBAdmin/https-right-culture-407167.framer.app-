import React from 'react';
import './Widgets.css';

function Widgets({ systemData }) {
  const widgets = [
    {
      id: 'cpu',
      title: 'Processor',
      icon: '⚙️',
      value: systemData?.cpu || 0,
      unit: '%',
      status: (systemData?.cpu || 0) > 80 ? 'warning' : 'normal',
    },
    {
      id: 'memory',
      title: 'Memory',
      icon: '💾',
      value: systemData?.memory || 0,
      unit: '%',
      status: (systemData?.memory || 0) > 80 ? 'warning' : 'normal',
    },
    {
      id: 'storage',
      title: 'Storage',
      icon: '📦',
      value: systemData?.storage || 0,
      unit: '%',
      status: (systemData?.storage || 0) > 90 ? 'warning' : 'normal',
    },
    {
      id: 'temperature',
      title: 'Temperature',
      icon: '🌡️',
      value: systemData?.temperature || 35,
      unit: '°C',
      status: (systemData?.temperature || 35) > 80 ? 'warning' : 'normal',
    },
    {
      id: 'network',
      title: 'Network',
      icon: '🌐',
      value: systemData?.online ? 'Connected' : 'Disconnected',
      status: systemData?.online ? 'normal' : 'offline',
    },
    {
      id: 'uptime',
      title: 'Uptime',
      icon: '⏱️',
      value: systemData?.uptime || '0d',
      status: 'normal',
    },
  ];

  return (
    <div className="widgets">
      <h2 className="widgets-title">System Metrics</h2>
      <div className="widgets-grid">
        {widgets.map((widget) => (
          <div
            key={widget.id}
            className={`widget ${widget.status}`}
          >
            <div className="widget-header">
              <span className="widget-icon">{widget.icon}</span>
              <span className="widget-title">{widget.title}</span>
            </div>
            <div className="widget-content">
              <span className="widget-value">
                {widget.value}
                {widget.unit && <span className="widget-unit">{widget.unit}</span>}
              </span>
              {widget.id !== 'network' && widget.id !== 'uptime' && (
                <div className="widget-bar">
                  <div
                    className="widget-fill"
                    style={{
                      width: `${Math.min(widget.value, 100)}%`,
                    }}
                  ></div>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Widgets;
