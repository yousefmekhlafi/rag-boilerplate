from ..EmbeddingInterface import EmbeddingInterface
import cohere

class CoHereEmbeddingProvider(EmbeddingInterface):

    def __init__(self, api_key: str, model_id: str, model_dimensions: int):
        self.api_key = api_key
        self.model_id = model_id
        self.model_dimensions = model_dimensions
        self.client = self.get_client()

    def get_client(self):
        return cohere.Client(self.api_key)

    def set_embedding_model(self, model_id: str, model_size: int):
        self.model_id = model_id
        self.model_dimensions = model_size

    def embed_text(self, text: str, document_type: str = None):
        response = self.client.embed(
            texts=[text],
            model=self.model_id,
            input_type="search_document",
            embedding_types=['int8']
        )
        
        return response.embeddings.int8[0]