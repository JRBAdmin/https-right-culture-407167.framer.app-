#!/usr/bin/env node

/**
 * Aura OS Quick Checker
 * Verifies all dependencies are installed
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  cyan: '\x1b[36m',
};

function log(message, color = 'reset') {
  console.log(`${colors[color]}${message}${colors.reset}`);
}

function check(command, name) {
  try {
    execSync(command, { stdio: 'ignore' });
    log(`[✓] ${name} installed`, 'green');
    return true;
  } catch (e) {
    log(`[X] ${name} NOT installed`, 'red');
    return false;
  }
}

function getVersion(command) {
  try {
    return execSync(command, { encoding: 'utf8' }).split('\n')[0];
  } catch {
    return 'not installed';
  }
}

log('\n================================', 'cyan');
log('  Aura OS - Dependency Checker', 'cyan');
log('================================\n', 'cyan');

let allOk = true;

log('Checking dependencies:', 'yellow');
log('');

// Check Python
if (!check('python --version', 'Python 3.10+')) {
  log('  Download: https://www.python.org/downloads/', 'yellow');
  allOk = false;
} else {
  log(`  Version: ${getVersion('python --version')}`, 'cyan');
}

// Check Node.js
if (!check('node --version', 'Node.js 18+')) {
  log('  Download: https://nodejs.org/', 'yellow');
  allOk = false;
} else {
  log(`  Version: ${getVersion('node --version')}`, 'cyan');
}

// Check npm
if (!check('npm --version', 'npm')) {
  log('  (Usually installs with Node.js)', 'yellow');
  allOk = false;
} else {
  log(`  Version: ${getVersion('npm --version')}`, 'cyan');
}

log('');

if (allOk) {
  log('✓ All dependencies installed!', 'green');
  log('');
  log('Next steps:', 'yellow');
  log('');
  log('  Option 1 - Quick Launch (Windows):');
  log('    Double-click: launch-dev.bat', 'cyan');
  log('');
  log('  Option 2 - PowerShell (Advanced):');
  log('    Run: .\\launch-dev.ps1', 'cyan');
  log('');
  log('  Option 3 - Manual:');
  log('    cd backend', 'cyan');
  log('    python core_server.py', 'cyan');
  log('');
  log('    (In another terminal:)', 'yellow');
  log('    cd frontend', 'cyan');
  log('    npm run dev', 'cyan');
  log('');
  log('Then open: http://localhost:9000', 'cyan');
  log('');
} else {
  log('✗ Missing dependencies!', 'red');
  log('');
  log('Please install all dependencies first.', 'yellow');
  log('');
}
