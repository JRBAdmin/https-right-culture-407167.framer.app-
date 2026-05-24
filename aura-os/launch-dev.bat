@echo off
REM Aura OS Development Launcher - Batch Version
REM Run this file to start Aura OS locally

echo ================================
echo   Aura OS - Development Launcher
echo ================================
echo.

setlocal enabledelayedexpansion

REM Get current directory
cd /d "%~dp0"
set PROJECT_DIR=%cd%
set BACKEND_DIR=%PROJECT_DIR%\backend
set FRONTEND_DIR=%PROJECT_DIR%\frontend

echo [*] Project Location: %PROJECT_DIR%
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] Python not found! Install Python 3.10+
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo [X] Node.js not found! Install Node.js 18+
    echo Download: https://nodejs.org/
    pause
    exit /b 1
)

echo [*] Setting up Backend...
cd /d "%BACKEND_DIR%"

if not exist venv (
    echo     Creating Python virtual environment...
    python -m venv venv
    echo     [OK] Virtual environment created
)

call venv\Scripts\activate.bat

echo     Installing dependencies...
pip install -q -r requirements.txt
echo     [OK] Dependencies installed
echo.

echo [*] Setting up Frontend...
cd /d "%FRONTEND_DIR%"

if not exist node_modules (
    echo     Installing Node.js dependencies...
    call npm install
    echo     [OK] Dependencies installed
) else (
    echo     [OK] Node modules already installed
)

echo.
echo ================================
echo   Starting Services...
echo ================================
echo.
echo [*] Backend:  http://localhost:9500
echo [*] Frontend: http://localhost:9000
echo.
echo Press Ctrl+C to stop
echo.

REM Start backend in new window
echo [*] Starting Backend (Port 9500)...
cd /d "%BACKEND_DIR%"
call venv\Scripts\activate.bat
start "Aura OS - Backend" cmd /k python core_server.py

REM Wait a bit for backend to start
timeout /t 3 /nobreak

REM Start frontend
echo [*] Starting Frontend (Port 9000)...
cd /d "%FRONTEND_DIR%"
set PORT=9000
call npm run dev
