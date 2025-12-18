import google.generativeai as genai
from web_search import web_search
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def chat_with_agent(user_query, context=None):
    try:
        prompt = f"Context: {context}\nUser Question: {user_query}"
        response = model.generate_content(prompt)
        return response.text
    except:
        return web_search(user_query)
