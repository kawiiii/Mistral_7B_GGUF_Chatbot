# Create the model directory
mkdir -p model

# Download the Mistral model
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf -O model/mistral-7b-instruct-v0.2.Q4_K_M.gguf