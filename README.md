# RAG-BOILERPLATE

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

## Running Docker Compose Services

```bash
$ cd docker
$ sudo docker compose up -d
```

- update `env` with your own username/password


### Run the FastAPI server 

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
