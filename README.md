# Mistral-7B-Instruct Chatbot

![Mistral Chatbot](images/mistral.png)

Welcome to the Mistral-7B Chatbot project! This application combines a FastAPI backend with a Streamlit front end to create an interactive chatbot using the Mistral-7B language model.

## Getting Started

Follow these steps to set up and run the project:

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kawiiii/Mistral_7B_GGUF_Chatbot.git 
   cd your-repo

2. Download the Mistral-7B model using this command.

   ```bash
   mkdir -p model
   wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf -O model/mistral-7b-instruct-v0.2.Q4_K_M.gguf

Alternatively, you can download the model using a shell script download_model.sh. 


3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   
### Running the Application

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload

2. In a new terminal, run the Streamlit app:

   ```bash
   python3 -m streamlit run app.py

Open your browser and navigate to http://localhost:8501 to interact with the Mistral-7B Chatbot.

### Model Quantization

The Mistral-7B-Instruct model in this project benefits from model quantization to improve efficiency. Quantization involves reducing the precision of numerical values in the model. For Mistral-7B, we use the GGUF quantized model with the following specifications:

- **Name:** mistral-7b-instruct-v0.2.Q4_K_M.gguf
- **Quantization Method:** Q4_K_M
- **Bits:** 4
- **Size:** 4.37 GB
- **Max RAM Required:** 6.87 GB
- **Use Case:** Medium, balanced quality - recommended

In this project, [C Transformers library](https://python.langchain.com/docs/integrations/providers/ctransformers)  natively integrated with LangChain is used that provides Python bindings for GGML models. The integration involves:

1. Instantiating a Model object
2. Loading the GGUF file into it
3. Applying the configuration settings

Additionally, declare the model type (e.g., "mistral") to inform the library about the specific model architecture.


### Usage
Once the application is running, you can chat with the Mistral-7B chatbot through the Streamlit interface. The chat history is logged in chathistory.txt.

Enjoy chatting with Mistral-7B! 🤖
