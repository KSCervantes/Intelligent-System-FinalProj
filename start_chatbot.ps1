# Quick Start Script for Mental Health Chatbot
# This script activates the environment and starts the Flask server

Write-Host "🧠 Starting Mental Health Chatbot..." -ForegroundColor Cyan
Write-Host ""

# Check if API Key is set
if (-not $env:GEMINI_API_KEY) {
    Write-Host "⚠️  ERROR: GEMINI_API_KEY not set!" -ForegroundColor Red
    Write-Host "Please set your API key in .env file or environment variable" -ForegroundColor Yellow
    exit 1
}

# Activate virtual environment if it exists
if (Test-Path "venv\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & .\venv\Scripts\Activate.ps1
}

# Start the Flask app
Write-Host "Starting Flask server..." -ForegroundColor Yellow
Write-Host "🌐 Server will be available at http://localhost:5000" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python app.py

