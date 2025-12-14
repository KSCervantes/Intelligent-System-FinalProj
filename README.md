# Mental Health FAQ Chatbot

A smart chatbot powered by Google's Gemini API that answers mental health questions based on a comprehensive FAQ database.

## Features

- 🤖 Powered by Google Gemini AI
- 💬 Interactive web-based chat interface
- 📚 Trained on 600+ mental health FAQ entries
- 🎨 Modern, responsive UI
- 🔒 Secure API key management
- ⚡ Fast and efficient responses

## 🔒 Security Notice

**IMPORTANT**: This project uses environment variables for API keys. Never commit your `.env` file or hardcode API keys in the source code. See [SECURITY.md](SECURITY.md) for details.

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key (Get it from [Google AI Studio](https://makersuite.google.com/app/apikey))
- Mental Health FAQ CSV file

## Setup Instructions

### 1. Get Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### 2. Google Colab Setup (Optional - for data preparation)

1. Open `Mental_Health_Chatbot_Colab.ipynb` in Google Colab
2. Upload your `Mental_Health_FAQ.csv` file
3. Enter your Gemini API key in the notebook
4. Run all cells
5. Download the generated `faq_data.json` file

### 3. Local Flask Setup

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   
   **Copy the example file:**
   ```powershell
   copy .env.example .env
   ```
   
   **Edit `.env` and add your actual API key:**
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   PORT=5000
   ```
   
   ⚠️ **Never commit the `.env` file to version control!**
   
   Or export it directly:
   ```powershell
   $env:GEMINI_API_KEY = "your_api_key_here"
   ```

4. **Prepare FAQ data:**
   
   If you have `faq_data.json` from Colab, place it in the project root.
   
   Otherwise, the app will automatically load from `Mental_Health_FAQ.csv` if available.

5. **Run the Flask application:**
   ```bash
   python app.py
   ```

6. **Open your browser:**
   Navigate to `http://localhost:5000`

## Project Structure

```
.
├── app.py                          # Main Flask application
├── chatbot_helper.py               # Helper functions for chatbot
├── Mental_Health_FAQ.csv           # Original FAQ data
├── faq_data.json                   # Processed FAQ data (generated)
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables (create this)
├── templates/
│   └── index.html                 # Chat interface
└── README.md                      # This file
```

## Usage

1. Start the Flask server
2. Open the web interface in your browser
3. Type your mental health question in the chat input
4. Receive AI-powered responses based on the FAQ database

## API Endpoints

- `GET /` - Main chat interface
- `POST /chat` - Send a message and get a response
  ```json
  {
    "message": "What is depression?"
  }
  ```
- `GET /health` - Health check endpoint

## Features Explained

### Smart Context Matching
The chatbot uses keyword matching to find the most relevant FAQ entries before generating a response, ensuring accurate answers.

### Empathetic Responses
The system prompt is designed to provide supportive, non-judgmental responses while encouraging professional help when appropriate.

### Crisis Detection
The chatbot is configured to recognize crisis situations and encourage immediate professional help.

## Important Disclaimer

⚠️ **This chatbot is for informational purposes only and is not a substitute for professional mental health care.**

- Always consult qualified mental health professionals for diagnosis and treatment
- If you're in crisis, contact emergency services or a crisis hotline immediately
- This tool provides general information based on FAQ data

## Troubleshooting

### API Key Issues
- Make sure your `GEMINI_API_KEY` is set correctly
- Check that the API key is valid and has not expired
- Ensure you have internet connectivity

### FAQ Data Not Loading
- Verify that `faq_data.json` or `Mental_Health_FAQ.csv` exists in the project root
- Check file permissions
- Review console logs for error messages

### Port Already in Use
- Change the `PORT` in `.env` or modify `app.py`
- Kill the process using the port: `lsof -ti:5000 | xargs kill`

## Customization

### Adjusting Response Style
Edit the `system_prompt` in `app.py` to change the chatbot's tone and behavior.

### Adding More FAQ Data
1. Update `Mental_Health_FAQ.csv`
2. Re-run the Colab notebook to generate new `faq_data.json`
3. Restart the Flask app

### Changing UI
Modify `templates/index.html` to customize the chat interface appearance.

## 🚀 Deployment

### GitHub Deployment

1. **Run security check before committing:**
   ```powershell
   python check_security.py
   ```

2. **Initialize git repository:**
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

### Streamlit Cloud Deployment

1. **Push to GitHub** (see above)
2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**
3. **Connect your repository**
4. **Set main file:** `streamlit_app.py`
5. **Add secret:** `GEMINI_API_KEY` in Streamlit Cloud settings
6. **Deploy!**

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.

## 🔒 Security

- **Never commit API keys** - Always use environment variables
- **Run security check:** `python check_security.py` before committing
- **See [SECURITY.md](SECURITY.md)** for security best practices

## License

This project is provided as-is for educational and informational purposes.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review Flask console logs
3. Verify API key and data files are correct

## Future Enhancements

- [ ] Conversation history/memory
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Integration with external mental health resources
- [ ] User feedback system
- [ ] Analytics dashboard

