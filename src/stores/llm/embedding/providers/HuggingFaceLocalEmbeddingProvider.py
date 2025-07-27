from ..EmbeddingInterface import EmbeddingInterface
from sentence_transformers import SentenceTransformer

class HuggingFaceLocalEmbeddingProvider(EmbeddingInterface):

    def __init__(self, model_id: str):
        self.model_id = model_id
        self.model = self.get_client()

    def get_client(self):
        return SentenceTransformer(self.model_id)

    def set_embedding_model(self, model_id: str, model_size: int):
        self.model_id = model_id
        self.model = self.get_client()

    def embed_text(self, text: str, document_type: str = None):
        return self.model.encode(text).tolist()