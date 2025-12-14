# Installation Fix for Python 3.13

## Problem
You're getting compilation errors when installing `pandas==2.1.4` because it's trying to build from source on Python 3.13, which has compatibility issues.

## Solutions

### Option 1: Install Pre-built Wheels (Recommended)

Run this in PowerShell:

```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Install pandas using only pre-built wheels (no compilation)
pip install pandas --only-binary :all: --upgrade

# Then install other packages
pip install flask==3.0.0 google-generativeai==0.3.2 python-dotenv==1.0.0
```

### Option 2: Use Updated Requirements

The `requirements.txt` has been updated to use `pandas>=2.2.3` which has better Python 3.13 support. Try:

```powershell
pip install -r requirements.txt
```

### Option 3: Use Python 3.11 or 3.12 (Most Reliable)

If the above doesn't work, consider using Python 3.11 or 3.12 which have better pandas support:

1. Download Python 3.12 from [python.org](https://www.python.org/downloads/)
2. Create a new virtual environment:
   ```powershell
   py -3.12 -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

### Option 4: Skip Pandas (If Not Critical)

If you only need to load CSV data, you can modify the code to use Python's built-in `csv` module instead of pandas. However, the current code uses pandas for CSV loading.

## Quick Fix Script

Run the provided `fix_installation.ps1` script:

```powershell
.\fix_installation.ps1
```

## Verify Installation

After installation, verify everything works:

```powershell
python -c "import pandas; import flask; import google.generativeai; print('✅ All packages installed successfully!')"
```

