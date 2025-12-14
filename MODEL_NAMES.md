# Available Gemini Models

## ✅ Your Available Models

Based on your API key, you have access to **33 models**. Here are the recommended ones:

### Recommended Models:

1. **`models/gemini-2.5-flash`** ⭐ (Recommended - Fast & Efficient)
   - Best for: Most chatbot applications
   - Fast response times
   - Cost-effective

2. **`models/gemini-2.5-pro`** (Most Capable)
   - Best for: Complex reasoning tasks
   - More powerful but slower

3. **`models/gemini-flash-latest`** (Always Latest Flash)
   - Best for: Always using the latest flash model
   - Auto-updates to newest version

4. **`models/gemini-pro-latest`** (Always Latest Pro)
   - Best for: Always using the latest pro model
   - Auto-updates to newest version

## ❌ Deprecated Models (Don't Use)

- `gemini-pro` (old, no longer available)
- `gemini-1.5-flash` (old, no longer available)
- `gemini-1.5-pro` (old, no longer available)

## Important: Model Name Format

**Always include the `models/` prefix!**

✅ Correct: `models/gemini-2.5-flash`
❌ Wrong: `gemini-2.5-flash`

## How to Check Available Models

Run this command anytime:

```powershell
python check_models.py
```

## Current Configuration

Your `app.py` is now configured to use:
1. First tries: `models/gemini-2.5-flash`
2. Falls back to: `models/gemini-2.5-pro`
3. Final fallback: `models/gemini-flash-latest`

This ensures maximum compatibility and reliability.

