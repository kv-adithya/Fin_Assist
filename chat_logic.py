import google.generativeai as genai
import streamlit as st

# Configure with Streamlit secrets
genai.configure(api_key=st.secrets["gemini"]["api_key"])

model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def get_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"