import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';
import SystemStatus from './SystemStatus';
import QuickLaunch from './QuickLaunch';
import Widgets from './Widgets';
import './Dashboard.css';

function Dashboard() {
  const [systemData, setSystemData] = useState(null);
  const [time, setTime] = useState(new Date());
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    // Initialize WebSocket connection
    const newSocket = io('http://localhost:9500');

    newSocket.on('system-update', (data) => {
      setSystemData(data);
    });

    newSocket.on('connect', () => {
      console.log('Connected to Aura Core');
    });

    setSocket(newSocket);

    return () => newSocket.close();
  }, []);

  useEffect(() => {
    // Update time every second
    const timer = setInterval(() => {
      setTime(new Date());
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  return (
    <div className="dashboard">
      {/* Header */}
      <header className="dashboard-header">
        <div className="header-left">
          <div className="aura-logo-small">
            <svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
              <circle cx="20" cy="20" r="18" fill="none" stroke="#00d4ff" strokeWidth="1" />
              <circle cx="20" cy="20" r="10" fill="none" stroke="#00d4ff" strokeWidth="1" />
              <circle cx="20" cy="20" r="3" fill="#00d4ff" />
            </svg>
          </div>
          <h1 className="dashboard-title">Aura OS</h1>
        </div>

        <div className="header-center">
          <div className="clock">
            <span className="time">
              {time.toLocaleTimeString('en-US', {
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
              })}
            </span>
            <span className="date">
              {time.toLocaleDateString('en-US', {
                weekday: 'short',
                month: 'short',
                day: 'numeric',
              })}
            </span>
          </div>
        </div>

        <div className="header-right">
          <SystemStatus systemData={systemData} />
        </div>
      </header>

      {/* Main Content */}
      <main className="dashboard-content">
        {/* Quick Launch */}
        <section className="section-quick-launch">
          <QuickLaunch />
        </section>

        {/* Widgets Grid */}
        <section className="section-widgets">
          <Widgets systemData={systemData} />
        </section>
      </main>

      {/* Footer */}
      <footer className="dashboard-footer">
        <span className="footer-text">Aura OS v1.0 • Professional Dashboard System</span>
        <span className="footer-status">
          {systemData?.online ? (
            <>
              <span className="status-dot online"></span>
              Online
            </>
          ) : (
            <>
              <span className="status-dot offline"></span>
              Offline
            </>
          )}
        </span>
      </footer>
    </div>
  );
}

export default Dashboard;
