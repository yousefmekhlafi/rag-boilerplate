from ..EmbeddingInterface import EmbeddingInterface
from openai import OpenAI

class OpenAIEmbeddingProvider(EmbeddingInterface):

    def __init__(self, api_key: str, api_url: str, model_id: str, model_dimensions: int):
        self.api_key = api_key
        self.api_url = api_url
        self.model_id = model_id
        self.model_dimensions = model_dimensions
        self.client = self.get_client()

    def get_client(self):
        return OpenAI(
            api_key=self.api_key,
            base_url=self.api_url
        )

    def set_embedding_model(self, model_id: str, model_size: int):
        self.model_id = model_id
        self.model_dimensions = model_size

    def embed_text(self, text: str, document_type: str = None):
        text = text.replace("\n", " ")
        return self.client.embeddings.create(
            input=[text],
            model=self.model_id,
            dimensions=self.model_dimensions
        ).data[0].embedding