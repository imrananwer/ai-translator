import streamlit as st
import os
import google.generativeai as genai

# Set page config
st.set_page_config(page_title="AI Translator - Imran", page_icon="🌐", layout="centered")

# 🌙 Custom Styling (Dark Theme)
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextArea textarea {
            background-color: #1a1c23;
            color: white;
        }
        .stButton button {
            background-color: #007BFF;
            color: white;
        }
        .big-font {
            font-size:20px !important;
            color: #00ccff;
        }
        .result-box {
            background-color: #1a1c23;
            padding: 20px;
            border-radius: 10px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Get API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Languages
languages = [
    "Urdu", "French", "Spanish", "German", "Chinese", "Japanese", "Korean", "Arabic",
    "Portuguese", "Russian", "Hindi", "Bengali", "Turkish", "Italian", "Dutch", "Greek",
    "Polish", "Swedish", "Thai", "Vietnamese", "Hebrew", "Malay", "Czech", "Romanian", "Finnish"
]

# Sidebar
with st.sidebar:
    st.header("🌍 AI Translator")
    st.write("By **Imran Anwer**")
    st.markdown("🎯 Translate English to 25+ languages using Google Gemini.")
    st.write("---")
    lang = st.selectbox("🌐 Select Target Language:", languages)

# Title
st.markdown('<h1 class="big-font">🔤 English to Multilingual Translator</h1>', unsafe_allow_html=True)
st.markdown("💡 *Powered by Gemini AI*")

# Input
text = st.text_area("📝 Enter English text to translate:", height=180)
btn = st.button("🚀 Translate Now")

# Translation
if btn and text:
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Translate the following text to {lang}:\n\n{text}"
        response = model.generate_content(prompt)
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(f"### ✅ Translated to {lang}:")
        st.markdown(f"**{response.text}**")
        st.markdown('</div>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
