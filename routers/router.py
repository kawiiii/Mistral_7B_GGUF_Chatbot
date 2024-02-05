from langchain.llms import CTransformers
from langchain import PromptTemplate, LLMChain
from langchain.schema.messages import HumanMessage
from handlers.handler import MyCustomHandler
from threading import Thread
from queue import Queue
import asyncio

class Mistral:
    def __init__(self):
        self.streamer_queue = Queue()
        self.llm = CTransformers(
            model="model/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
            model_type="mistral",
            config={'max_new_tokens': 128,
                    'repetition_penalty': 1.1,
                    'temperature': 0.7,
                    'stream': True,
                    'gpu_layers':100},
                    callbacks= [MyCustomHandler(self.streamer_queue)])
        
        template = """<s>[INST] {prompt} [/INST]"""
        prompt = PromptTemplate(template=template, input_variables=["text"])
        self.chat = LLMChain(prompt=prompt, llm=self.llm)

    def generate(self, query):
        self.chat.invoke(query)

    def start_generation(self, query):
        thread = Thread(target=self.generate, args=(query,))
        thread.start()

    async def response_generator(self, query):
        self.start_generation(query)

        while True:
            value = self.streamer_queue.get()
            if value == None:
                break
            yield value
            self.streamer_queue.task_done()
            await asyncio.sleep(2)