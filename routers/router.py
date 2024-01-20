from langchain.llms import CTransformers
from langchain import PromptTemplate, LLMChain
import copy

class Mistral:
    def __init__(self):
        self.llm = CTransformers(
            model="model/mistral-7b-v0.1.Q4_K_M.gguf",
            model_type="mistral",
            config={'max_new_tokens': 50,
                    'repetition_penalty': 1.1,
                    'temperature': 0.7,
                    'context_length': 100,
                    'stream': True})

        template = """{text}"""
        prompt = PromptTemplate(template=template, input_variables=["text"])
        self.chat = LLMChain(prompt=prompt, llm=self.llm)

    def get_response(self, question):
        res = self.chat.run(question)
        result = copy.deepcopy(res)
        return result
