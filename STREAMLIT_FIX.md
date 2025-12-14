# Streamlit Deployment Fixes

## Common Issues and Solutions

### Issue 1: FAQ Data Not Loading

**Symptoms:**
- Chatbot responds but doesn't use FAQ data
- Error messages about missing files
- Empty responses

**Solution:**
1. **Ensure files are in repository:**
   - `faq_data.json` OR
   - `Mental_Health_FAQ.csv`
   
2. **Check file paths:**
   - Files must be in the root directory (same level as `streamlit_app.py`)
   - Not in subdirectories

3. **Verify file format:**
   - `faq_data.json` should be valid JSON
   - `Mental_Health_FAQ.csv` should have columns: `Question_ID`, `Questions`, `Answers`

### Issue 2: Dark Theme Not Visible

**Symptoms:**
- White background instead of dark
- Text not visible
- Poor contrast

**Solution:**
- Updated CSS in `streamlit_app.py` includes comprehensive dark theme
- If still not working, check Streamlit Cloud settings
- Try clearing browser cache

### Issue 3: API Key Not Working

**Symptoms:**
- Error about missing API key
- Chatbot doesn't respond

**Solution:**
1. **Set in Streamlit Cloud Secrets:**
   - Go to your app settings
   - Click "Secrets"
   - Add:
     ```toml
     GEMINI_API_KEY = "your_actual_api_key_here"
     ```
2. **Redeploy** after adding secrets

### Issue 4: Elements Not Visible

**Symptoms:**
- Some UI elements missing
- Buttons not showing
- Text cut off

**Solutions:**
1. **Check requirements.txt:**
   - Ensure `streamlit>=1.28.0` is included
   - Use `requirements-streamlit.txt` if needed

2. **Clear browser cache:**
   - Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

3. **Check Streamlit Cloud logs:**
   - Go to app settings
   - View logs for errors

## Files Required for Streamlit Deployment

### Must Include:
- ✅ `streamlit_app.py` (main file)
- ✅ `requirements.txt` or `requirements-streamlit.txt`
- ✅ `faq_data.json` OR `Mental_Health_FAQ.csv`
- ✅ `.gitignore` (to exclude .env)

### Optional but Recommended:
- ✅ `README.md`
- ✅ `.env.example`

### Should NOT Include:
- ❌ `.env` (use Streamlit secrets instead)
- ❌ `venv/` or `__pycache__/`

## Deployment Checklist

Before deploying:
- [ ] `faq_data.json` or `Mental_Health_FAQ.csv` is in repository
- [ ] `requirements.txt` includes `streamlit`
- [ ] No hardcoded API keys in code
- [ ] `.env` is in `.gitignore`
- [ ] Tested locally with `streamlit run streamlit_app.py`

After deploying:
- [ ] Set `GEMINI_API_KEY` in Streamlit Cloud secrets
- [ ] Verify app loads without errors
- [ ] Test a question
- [ ] Check that FAQ data loaded (see sidebar status)
- [ ] Verify dark theme is applied

## Testing Locally

```powershell
# Set API key
$env:GEMINI_API_KEY = "your_key_here"

# Run Streamlit
streamlit run streamlit_app.py
```

## Debugging Tips

1. **Check Streamlit Cloud logs:**
   - App settings → View logs
   - Look for error messages

2. **Add debug info:**
   - The updated `streamlit_app.py` shows status in sidebar
   - Check FAQ data count
   - Verify API key status

3. **Test file loading:**
   - The app now shows success/error messages
   - Check if files are found and loaded

4. **Verify requirements:**
   - Ensure all packages are in `requirements.txt`
   - Check Python version (3.10 or 3.11 recommended)

## Quick Fixes

### If FAQ data not loading:
1. Ensure file is committed to GitHub
2. Check file is in root directory
3. Verify file format is correct
4. Check Streamlit Cloud logs for errors

### If dark theme not working:
1. Hard refresh browser (Ctrl+Shift+R)
2. Check CSS is in `streamlit_app.py`
3. Try different browser

### If API errors:
1. Verify API key in Streamlit secrets
2. Check API key is valid at Google AI Studio
3. Check API quota/limits
4. Review error messages in logs

