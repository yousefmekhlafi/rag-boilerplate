from .EmbeddingEnums import EmbeddingEnums
from .providers import HuggingFaceEmbeddingProvider, HuggingFaceLocalEmbeddingProvider

class EmbeddingProviderFactory:
    def __init__(self, config: dict):
        self.config = config

    def create(self):
        provider = self.config.EMBEDDING_BACKEND
        if provider == EmbeddingEnums.HUGGINGFACE.value:
            return HuggingFaceEmbeddingProvider(
                api_key = self.config.HUGGINGFACE_API_KEY,
                model_id = self.config.EMBEDDING_MODEL_ID
            )

        if provider == EmbeddingEnums.HUGGINGFACE_LOCAL.value:
            return HuggingFaceLocalEmbeddingProvider(
                model_id = self.config.EMBEDDING_MODEL_ID
            )

        return None