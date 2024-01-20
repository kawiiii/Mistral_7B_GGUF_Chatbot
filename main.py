# API import Section
from fastapi import FastAPI
from routers.router import Mistral


app = FastAPI(
    title="Inference API for Mistral-TB",
    description="A simple API that use Mistral-7B as a chatbot",
    version="1.0",
)

mistral_chatbot = Mistral()

@app.get('/')
async def hello():
    return {"hello": "Welcome to Mistral Chatbot"}

@app.get('/mistral')
async def mistral(question: str):
    result = mistral_chatbot.get_response(question)
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(host="127.0.0.1", port=8000, app=app)

