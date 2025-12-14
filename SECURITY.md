# Security Policy

## 🔒 API Key Protection

### Critical: Never Commit API Keys

This repository is configured to prevent accidental exposure of API keys:

1. **`.env` file is in `.gitignore`** - Never commit this file
2. **No hardcoded keys in code** - All keys use environment variables
3. **`.env.example` provided** - Template for configuration

### If You Accidentally Commit an API Key

1. **Rotate the key immediately** at [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **Remove from git history:**
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch .env" \
     --prune-empty --tag-name-filter cat -- --all
   ```
3. **Force push** (if already pushed):
   ```bash
   git push origin --force --all
   ```
4. **Update .gitignore** to ensure it's excluded

## 🔐 Environment Variables

### Required Variables

- `GEMINI_API_KEY` - Your Google Gemini API key

### Setting Environment Variables

**Local Development:**
```powershell
# PowerShell
$env:GEMINI_API_KEY = "your_key_here"

# Or create .env file
GEMINI_API_KEY=your_key_here
```

**Streamlit Cloud:**
- Use Streamlit Secrets (Settings → Secrets)

**Other Platforms:**
- Use platform-specific environment variable settings

## 🛡️ Best Practices

1. ✅ Always use environment variables
2. ✅ Never hardcode credentials
3. ✅ Use `.env.example` as template
4. ✅ Rotate keys regularly
5. ✅ Use different keys for dev/prod
6. ✅ Review commits before pushing
7. ✅ Use secrets management services

## 📋 Security Checklist

Before pushing to GitHub:
- [ ] No API keys in code files
- [ ] `.env` is in `.gitignore`
- [ ] `.env.example` exists (without real keys)
- [ ] All sensitive data removed
- [ ] Commits reviewed with `git diff`

## 🚨 Reporting Security Issues

If you discover a security vulnerability:
1. **Do NOT** create a public issue
2. Contact the repository maintainer privately
3. Include details of the vulnerability
4. Allow time for fix before disclosure

## 📚 Additional Resources

- [GitHub Security Best Practices](https://docs.github.com/en/code-security)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Google AI Security](https://ai.google.dev/safety)

