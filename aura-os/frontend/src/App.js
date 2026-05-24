import React, { useEffect, useState } from 'react';
import LoadingScreen from './components/LoadingScreen';
import Dashboard from './components/Dashboard';
import './App.css';

function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [systemReady, setSystemReady] = useState(false);

  useEffect(() => {
    // Simulate system startup sequence
    const bootSequence = async () => {
      try {
        // Check backend connectivity
        const response = await fetch('http://localhost:9500/health', {
          method: 'GET',
          timeout: 5000,
        });

        if (response.ok) {
          setSystemReady(true);
          // Keep loading screen visible for professional feel (2 seconds min)
          setTimeout(() => {
            setIsLoading(false);
          }, 2000);
        }
      } catch (error) {
        console.log('Backend not ready, retrying...');
        // Retry after 1 second
        setTimeout(() => {
          setIsLoading(false);
          setSystemReady(false);
        }, 1000);
      }
    };

    bootSequence();
  }, []);

  return (
    <div className="app">
      {isLoading ? (
        <LoadingScreen systemReady={systemReady} />
      ) : (
        <Dashboard />
      )}
    </div>
  );
}

export default App;
