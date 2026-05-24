# Aura OS Dev Launcher - PowerShell
# Run both backend and frontend with one command

Write-Host "================================" -ForegroundColor Cyan
Write-Host "  Aura OS - Development Launcher" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Get script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$backendDir = Join-Path $scriptDir "backend"
$frontendDir = Join-Path $scriptDir "frontend"

# Colors
$success = "Green"
$error = "Red"
$info = "Yellow"

# Check if directories exist
if (-not (Test-Path $backendDir)) {
    Write-Host "[X] Backend directory not found: $backendDir" -ForegroundColor $error
    exit 1
}

if (-not (Test-Path $frontendDir)) {
    Write-Host "[X] Frontend directory not found: $frontendDir" -ForegroundColor $error
    exit 1
}

Write-Host "[*] Aura OS Project Location: $scriptDir" -ForegroundColor $info
Write-Host ""

# Setup Backend
Write-Host "[*] Setting up Backend..." -ForegroundColor $info

$venvDir = Join-Path $backendDir "venv"
if (-not (Test-Path $venvDir)) {
    Write-Host "    Creating Python virtual environment..." -ForegroundColor $info
    cd $backendDir
    python -m venv venv
    Write-Host "    [✓] Virtual environment created" -ForegroundColor $success
}

# Activate venv
$venvActivate = Join-Path $venvDir "Scripts" "Activate.ps1"
& $venvActivate

# Install backend dependencies
$requirementsFile = Join-Path $backendDir "requirements.txt"
if (Test-Path $requirementsFile) {
    Write-Host "    Installing Python dependencies..." -ForegroundColor $info
    pip install -q -r requirements.txt
    Write-Host "    [✓] Dependencies installed" -ForegroundColor $success
}

Write-Host ""

# Setup Frontend
Write-Host "[*] Setting up Frontend..." -ForegroundColor $info

$nodeModules = Join-Path $frontendDir "node_modules"
if (-not (Test-Path $nodeModules)) {
    Write-Host "    Installing Node.js dependencies..." -ForegroundColor $info
    cd $frontendDir
    npm install
    Write-Host "    [✓] Dependencies installed" -ForegroundColor $success
} else {
    Write-Host "    [✓] Node modules already installed" -ForegroundColor $success
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "  Starting Services..." -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[*] Backend:  http://localhost:9500" -ForegroundColor $info
Write-Host "[*] Frontend: http://localhost:9000" -ForegroundColor $info
Write-Host ""
Write-Host "Press Ctrl+C to stop all services" -ForegroundColor $info
Write-Host ""

# Launch backend in background job
Write-Host "[*] Starting Backend (Port 9500)..." -ForegroundColor $info
$backendJob = Start-Job -ScriptBlock {
    cd $args[0]
    $venvActivate = Join-Path $args[0] "venv" "Scripts" "Activate.ps1"
    & $venvActivate
    python core_server.py
} -ArgumentList $backendDir

Start-Sleep -Seconds 3

# Launch frontend
Write-Host "[*] Starting Frontend (Port 9000)..." -ForegroundColor $info
$env:PORT = "9000"
cd $frontendDir

# Run npm dev
try {
    npm run dev
} finally {
    # Cleanup: stop backend job
    Write-Host ""
    Write-Host "[*] Stopping services..." -ForegroundColor $info
    Stop-Job -Job $backendJob
    Remove-Job -Job $backendJob
    Write-Host "[✓] Services stopped" -ForegroundColor $success
}
