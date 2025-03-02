   
    
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from ai_agent import get_response_from_ai_agent

# class RequestState(BaseModel):
#     model_name: str
#     model_provider: str
#     system_prompt: str
#     messages: list[str]
#     allow_search: bool

# # Allowed models per provider
# ALLOWED_MODELS = {
#     "Groq": ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"],
#     "HuggingFace": ["bigscience/bloom", "meta-llama/Llama-2-7b-chat-hf"]
# }

# app = FastAPI(title="AI Chatbot Backend (Groq + Hugging Face)")

# @app.post("/chat")
# def chat(request: RequestState):
#     # Validate model selection
#     if request.model_provider not in ALLOWED_MODELS or request.model_name not in ALLOWED_MODELS[request.model_provider]:
#         raise HTTPException(status_code=400, detail="Invalid model name or provider.")

#     query = request.messages[-1]

#     # Get AI Response
#     response = get_response_from_ai_agent(
#         request.model_name,
#         request.model_provider,
#         query,
#         request.allow_search,
#         request.system_prompt
#     )
    
#     return {"response": response}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)


import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai_agent import get_response_from_ai_agent

# Load environment variables
load_dotenv()
API_URL = os.getenv("API_URL")  # Fetch API URL from .env

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: list[str]
    allow_search: bool

# Allowed models per provider
ALLOWED_MODELS = {
    "Groq": ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"],
    "HuggingFace": ["bigscience/bloom", "meta-llama/Llama-2-7b-chat-hf"]
}

app = FastAPI(title="LangGraph AI Chatbot",icon="🤖")

@app.post("/chat")
def chat(request: RequestState):
    # Validate model selection
    if request.model_provider not in ALLOWED_MODELS or request.model_name not in ALLOWED_MODELS[request.model_provider]:
        raise HTTPException(status_code=400, detail="Invalid model name or provider.")

    query = request.messages[-1]

    # Get AI Response
    response = get_response_from_ai_agent(
        request.model_name,
        request.model_provider,
        query,
        request.allow_search,
        request.system_prompt
    )
    
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

