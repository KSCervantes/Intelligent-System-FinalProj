# PowerShell Setup Script for Mental Health Chatbot
# Run this script to set up and start the chatbot

Write-Host "🧠 Mental Health Chatbot - PowerShell Setup" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ $pythonVersion found" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python 3.8+ from python.org" -ForegroundColor Red
    exit 1
}

# Check if API Key is set
if (-not $env:GEMINI_API_KEY) {
    Write-Host "⚠️  WARNING: GEMINI_API_KEY not set!" -ForegroundColor Yellow
    Write-Host "Please set your API key:" -ForegroundColor Cyan
    Write-Host "   `$env:GEMINI_API_KEY = 'your_api_key_here'" -ForegroundColor White
    Write-Host ""
    Write-Host "Or create a .env file with:" -ForegroundColor Cyan
    Write-Host "   GEMINI_API_KEY=your_api_key_here" -ForegroundColor White
    Write-Host ""
    $continue = Read-Host "Continue anyway? (y/n)"
    if ($continue -ne 'y') {
        exit 1
    }
} else {
    Write-Host "✅ API Key configured" -ForegroundColor Green
}

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✅ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Install/upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install requirements
Write-Host "Installing requirements..." -ForegroundColor Yellow
pip install -r requirements.txt
Write-Host "✅ Dependencies installed" -ForegroundColor Green

# Check if data files exist
Write-Host "Checking data files..." -ForegroundColor Yellow
if (Test-Path "faq_data.json") {
    Write-Host "✅ faq_data.json found" -ForegroundColor Green
} elseif (Test-Path "Mental_Health_FAQ.csv") {
    Write-Host "✅ Mental_Health_FAQ.csv found (will be loaded automatically)" -ForegroundColor Green
} else {
    Write-Host "⚠️  No FAQ data file found. Please ensure faq_data.json or Mental_Health_FAQ.csv exists." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "To start the chatbot, run:" -ForegroundColor Cyan
Write-Host "  python app.py" -ForegroundColor White
Write-Host ""
Write-Host "Or use the quick start:" -ForegroundColor Cyan
Write-Host "  python run.py" -ForegroundColor White
Write-Host ""
Write-Host "Then open http://localhost:5000 in your browser" -ForegroundColor Cyan

