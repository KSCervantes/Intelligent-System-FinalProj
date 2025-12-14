from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API - MUST be set via environment variable
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY environment variable is required. "
        "Please set it in your .env file or environment variables. "
        "Never commit API keys to version control!"
    )
genai.configure(api_key=GEMINI_API_KEY)

# Load FAQ data
def load_faq_data(json_path='faq_data.json'):
    """Load FAQ data from JSON file"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {json_path} not found. Loading from CSV...")
        return load_faq_from_csv('Mental_Health_FAQ.csv')

def load_faq_from_csv(csv_path):
    """Load FAQ data from CSV file if JSON doesn't exist"""
    import pandas as pd
    df = pd.read_csv(csv_path)
    faq_data = []
    for idx, row in df.iterrows():
        faq_data.append({
            'question_id': str(row['Question_ID']),
            'question': str(row['Questions']).strip(),
            'answer': str(row['Answers']).strip()
        })
    return faq_data

def create_faq_context(faq_data, max_entries=150):
    """Create formatted context string from FAQ data"""
    context_parts = []
    # Use a subset to avoid token limits
    for entry in faq_data[:max_entries]:
        q = entry['question'].strip()
        a = entry['answer'].strip()
        context_parts.append(f"Q: {q}\nA: {a}\n")
    return "\n".join(context_parts)

def find_similar_question(user_question, faq_data, top_n=3):
    """Find similar questions from FAQ using simple keyword matching"""
    user_lower = user_question.lower()
    scores = []
    
    for entry in faq_data:
        question = entry['question'].lower()
        # Simple keyword matching
        keywords = user_lower.split()
        matches = sum(1 for keyword in keywords if keyword in question)
        if matches > 0:
            scores.append((matches, entry))
    
    # Sort by match count and return top N
    scores.sort(reverse=True, key=lambda x: x[0])
    return [entry for _, entry in scores[:top_n]]

def get_chatbot_response(user_question, faq_data, api_key):
    """Generate response using Gemini API with FAQ context"""
    if not api_key:
        return "Error: Gemini API key not configured. Please set GEMINI_API_KEY environment variable."
    
    try:
        # Find similar questions first
        similar_questions = find_similar_question(user_question, faq_data)
        
        # Create context from similar questions and general FAQ
        relevant_context = ""
        if similar_questions:
            relevant_context = "Most relevant FAQ entries:\n"
            for entry in similar_questions:
                relevant_context += f"Q: {entry['question']}\nA: {entry['answer']}\n\n"
        
        # Add general FAQ context (limited to avoid token limits)
        faq_context = create_faq_context(faq_data, max_entries=100)
        
        system_prompt = f"""You are a helpful and empathetic mental health assistant chatbot. 
Your role is to provide accurate, supportive, and compassionate information about mental health based on the following FAQ database.

{relevant_context}

Additional FAQ Database Context:
{faq_context[:3000]}

Instructions:
1. Use the FAQ database above to answer user questions accurately
2. If a question matches or is similar to a FAQ entry, provide that answer
3. If the question is not directly in the FAQ, use your knowledge to provide helpful, empathetic responses
4. Always be supportive, non-judgmental, and encourage professional help when appropriate
5. If someone is in crisis or mentions self-harm, encourage them to seek immediate professional help
6. Keep responses clear, concise, and easy to understand
7. If you're unsure, acknowledge it and suggest consulting a mental health professional

Remember: You are not a replacement for professional mental health care. Always encourage users to consult with qualified mental health professionals for diagnosis and treatment.
"""
        
        # Initialize model - using gemini-2.5-flash (faster) or gemini-2.5-pro (more capable)
        # Model names must include 'models/' prefix
        try:
            model = genai.GenerativeModel('models/gemini-2.5-flash')
        except Exception:
            try:
                model = genai.GenerativeModel('models/gemini-2.5-pro')
            except Exception:
                # Fallback to latest versions
                model = genai.GenerativeModel('models/gemini-flash-latest')
        
        # Create full prompt
        full_prompt = f"{system_prompt}\n\nUser Question: {user_question}\n\nPlease provide a helpful and empathetic response:"
        
        # Generate response
        response = model.generate_content(full_prompt)
        return response.text
        
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}. Please try again or contact support."

# Load FAQ data at startup
faq_data = load_faq_data()

@app.route('/')
def index():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Get response from chatbot
        bot_response = get_chatbot_response(user_message, faq_data, GEMINI_API_KEY)
        
        return jsonify({
            'response': bot_response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'faq_entries': len(faq_data),
        'api_configured': bool(GEMINI_API_KEY)
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

