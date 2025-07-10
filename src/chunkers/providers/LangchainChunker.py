from langchain.text_splitter import RecursiveCharacterTextSplitter
from llama_index.core import Document

class LangchainChunker:

    def __init__(self):
        self.chunk_size = 500
        self.overlap_size = 50

    def chunk_documents(self, file_content: list):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.overlap_size,
            length_function=len
        )
        chunks = []
        for doc in file_content:
            split_texts = text_splitter.split_text(doc.get_content())
            for chunk_text in split_texts:
                chunks.append(Document(text=chunk_text, metadata=doc.metadata))
        return chunks
