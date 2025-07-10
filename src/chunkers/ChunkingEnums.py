from enum import Enum

class ChunkingProviderEnum(str, Enum):
    LLAMA_INDEX = "llamaindex"
    LANGCHAIN = "langchain"