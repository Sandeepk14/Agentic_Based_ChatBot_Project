# #Setup api keys for Groq, OpenAI, and Tavily
# import os
# from dotenv import load_dotenv
# load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# # Setup LLM and Tools
# # from langchain.llms import OpenAI
# # from langchain.chat_models import ChatOpenAI

# from langchain_community.llms import OpenAI
# from langchain_openai import ChatOpenAI


# from langchain_community.tools.tavily_search import TavilySearchResults





# # Initialize LLMs
# openai_llm = ChatOpenAI(temperature=0,  model="gpt-4o-mini")
# groq_llm = OpenAI(temperature=0, model="llama-3.3-70b-versatile")


# # Setup tools
# search_tool = TavilySearchResults( search_type="web",max_results=3)

# # Setup agent with search tool functionality
# from langchain.prebuilt import create_react_agent

# system_prompt = """
# You are a helpful assistant that can search the web for information. You have access to a search tool that can find relevant information online. Use this tool to answer questions that require up-to-date information or specific details that you may not know.
# """

# syatem_prompt = system_prompt.strip()

# agent=create_react_agent(
#     model=groq_llm,
#     tools=[search_tool],
#     state_modifier=syatem_prompt,
    
#     verbose=True
# )

# # Test the agent with a question
# response = agent("What is the latest news on AI?")
# print(response)


import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Correct Imports
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

# Initialize LLMs
openai_llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model="gpt-4o-mini")
groq_llm = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="llama-3.3-70b-versatile")

# Setup search tool
search_tool = TavilySearchResults(api_key=TAVILY_API_KEY, search_type="web", max_results=3)

# Define system prompt
system_prompt = """
You are a helpful AI assistant that can search the web for real-time information. Use the search tool when necessary.
"""

# Create agent (correct function used)
from langgraph.prebuilt import create_react_agent

agent=create_react_agent(
        model=groq_llm,
        tools=[search_tool],
        state_modifier=system_prompt
    )

# Test the agent with a query
query = "can you find github repo for Sandeepk14"
state={"messages": query}
response = agent.invoke(state)
print(response)
