"""
Streamlit version of the Mental Health FAQ Chatbot
For deployment on Streamlit Cloud
"""
import streamlit as st
import google.generativeai as genai
import json
import os
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Mental Health FAQ Chatbot",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
    .stApp {
        background-color: #1a1a1a;
    }
    .main .block-container {
        padding-top: 2rem;
    }
    .stChatMessage {
        background-color: #2d2d2d;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm here to help answer questions about mental health based on a comprehensive FAQ database. How can I assist you today?"
        }
    ]

if 'faq_data' not in st.session_state:
    # Load FAQ data
    @st.cache_data
    def load_faq_data():
        """Load FAQ data from JSON or CSV"""
        try:
            if os.path.exists('faq_data.json'):
                with open('faq_data.json', 'r', encoding='utf-8') as f:
                    return json.load(f)
            elif os.path.exists('Mental_Health_FAQ.csv'):
                df = pd.read_csv('Mental_Health_FAQ.csv')
                faq_data = []
                for idx, row in df.iterrows():
                    faq_data.append({
                        'question_id': str(row['Question_ID']),
                        'question': str(row['Questions']).strip(),
                        'answer': str(row['Answers']).strip()
                    })
                return faq_data
            else:
                st.error("FAQ data file not found!")
                return []
        except Exception as e:
            st.error(f"Error loading FAQ data: {str(e)}")
            return []
    
    st.session_state.faq_data = load_faq_data()

# Configure Gemini API
@st.cache_resource
def get_gemini_model():
    """Initialize Gemini model"""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        st.error("⚠️ GEMINI_API_KEY not found! Please set it in Streamlit Cloud secrets.")
        st.stop()
    
    genai.configure(api_key=api_key)
    
    # Try to initialize model with fallbacks
    try:
        return genai.GenerativeModel('models/gemini-2.5-flash')
    except Exception:
        try:
            return genai.GenerativeModel('models/gemini-2.5-pro')
        except Exception:
            return genai.GenerativeModel('models/gemini-flash-latest')

def find_similar_question(user_question, faq_data, top_n=3):
    """Find similar questions from FAQ"""
    user_lower = user_question.lower()
    scores = []
    
    for entry in faq_data:
        question = entry['question'].lower()
        keywords = user_lower.split()
        matches = sum(1 for keyword in keywords if keyword in question)
        if matches > 0:
            scores.append((matches, entry))
    
    scores.sort(reverse=True, key=lambda x: x[0])
    return [entry for _, entry in scores[:top_n]]

def get_chatbot_response(user_question, faq_data, model):
    """Generate response using Gemini API"""
    try:
        # Find similar questions
        similar_questions = find_similar_question(user_question, faq_data)
        
        # Create context
        relevant_context = ""
        if similar_questions:
            relevant_context = "Most relevant FAQ entries:\n"
            for entry in similar_questions:
                relevant_context += f"Q: {entry['question']}\nA: {entry['answer']}\n\n"
        
        # Add general FAQ context
        faq_context = ""
        for entry in faq_data[:100]:  # Limit to avoid token limits
            faq_context += f"Q: {entry['question']}\nA: {entry['answer']}\n\n"
        
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
        
        full_prompt = f"{system_prompt}\n\nUser Question: {user_question}\n\nPlease provide a helpful and empathetic response:"
        
        response = model.generate_content(full_prompt)
        return response.text
        
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}. Please try again or contact support."

# Main UI
st.title("🧠 Mental Health FAQ Assistant")
st.caption("Ask me anything about mental health")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your question here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            model = get_gemini_model()
            response = get_chatbot_response(prompt, st.session_state.faq_data, model)
            st.markdown(response)
    
    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

# Disclaimer
st.markdown("---")
st.warning("⚠️ **Important Disclaimer**: This chatbot provides general information only and is not a substitute for professional mental health care. If you're in crisis, please contact a mental health professional or emergency services immediately.")

