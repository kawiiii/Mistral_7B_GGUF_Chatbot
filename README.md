# Mistral-7B Chatbot

![Mistral Chatbot](images/mistral.png)

Welcome to the Mistral-7B Chatbot project! This application combines a FastAPI backend with a Streamlit front end to create an interactive chatbot using the Mistral-7B language model.

## Getting Started

Follow these steps to set up and run the project:

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. Download the Mistral-7B model from [here](https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF) and place it in the models folder.

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

The Mistral-7B model in this project benefits from model quantization to improve efficiency. Quantization involves reducing the precision of numerical values in the model. For Mistral-7B, we use the GGUF quantized model with the following specifications:

- **Name:** mistral-7b-v0.1.Q4_K_M.gguf
- **Quantization Method:** Q4_K_M
- **Bits:** 4
- **Size:** 4.37 GB
- **Max RAM Required:** 6.87 GB
- **Use Case:** Medium, balanced quality - recommended

In this project, [C Transformers library natively integrated with LangChain](library-link) is used that provides Python bindings for GGML models. The integration involves:

1. Instantiating a Model object
2. Loading the GGUF file into it
3. Applying the configuration settings

Additionally, declare the model type (e.g., "mistral") to inform the library about the specific model architecture.


### Usage
Once the application is running, you can chat with the Mistral-7B chatbot through the Streamlit interface. The chat history is logged in chathistory.txt.

Enjoy chatting with Mistral-7B! 🤖