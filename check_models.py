"""
Script to check available Gemini models for your API key
"""
import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv

# Fix encoding for Windows PowerShell
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables
load_dotenv()

# Get API key - MUST be set via environment variable
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    print("ERROR: GEMINI_API_KEY environment variable is required!")
    print("Please set it in your .env file or environment variables.")
    sys.exit(1)
genai.configure(api_key=api_key)

print("Checking available Gemini models...\n")
print("=" * 60)

try:
    # List all available models
    models = genai.list_models()
    
    print("API Key is valid!\n")
    print("Available models that support generateContent:\n")
    
    available_models = []
    for model in models:
        if 'generateContent' in model.supported_generation_methods:
            available_models.append(model.name)
            print(f"  [OK] {model.name}")
            if model.display_name:
                print(f"    Display Name: {model.display_name}")
            print()
    
    print("=" * 60)
    print(f"\nTotal models found: {len(available_models)}\n")
    
    # Recommend a model
    if available_models:
        # Prefer flash models (faster), then pro models
        recommended = None
        for model_name in available_models:
            if 'flash' in model_name.lower():
                recommended = model_name
                break
        if not recommended:
            for model_name in available_models:
                if 'pro' in model_name.lower():
                    recommended = model_name
                    break
        
        if recommended:
            print(f"Recommended model: {recommended}")
            print(f"\nUpdate your app.py to use:")
            print(f'  model = genai.GenerativeModel("{recommended}")')
        else:
            print(f"First available model: {available_models[0]}")
            print(f"\nUpdate your app.py to use:")
            print(f'  model = genai.GenerativeModel("{available_models[0]}")')
    
except Exception as e:
    print(f"Error: {str(e)}")
    print("\nPossible issues:")
    print("  1. API key is invalid or expired")
    print("  2. API key doesn't have access to Gemini models")
    print("  3. Network connection issue")
    print("  4. google-generativeai library needs update")
    print("\nTry:")
    print("  pip install --upgrade google-generativeai")

