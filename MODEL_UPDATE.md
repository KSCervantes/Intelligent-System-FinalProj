# Gemini Model Update

## Issue Fixed
The chatbot was using the deprecated `gemini-pro` model which is no longer available. This caused the error:
```
404 models/gemini-pro is not found for API version v1beta
```

## Solution
Updated all model references to use the newer Gemini models:
- **Primary**: `gemini-1.5-flash` (faster, more cost-effective)
- **Fallback**: `gemini-1.5-pro` (more capable, if flash is unavailable)

## Files Updated
1. ✅ `app.py` - Main Flask application
2. ✅ `chatbot_helper.py` - Helper functions
3. ✅ `Mental_Health_Chatbot_Colab.ipynb` - Colab notebook

## Available Gemini Models

### Current Models (2024):
- `gemini-1.5-pro` - Most capable model, best for complex tasks
- `gemini-1.5-flash` - Faster and more cost-effective, great for most use cases
- `gemini-1.5-flash-8b` - Smaller, even faster model

### Deprecated Models:
- ❌ `gemini-pro` - No longer available
- ❌ `gemini-pro-vision` - No longer available

## Testing
After updating, restart your Flask server and test the chatbot. The error should be resolved.

## If You Still Get Errors

1. **Check your API key**: Make sure it's valid and has access to Gemini models
2. **Update the library**: 
   ```powershell
   pip install --upgrade google-generativeai
   ```
3. **List available models**:
   ```python
   import google.generativeai as genai
   genai.configure(api_key="YOUR_API_KEY")
   for model in genai.list_models():
       if 'generateContent' in model.supported_generation_methods:
           print(model.name)
   ```

