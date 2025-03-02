

# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain.llms import HuggingFaceHub
# from langgraph.prebuilt import create_react_agent
# from langchain_community.tools.tavily_search import TavilySearchResults
# from langchain_core.messages import AIMessage

# # Load environment variables
# load_dotenv()
# HFT_API_KEY = os.getenv("HFT_API_KEY")  # Hugging Face API Key
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Groq API Key
# TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")  # Tavily API Key

# # Allowed models
# GROQ_MODELS = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
# HUGGINGFACE_MODELS = ["bigscience/bloom", "meta-llama/Llama-2-7b-chat-hf"]

# # Setup Web Search Tool
# search_tool = TavilySearchResults(api_key=TAVILY_API_KEY, search_type="web", max_results=3)

# def get_response_from_ai_agent(model_name, provider, query, allow_search, system_prompt):
#     # Select model provider
#     if provider == "Groq":
#         llm = ChatGroq(model_name=model_name, api_key=GROQ_API_KEY)
#     elif provider == "HuggingFace":
#         llm = HuggingFaceHub(repo_id=model_name, huggingfacehub_api_token=HFT_API_KEY)
#     else:
#         return "⚠️ Invalid provider selected."

#     tools = [search_tool] if allow_search else []

#     # Create AI Agent
#     agent = create_react_agent(model=llm, tools=tools)

#     # Invoke AI Agent
#     state = {"messages": [query]}  # Fixed incorrect formatting
#     response = agent.invoke(state)

#     # Extract AI Messages
#     messages = response.get("messages", [])
#     ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]

#     return ai_messages[-1] if ai_messages else "⚠️ No response from AI."


import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.llms import HuggingFaceHub
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import AIMessage
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()
HFT_API_KEY = os.getenv("HFT_API_KEY")  # Hugging Face API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Groq API Key
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")  # Tavily API Key

# Allowed models
GROQ_MODELS = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
HUGGINGFACE_MODELS = ["bigscience/bloom", "meta-llama/Llama-2-7b-chat-hf"]

# Setup Web Search Tool
search_tool = TavilySearchResults(api_key=TAVILY_API_KEY, search_type="web", max_results=3)

# Initialize memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def get_response_from_ai_agent(model_name, provider, query, allow_search, system_prompt):
    # Select model provider
    if provider == "Groq":
        llm = ChatGroq(model_name=model_name, api_key=GROQ_API_KEY)
    elif provider == "HuggingFace":
        llm = HuggingFaceHub(repo_id=model_name, huggingfacehub_api_token=HFT_API_KEY)
    else:
        return "⚠️ Invalid provider selected."

    tools = [search_tool] if allow_search else []

    # Create AI Agent with Memory
    agent = create_react_agent(model=llm, tools=tools, memory=memory)

    # Invoke AI Agent
    state = {"messages": memory.load_memory_variables({})["chat_history"] + [query]}  
    response = agent.invoke(state)

    # Store AI Response in Memory
    messages = response.get("messages", [])
    ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]
    
    if ai_messages:
        memory.save_context({"input": query}, {"output": ai_messages[-1]})
    
    return ai_messages[-1] if ai_messages else "⚠️ No response from AI."
