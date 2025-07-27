from .EmbeddingEnums import EmbeddingEnums
from .providers import OpenAIEmbeddingProvider, CoHereEmbeddingProvider

class EmbeddingProviderFactory:
    def __init__(self, config: dict):
        self.config = config

    def create(self):
        provider = self.config.EMBEDDING_BACKEND
        if provider == EmbeddingEnums.OPENAI.value:
            return OpenAIEmbeddingProvider(
                api_key = self.config.OPENAI_API_KEY,
                api_url = self.config.OPENAI_API_URL,
                model_id = self.config.EMBEDDING_MODEL_ID,
                model_dimensions = self.config.EMBEDDING_MODEL_SIZE
            )

        if provider == EmbeddingEnums.COHERE.value:
            return CoHereEmbeddingProvider(
                api_key = self.config.COHERE_API_KEY,
                model_id = self.config.EMBEDDING_MODEL_ID,
                model_dimensions = self.config.EMBEDDING_MODEL_SIZE
            )

        return None