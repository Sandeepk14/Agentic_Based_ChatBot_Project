

# import streamlit as st
# import requests
# import time
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Set Page Configuration
# st.set_page_config(page_title="🤖 AI Chatbot (Groq + Hugging Face)", page_icon="💬", layout="wide")

# # Sidebar Configuration
# st.sidebar.header("⚙️ Chatbot Configuration")
# st.sidebar.write("Customize the AI Agent")

# # Model Provider Selection
# provider = st.sidebar.radio("📌 Select Provider:", ["Groq", "HuggingFace"])

# # Model Options
# GROQ_MODELS = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
# HUGGINGFACE_MODELS = ["bigscience/bloom", "meta-llama/Llama-2-7b-chat-hf"]

# # Select Model Based on Provider
# if provider == "Groq":
#     selected_model = st.sidebar.selectbox("🧠 Groq Model:", GROQ_MODELS)
# else:
#     selected_model = st.sidebar.selectbox("🧠 Hugging Face Model:", HUGGINGFACE_MODELS)

# # System Prompt Input
# system_prompt = st.sidebar.text_area(
#     "📜 Define AI Agent:",
#     "You are a helpful AI assistant that can search the web for real-time information.",
#     height=80
# )

# # Web Search Option
# allow_web_search = st.sidebar.checkbox("🔍 Allow Web Search")

# # API URL
# API_URL = "http://127.0.0.1:8000/chat"

# # Page Title
# st.markdown("<h1 style='text-align: center;'>🤖 AI Chatbot (Groq + Hugging Face)</h1>", unsafe_allow_html=True)
# st.markdown("<h4 style='text-align: center;'>🚀 Ask me anything below</h4>", unsafe_allow_html=True)
# st.write("---")

# # Chat Messages Storage
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display Chat History
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # User Input
# user_query = st.chat_input("💬 Type your message here...")

# # API Call & Response Handling
# if user_query:
#     # Save User Message
#     st.session_state.messages.append({"role": "user", "content": f"👤 **You:** {user_query}"})
#     with st.chat_message("user"):
#         st.markdown(f"👤 **You:** {user_query}")

#     # AI Processing
#     with st.chat_message("assistant"):
#         with st.spinner("🤖 Thinking..."):
#             time.sleep(1)  # Simulate processing delay

#             # Send Request to API
#             payload = {
#                 "model_name": selected_model,
#                 "model_provider": provider,
#                 "system_prompt": system_prompt,
#                 "messages": [user_query],
#                 "allow_search": allow_web_search
#             }

#             try:
#                 response = requests.post(API_URL, json=payload)
#                 if response.status_code == 200:
#                     response_data = response.json()
#                     ai_response = f"🤖 **AI:** {response_data.get('response', 'No response received.')}"
#                 else:
#                     ai_response = "⚠️ **Error:** API is not responding."

#             except Exception as e:
#                 ai_response = f"⚠️ **Error:** {str(e)}"

#             # Display AI Response
#             st.markdown(ai_response)
#             st.session_state.messages.append({"role": "assistant", "content": ai_response})



import os
import streamlit as st
import requests
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_URL = os.getenv("API_URL")  # Fetch API URL from .env

# Set Page Configuration
st.set_page_config(page_title="🤖LangGraph AI Chatbot Agent", page_icon="💬", layout="wide")

# Sidebar Configuration
st.sidebar.header("⚙️ Chatbot Configuration")
st.sidebar.write("Customize the AI Agent")

# Model Provider Selection
provider = st.sidebar.radio("📌 Select Provider:", ["Groq", "HuggingFace"])

# Model Options
GROQ_MODELS = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
HUGGINGFACE_MODELS = ["bigscience/bloom", "meta-llama/Llama-2-7b-chat-hf"]

# Select Model Based on Provider
if provider == "Groq":
    selected_model = st.sidebar.selectbox("🧠 Groq Model:", GROQ_MODELS)
else:
    selected_model = st.sidebar.selectbox("🧠 Hugging Face Model:", HUGGINGFACE_MODELS)

# System Prompt Input
system_prompt = st.sidebar.text_area(
    "📜 Define AI Agent:",
    "You are a helpful AI assistant that can search the web for real-time information.",
    height=80
)

# Web Search Option
allow_web_search = st.sidebar.checkbox("🔍 Allow Web Search")

# Page Title
st.markdown("<h1 style='text-align: center;'>🤖LangGraph AI Chatbot Agent</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>🚀 Ask me anything below</h4>", unsafe_allow_html=True)
st.write("---")

# Chat Messages Storage
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input
user_query = st.chat_input("💬 Type your message here...")

# API Call & Response Handling
if user_query:
    # Save User Message
    st.session_state.messages.append({"role": "user", "content": f"👤 **You:** {user_query}"})
    with st.chat_message("user"):
        st.markdown(f"👤 **You:** {user_query}")

    # AI Processing
    with st.chat_message("assistant"):
        with st.spinner("🤖 Thinking..."):
            time.sleep(1)  # Simulate processing delay

            # Send Request to API
            payload = {
                "model_name": selected_model,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages": [user_query],
                "allow_search": allow_web_search
            }

            try:
                response = requests.post(API_URL, json=payload)
                if response.status_code == 200:
                    response_data = response.json()
                    ai_response = f"🤖 **AI:** {response_data.get('response', 'No response received.')}"
                else:
                    ai_response = "⚠️ **Error:** API is not responding."

            except Exception as e:
                ai_response = f"⚠️ **Error:** {str(e)}"

            # Display AI Response
            st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
