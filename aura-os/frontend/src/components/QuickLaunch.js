import React from 'react';
import { BarChart3, Settings, Shield, Network } from 'lucide-react';
import './QuickLaunch.css';

function QuickLaunch() {
  const apps = [
    {
      id: 'dashboard',
      label: 'Dashboard',
      icon: BarChart3,
      color: '#00d4ff',
    },
    {
      id: 'network',
      label: 'Network',
      icon: Network,
      color: '#00ff88',
    },
    {
      id: 'security',
      label: 'Security',
      icon: Shield,
      color: '#ff6b35',
    },
    {
      id: 'settings',
      label: 'Settings',
      icon: Settings,
      color: '#ffd60a',
    },
  ];

  const handleAppClick = (appId) => {
    console.log(`Launching app: ${appId}`);
  };

  return (
    <div className="quick-launch">
      <h2 className="quick-launch-title">Quick Access</h2>
      <div className="quick-launch-grid">
        {apps.map((app) => {
          const Icon = app.icon;
          return (
            <button
              key={app.id}
              className="quick-launch-item"
              onClick={() => handleAppClick(app.id)}
              style={{ '--accent-color': app.color }}
            >
              <div className="app-icon">
                <Icon size={28} />
              </div>
              <span className="app-label">{app.label}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
}

export default QuickLaunch;
