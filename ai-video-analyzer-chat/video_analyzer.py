import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_video(video_bytes, user_prompt):
    response = model.generate_content([
        user_prompt,
        {"mime_type": "video/mp4", "data": video_bytes}
    ])
    return response.text
