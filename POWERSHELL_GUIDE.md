# PowerShell Setup Guide

This guide will help you set up and run the Mental Health Chatbot on Windows PowerShell.

## Quick Start

### Option 1: Automated Setup (Recommended)

1. Open PowerShell in the project directory
2. Run the setup script:
   ```powershell
   .\setup_powershell.ps1
   ```
3. Start the chatbot:
   ```powershell
   .\start_chatbot.ps1
   ```

### Option 2: Manual Setup

1. **Set the API Key** (for current session):
   ```powershell
   $env:GEMINI_API_KEY = "AIzaSyCRDvPbyaO2EoffRrXn-dP6_HBNvllI4cI"
   ```

2. **Make API Key Permanent** (optional):
   ```powershell
   # Add to your PowerShell profile
   notepad $PROFILE
   # Add this line:
   $env:GEMINI_API_KEY = ""
   ```

3. **Create Virtual Environment**:
   ```powershell
   python -m venv venv
   ```

4. **Activate Virtual Environment**:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

5. **Install Dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

6. **Run the Application**:
   ```powershell
   python app.py
   ```
   Or use the quick start:
   ```powershell
   python run.py
   ```

## Common PowerShell Commands

### Check Python Version
```powershell
python --version
```

### Check if API Key is Set
```powershell
$env:GEMINI_API_KEY
```

### List Installed Packages
```powershell
pip list
```

### Deactivate Virtual Environment
```powershell
deactivate
```

### Check if Port is in Use
```powershell
netstat -ano | findstr :5000
```

### Kill Process on Port 5000
```powershell
# Find the process ID first
$process = Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue
if ($process) {
    Stop-Process -Id $process.OwningProcess -Force
}
```

## Troubleshooting

### Execution Policy Error

If you get an execution policy error when running `.ps1` scripts:

```powershell
# Check current policy
Get-ExecutionPolicy

# Set execution policy for current user (recommended)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Or run script with bypass
powershell -ExecutionPolicy Bypass -File .\setup_powershell.ps1
```

### Virtual Environment Not Activating

If activation fails, try:
```powershell
# Use full path
& .\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Module Not Found Errors

Make sure you've activated the virtual environment:
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### API Key Not Working

1. Verify the key is set:
   ```powershell
   echo $env:GEMINI_API_KEY
   ```

2. Set it again if needed:
   ```powershell
   $env:GEMINI_API_KEY = "AIzaSyCRDvPbyaO2EoffRrXn-dP6_HBNvllI4cI"
   ```

3. Restart PowerShell and try again

## Environment Variables in PowerShell

### Set for Current Session
```powershell
$env:VARIABLE_NAME = "value"
```

### Set Permanently (User Level)
```powershell
[System.Environment]::SetEnvironmentVariable("VARIABLE_NAME", "value", "User")
```

### Set Permanently (System Level - requires admin)
```powershell
[System.Environment]::SetEnvironmentVariable("VARIABLE_NAME", "value", "Machine")
```

### View All Environment Variables
```powershell
Get-ChildItem Env:
```

### View Specific Variable
```powershell
$env:VARIABLE_NAME
```

## Running in Background

To run the Flask app in the background:

```powershell
Start-Process python -ArgumentList "app.py" -WindowStyle Hidden
```

To stop it:
```powershell
Get-Process python | Where-Object {$_.Path -like "*venv*"} | Stop-Process
```

## File Structure

After setup, your project should look like:
```
Intelligent System Project/
├── app.py
├── run.py
├── requirements.txt
├── Mental_Health_FAQ.csv
├── faq_data.json
├── venv/                    # Virtual environment
├── templates/
│   └── index.html
├── setup_powershell.ps1
├── start_chatbot.ps1
└── POWERSHELL_GUIDE.md
```

## Next Steps

1. ✅ Run setup script
2. ✅ Start the chatbot
3. 🌐 Open http://localhost:5000 in your browser
4. 💬 Start chatting!

## Need Help?

- Check the main README.md for general information
- Review Flask console output for errors
- Verify all files are in the correct location
- Ensure Python 3.8+ is installed

