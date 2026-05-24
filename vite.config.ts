import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import {defineConfig, loadEnv} from 'vite';

export default defineConfig(({mode}) => {
  const env = loadEnv(mode, '.', '');
  return {
    plugins: [react(), tailwindcss()],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
        '@assets': path.resolve(__dirname, 'attached_assets'),
      },
    },
    server: {
      host: '0.0.0.0',
      allowedHosts: true,
      hmr: false,
    },
  };
});
