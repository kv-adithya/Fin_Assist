import google.generativeai as genai
import streamlit as st
genai.configure(api_key=st.secrets["gemini"]["api_key"])

model = genai.GenerativeModel("gemini-pro")

def query_llm(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
