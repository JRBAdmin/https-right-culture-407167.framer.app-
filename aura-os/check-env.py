#!/usr/bin/env python3
"""
Aura OS Environment Setup Checker
Verify all dependencies and suggest fixes
"""

import os
import subprocess
import sys
from pathlib import Path

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'

def print_header(text):
    print(f"\n{Colors.CYAN}{'='*50}{Colors.END}")
    print(f"{Colors.CYAN}{text.center(50)}{Colors.END}")
    print(f"{Colors.CYAN}{'='*50}{Colors.END}\n")

def check_command(cmd, name, install_help):
    """Check if a command exists"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            timeout=5
        )
        if result.returncode == 0:
            print(f"{Colors.GREEN}[✓]{Colors.END} {name}")
            print(f"    {result.stdout.decode().strip().split(chr(10))[0]}")
            return True
        else:
            print(f"{Colors.RED}[✗]{Colors.END} {name}")
            print(f"    {install_help}")
            return False
    except Exception as e:
        print(f"{Colors.RED}[✗]{Colors.END} {name}")
        print(f"    {install_help}")
        return False

def check_file(path, name):
    """Check if a file exists"""
    if Path(path).exists():
        print(f"{Colors.GREEN}[✓]{Colors.END} {name}")
        return True
    else:
        print(f"{Colors.RED}[✗]{Colors.END} {name}")
        return False

def check_directory(path, name):
    """Check if a directory exists"""
    if Path(path).is_dir():
        print(f"{Colors.GREEN}[✓]{Colors.END} {name}")
        return True
    else:
        print(f"{Colors.RED}[✗]{Colors.END} {name}")
        return False

def main():
    print_header("Aura OS - Environment Checker")
    
    all_ok = True
    
    # System checks
    print(f"{Colors.BLUE}System Dependencies:{Colors.END}")
    
    python_ok = check_command(
        "python --version",
        "Python 3.10+",
        "Download: https://www.python.org/downloads/"
    )
    all_ok = all_ok and python_ok
    
    node_ok = check_command(
        "node --version",
        "Node.js 18+",
        "Download: https://nodejs.org/"
    )
    all_ok = all_ok and node_ok
    
    npm_ok = check_command(
        "npm --version",
        "npm",
        "Usually installs with Node.js. Reinstall Node.js"
    )
    all_ok = all_ok and npm_ok
    
    # Project structure checks
    print(f"\n{Colors.BLUE}Project Structure:{Colors.END}")
    
    project_dir = Path(__file__).parent
    
    backend_ok = check_directory(
        project_dir / "backend",
        "Backend directory"
    )
    all_ok = all_ok and backend_ok
    
    frontend_ok = check_directory(
        project_dir / "frontend",
        "Frontend directory"
    )
    all_ok = all_ok and frontend_ok
    
    # Configuration files
    print(f"\n{Colors.BLUE}Configuration Files:{Colors.END}")
    
    config_ok = check_file(
        project_dir / "backend" / "config.py",
        "Backend config"
    )
    all_ok = all_ok and config_ok
    
    requirements_ok = check_file(
        project_dir / "backend" / "requirements.txt",
        "Python requirements"
    )
    all_ok = all_ok and requirements_ok
    
    package_ok = check_file(
        project_dir / "frontend" / "package.json",
        "Frontend package.json"
    )
    all_ok = all_ok and package_ok
    
    # Installation status checks
    print(f"\n{Colors.BLUE}Installation Status:{Colors.END}")
    
    venv_exists = (project_dir / "backend" / "venv").is_dir()
    if venv_exists:
        print(f"{Colors.GREEN}[✓]{Colors.END} Python virtual environment (created)")
    else:
        print(f"{Colors.YELLOW}[~]{Colors.END} Python virtual environment (not created yet)")
    
    node_modules_exists = (project_dir / "frontend" / "node_modules").is_dir()
    if node_modules_exists:
        print(f"{Colors.GREEN}[✓]{Colors.END} Node modules (installed)")
    else:
        print(f"{Colors.YELLOW}[~]{Colors.END} Node modules (not installed yet)")
    
    # Summary
    print_header("Summary")
    
    if all_ok:
        print(f"{Colors.GREEN}✓ All checks passed!{Colors.END}\n")
        print(f"{Colors.CYAN}Ready to start Aura OS:{Colors.END}\n")
        print(f"  {Colors.YELLOW}Option 1 - Double-click:{Colors.END}")
        print(f"    launch-dev.bat\n")
        print(f"  {Colors.YELLOW}Option 2 - PowerShell:{Colors.END}")
        print(f"    .\\launch-dev.ps1\n")
        print(f"  {Colors.YELLOW}Option 3 - Manual:{Colors.END}")
        print(f"    cd backend && python core_server.py")
        print(f"    (In another terminal:)")
        print(f"    cd frontend && npm run dev\n")
        print(f"  {Colors.CYAN}Then open: http://localhost:9000{Colors.END}\n")
    else:
        print(f"{Colors.RED}✗ Some checks failed!{Colors.END}\n")
        print(f"{Colors.YELLOW}Install missing dependencies and try again.{Colors.END}\n")
        print(f"{Colors.CYAN}Helpful links:{Colors.END}")
        print(f"  Python: https://www.python.org/downloads/")
        print(f"  Node.js: https://nodejs.org/")
        print(f"  Git: https://git-scm.com/\n")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Cancelled{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.END}")
        sys.exit(1)
