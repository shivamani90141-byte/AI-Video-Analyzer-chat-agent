import streamlit as st
from video_analyzer import analyze_video
from chat_agent import chat_with_agent
import os

st.set_page_config(page_title="AI Video Analyzer & Chat Agent")

st.title("🎥 AI Video Analyzer and Chat Agent")

uploaded_video = st.file_uploader("Upload a video", type=["mp4"])
user_prompt = st.text_input("Ask something about the video")

if uploaded_video and user_prompt:
    video_bytes = uploaded_video.read()
    with st.spinner("Analyzing video..."):
        analysis = analyze_video(video_bytes, user_prompt)
    st.subheader("Video Analysis")
    st.write(analysis)

st.subheader("💬 Chat with AI Agent")
chat_query = st.text_input("Ask a general question")

if chat_query:
    response = chat_with_agent(chat_query)
    st.write(response)
