from ..EmbeddingInterface import EmbeddingInterface
import requests

class HuggingFaceEmbeddingProvider(EmbeddingInterface):

    def __init__(self, api_key: str, model_id: str):
        self.api_key = api_key
        self.model_id = model_id
        self.api_url = f"https://api-inference.huggingface.co/models/{model_id}"
        self.headers = {"Authorization": f"Bearer {api_key}"}

    def set_embedding_model(self, model_id: str, model_size: int):
        self.model_id = model_id
        self.api_url = f"https://api-inference.huggingface.co/models/{model_id}"

    def embed_text(self, text: str, document_type: str = None):
        response = requests.post(self.api_url, headers=self.headers, json={"inputs": text})
        return response.json()[0]