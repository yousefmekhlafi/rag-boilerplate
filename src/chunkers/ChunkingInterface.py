from abc import ABC, abstractmethod

class ChunkingInterface(ABC):
    @abstractmethod
    def chunk_documents(self, file_content: list, chunk_size: int, overlap_size: int):
        pass
