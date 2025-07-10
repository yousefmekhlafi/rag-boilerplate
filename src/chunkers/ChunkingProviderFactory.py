from helpers.config import get_settings
from .providers.LlamaindexChunker import LlamaIndexChunker
from .providers.LangchainChunker import LangchainChunker
from .ChunkingEnums import ChunkingProviderEnum

class ChunkingProviderFactory:
    @staticmethod
    def get_chunker():
        settings = get_settings()
        provider = settings.CHUNKING_PROVIDER

        if provider == ChunkingProviderEnum.LLAMA_INDEX.value:
            return LlamaIndexChunker()
        elif provider == ChunkingProviderEnum.LANGCHAIN.value:
            return LangchainChunker()
        else:
            raise ValueError(f"Unsupported chunking provider: {provider}")
