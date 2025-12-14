# Deployment Guide

This guide covers secure deployment to GitHub and hosting on Streamlit Cloud.

## 🔒 Security Checklist

### ✅ Before Committing to GitHub

1. **Remove all hardcoded API keys** - ✅ Done
2. **Add .env to .gitignore** - ✅ Done
3. **Create .env.example** - ✅ Done
4. **Never commit sensitive data** - ✅ Verified

## 📦 GitHub Deployment

### Step 1: Prepare Repository

1. **Verify .gitignore includes:**
   ```
   .env
   .env.*
   !.env.example
   ```

2. **Check for any remaining API keys:**
   ```powershell
   # Search for API keys in code
   Select-String -Path *.py,*.ps1,*.md -Pattern "AIzaSy" -CaseSensitive
   ```

3. **Create .env.example** (already created):
   ```bash
   # Copy and fill with your actual key
   cp .env.example .env
   # Edit .env and add your real API key
   ```

### Step 2: Initialize Git Repository

```powershell
# Initialize git (if not already done)
git init

# Add all files
git add .

# Check what will be committed (verify .env is NOT included)
git status

# Commit
git commit -m "Initial commit: Mental Health FAQ Chatbot"

# Add remote repository
git remote add origin https://github.com/yourusername/your-repo-name.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Verify Security

After pushing, verify on GitHub that:
- ✅ No `.env` file is visible
- ✅ No API keys in code files
- ✅ `.env.example` is present

## 🚀 Streamlit Cloud Deployment

### Option 1: Use Streamlit Version (Recommended)

The project includes `streamlit_app.py` for Streamlit Cloud deployment.

### Step 1: Prepare for Streamlit

1. **Ensure you have `streamlit_app.py`** (already created)
2. **Update `requirements.txt` for Streamlit:**
   ```txt
   streamlit>=1.28.0
   google-generativeai>=0.3.2
   pandas>=2.2.3
   python-dotenv>=1.0.0
   ```

3. **Create `packages.txt` (if needed for system dependencies):**
   ```txt
   # Usually not needed for this project
   ```

### Step 2: Deploy to Streamlit Cloud

1. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**
2. **Sign in with GitHub**
3. **Click "New app"**
4. **Select your repository**
5. **Configure:**
   - **Main file path:** `streamlit_app.py`
   - **Python version:** 3.11 (recommended) or 3.10
6. **Click "Deploy"**

### Step 3: Add Secrets (API Key)

1. **In Streamlit Cloud dashboard, go to "Settings"**
2. **Click "Secrets"**
3. **Add your API key:**
   ```toml
   GEMINI_API_KEY = "your_actual_api_key_here"
   ```
4. **Save and redeploy**

### Step 4: Verify Deployment

- Check that the app loads
- Test a question
- Verify API key is working

## 🔄 Alternative: Keep Flask App

If you prefer to keep the Flask app instead of Streamlit:

### Option A: Render.com (Free Flask Hosting)

1. **Connect GitHub repository**
2. **Create new Web Service**
3. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
4. **Add Environment Variable:**
   - `GEMINI_API_KEY` = your_api_key
5. **Deploy**

### Option B: Railway.app

1. **Connect GitHub repository**
2. **Create new project**
3. **Add environment variable:**
   - `GEMINI_API_KEY`
4. **Deploy**

### Option C: Heroku (Paid)

1. **Install Heroku CLI**
2. **Create `Procfile`:**
   ```
   web: python app.py
   ```
3. **Deploy:**
   ```bash
   heroku create your-app-name
   heroku config:set GEMINI_API_KEY=your_api_key
   git push heroku main
   ```

## 📋 Files to Include in Repository

### ✅ Should be committed:
- `app.py`
- `streamlit_app.py`
- `requirements.txt`
- `templates/index.html`
- `chatbot_helper.py`
- `check_models.py`
- `README.md`
- `.env.example`
- `.gitignore`
- `Mental_Health_FAQ.csv` (or `faq_data.json`)
- All documentation files

### ❌ Should NOT be committed:
- `.env`
- `__pycache__/`
- `venv/`
- `*.log`
- Any files with API keys

## 🔐 Security Best Practices

1. **Never commit API keys** - Always use environment variables
2. **Use .env.example** - Template for others to follow
3. **Rotate keys if exposed** - If you accidentally commit a key, rotate it immediately
4. **Use secrets management** - Streamlit Cloud secrets, GitHub secrets, etc.
5. **Review commits** - Check `git diff` before pushing

## 🧪 Testing Before Deployment

```powershell
# Test locally without API key in code
$env:GEMINI_API_KEY = "your_key"
python app.py

# Or test Streamlit version
streamlit run streamlit_app.py
```

## 📝 Post-Deployment Checklist

- [ ] App loads successfully
- [ ] API key is working (test a question)
- [ ] No errors in logs
- [ ] FAQ data loads correctly
- [ ] Dark theme displays properly
- [ ] Chat history persists during session
- [ ] No API keys visible in public repository

## 🆘 Troubleshooting

### API Key Not Working
- Check Streamlit secrets are set correctly
- Verify key format (no extra spaces)
- Check API key is valid at Google AI Studio

### App Won't Deploy
- Check Python version compatibility
- Verify all dependencies in `requirements.txt`
- Check build logs for errors

### FAQ Data Not Loading
- Ensure `faq_data.json` or `Mental_Health_FAQ.csv` is in repository
- Check file paths in code

## 🔗 Useful Links

- [Streamlit Cloud](https://streamlit.io/cloud)
- [Google AI Studio](https://makersuite.google.com/app/apikey)
- [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Render.com](https://render.com)
- [Railway.app](https://railway.app)

