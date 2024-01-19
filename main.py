# API import Section
from fastapi import FastAPI

# LLM section import
from transformers import pipeline

# IMPORTS FOR TEXT GENERATION CHAIN
from langchain.llms import CTransformers
from langchain import PromptTemplate, LLMChain
import copy

app = FastAPI(
    title="Inference API for Mistral-TB",
    description="A simple API that use Mistral-7B as a chatbot",
    version="1.0",
)

### INITIALIZING MISTRAL -7B MODEL

llm = CTransformers(
        model="model/mistral-7b-v0.1.Q4_K_M.gguf",
        model_type="mistral",
        config={'max_new_tokens': 50,
                'repetition_penalty': 1.1,
                'temperature': 0.7,
                'context_length': 70, })


template = """{text}"""
prompt = PromptTemplate(template=template, input_variables=["text"])
chat = LLMChain(prompt=prompt, llm=llm)


@app.get('/')
async def hello():
    return {"hello" : "Welcome to Mistral Chatbot"}

@app.get('/mistral')
async def mistral(question : str):
    res = chat.run(question)
    result = copy.deepcopy(res)
    return {"result" : result}