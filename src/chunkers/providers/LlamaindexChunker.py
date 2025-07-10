from llama_index.core import Document
from llama_index.core.text_splitter import SentenceSplitter

class LlamaIndexChunker:

    def __init__(self):
        self.chunk_size = 1000
        self.overlap_size = 200

    def chunk_documents(self, file_content: list):
        text_splitter = SentenceSplitter(chunk_size=self.chunk_size, chunk_overlap=self.overlap_size)
        chunks = []
        for doc in file_content:
            split_texts = text_splitter.split_text(doc.get_content())
            for chunk_text in split_texts:
                chunks.append(Document(text=chunk_text, metadata=doc.metadata))
        return chunks
