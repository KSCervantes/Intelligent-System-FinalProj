import google.generativeai as genai
import json
import os

def load_faq_data(json_path='faq_data.json'):
    """Load FAQ data from JSON file"""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_faq_context(faq_data, max_entries=100):
    """Create formatted context string from FAQ data"""
    context_parts = []
    for entry in faq_data[:max_entries]:
        q = entry['question'].strip()
        a = entry['answer'].strip()
        context_parts.append(f"Q: {q}\nA: {a}\n")
    return "\n".join(context_parts)

def get_chatbot_response(user_question, faq_data, api_key):
    """Generate response using Gemini API with FAQ context"""
    # Configure Gemini
    genai.configure(api_key=api_key)
    
    # Create context (use first 100 entries to avoid token limits)
    faq_context = create_faq_context(faq_data[:100])
    
    system_prompt = f"""You are a helpful and empathetic mental health assistant chatbot. 
Your role is to provide accurate, supportive, and compassionate information about mental health based on the following FAQ database.

FAQ Database:
{faq_context}

Instructions:
1. Use the FAQ database above to answer user questions accurately
2. If a question matches or is similar to a FAQ entry, provide that answer
3. If the question is not directly in the FAQ, use your knowledge to provide helpful, empathetic responses
4. Always be supportive, non-judgmental, and encourage professional help when appropriate
5. If someone is in crisis, encourage them to seek immediate professional help
6. Keep responses clear, concise, and easy to understand

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
    full_prompt = f"{system_prompt}\n\nUser Question: {user_question}"
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}"

