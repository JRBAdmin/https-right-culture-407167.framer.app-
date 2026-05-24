import React, { useEffect, useState } from 'react';
import './LoadingScreen.css';

function LoadingScreen({ systemReady }) {
  const [loadingStep, setLoadingStep] = useState(0);

  const steps = [
    'Initializing Aura Core...',
    'Loading system services...',
    'Connecting to network...',
    'Preparing dashboard...',
    'Ready.',
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setLoadingStep((prev) => (prev < steps.length - 1 ? prev + 1 : prev));
    }, 400);

    return () => clearInterval(interval);
  }, [steps.length]);

  return (
    <div className="loading-screen">
      <div className="loading-container">
        {/* Aura Logo - Animated */}
        <div className="aura-logo">
          <svg
            viewBox="0 0 200 200"
            xmlns="http://www.w3.org/2000/svg"
            className="logo-svg"
          >
            {/* Outer ring */}
            <circle cx="100" cy="100" r="90" fill="none" stroke="#00d4ff" strokeWidth="2" opacity="0.3" />

            {/* Middle ring */}
            <circle cx="100" cy="100" r="70" fill="none" stroke="#00a8cc" strokeWidth="1.5" opacity="0.5" />

            {/* Inner glowing circle */}
            <circle cx="100" cy="100" r="50" fill="none" stroke="#00d4ff" strokeWidth="2" />

            {/* Center dot */}
            <circle cx="100" cy="100" r="8" fill="#00d4ff" />

            {/* Aura letter A */}
            <g transform="translate(100, 100)">
              <path
                d="M -20 10 L 0 -30 L 20 10 M -12 -5 L 12 -5"
                fill="none"
                stroke="#00d4ff"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </g>
          </svg>
        </div>

        {/* Aura Text Branding */}
        <h1 className="aura-title">AURA OS</h1>
        <p className="aura-subtitle">Professional Dashboard System</p>

        {/* Loading Steps */}
        <div className="loading-steps">
          {steps.map((step, index) => (
            <div
              key={index}
              className={`loading-step ${index <= loadingStep ? 'active' : ''} ${
                index === loadingStep ? 'current' : ''
              }`}
            >
              <span className="step-dot"></span>
              <span className="step-text">{step}</span>
            </div>
          ))}
        </div>

        {/* Progress bar */}
        <div className="progress-container">
          <div
            className="progress-bar"
            style={{ width: `${((loadingStep + 1) / steps.length) * 100}%` }}
          />
        </div>

        {/* System status */}
        <div className="system-status">
          <span className={`status-indicator ${systemReady ? 'ready' : 'connecting'}`}></span>
          <span className="status-text">
            {systemReady ? 'System Ready' : 'Connecting...'}
          </span>
        </div>
      </div>

      {/* Background animation */}
      <div className="background-animation">
        <div className="glow glow-1"></div>
        <div className="glow glow-2"></div>
        <div className="glow glow-3"></div>
      </div>
    </div>
  );
}

export default LoadingScreen;
