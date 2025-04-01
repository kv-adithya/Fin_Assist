import google.generativeai as genai

genai.configure(api_key="AIzaSyBQnJkSx4p2f7y23W8YMroRFc_fGGm6ybg")

model = genai.GenerativeModel("gemini-pro")

def query_llm(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
