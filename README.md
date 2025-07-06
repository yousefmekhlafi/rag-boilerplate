# RAG-BOILERPLATE

This is a multi-modal rag application boilerplate. 

The majority of the project was engineered along Abu-Bakr Soliman's "mini-rag" tutorial series on YouTube

This project differs in the following points: 

1- Llamaindex is used for efficient multi-modal support (text, images and tables) as separate components/modules.

2- Groq is used for text generation, and huggingface for embeddings. Separating the LLMFactory LLMProvider module into separate generation and embedding modules

3- Hybrid search and Reranking added techniques for better retrieval 

4- Adding a knowledge base for custom business use-cases 

## Requirements 

- Python 3.10 or later

### Install Python using MiniConda

1) Download and install MiniConda from (https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) Create a new virtual environment using the following command: 
```bash
$ conda create -n "YOUR-ENV-NAME" python=3.10
``` 
3) Activating your environment
```bash
$ conda activate "YOUR-ENV-NAME"
```

## Installation 

### Install required package 

```bash
$ pip install -r requirements.txt 
```

### Setup the environment variables 

```bash
$ cp .env.example .env
```

Set your environment variables in `.env` file such as your OPENAI/GROQ/HUGGINGFACE api keys and secrets.

### Run the FastAPI server 

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
