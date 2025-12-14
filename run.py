#!/usr/bin/env python3
"""
Quick start script for Mental Health Chatbot
"""
import os
import sys

def check_requirements():
    """Check if required packages are installed"""
    try:
        import flask
        import google.generativeai
        import pandas
        import dotenv
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e.name}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def check_api_key():
    """Check if API key is configured"""
    api_key = os.getenv('GEMINI_API_KEY', '')
    if not api_key:
        print("⚠️  Warning: GEMINI_API_KEY not found in environment variables")
        print("   Please set it in .env file or PowerShell:")
        print("   $env:GEMINI_API_KEY='your_key_here'")
        return False
    return True

def check_data_files():
    """Check if FAQ data files exist"""
    if os.path.exists('faq_data.json'):
        return True
    elif os.path.exists('Mental_Health_FAQ.csv'):
        print("ℹ️  faq_data.json not found, will load from CSV")
        return True
    else:
        print("❌ Error: Neither faq_data.json nor Mental_Health_FAQ.csv found")
        return False

def main():
    print("🧠 Mental Health Chatbot - Starting...\n")
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Check API key
    api_configured = check_api_key()
    
    # Check data files
    if not check_data_files():
        sys.exit(1)
    
    if not api_configured:
        response = input("\nContinue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    print("\n✅ Starting Flask server...")
    print("🌐 Open http://localhost:5000 in your browser\n")
    
    # Import and run the app
    from app import app
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()

