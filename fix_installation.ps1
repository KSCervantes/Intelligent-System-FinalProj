# Fix Installation Script for Python 3.13 Compatibility
# This script installs compatible versions of packages

Write-Host "🔧 Fixing Installation for Python 3.13..." -ForegroundColor Cyan
Write-Host ""

# Upgrade pip first
Write-Host "Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install packages one by one with compatible versions
Write-Host "Installing Flask..." -ForegroundColor Yellow
pip install flask==3.0.0

Write-Host "Installing Google Generative AI..." -ForegroundColor Yellow
pip install google-generativeai==0.3.2

Write-Host "Installing pandas (latest compatible version)..." -ForegroundColor Yellow
# Try latest pandas first (has better Python 3.13 support)
pip install pandas --upgrade

# If that fails, try installing without building from source
Write-Host "If pandas installation failed, trying with pre-built wheels only..." -ForegroundColor Yellow
pip install pandas --only-binary :all: --upgrade

Write-Host "Installing python-dotenv..." -ForegroundColor Yellow
pip install python-dotenv==1.0.0

Write-Host ""
Write-Host "✅ Installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "If pandas still fails, try:" -ForegroundColor Cyan
Write-Host "  1. Use Python 3.11 or 3.12 (better pandas support)" -ForegroundColor White
Write-Host "  2. Or install pandas without building: pip install pandas --only-binary :all:" -ForegroundColor White

