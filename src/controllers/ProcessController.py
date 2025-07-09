from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from llama_index.core import SimpleDirectoryReader, Document
from llama_index.core.text_splitter import SentenceSplitter

from models import ProcessingEnum

class ProcessController(BaseController):

    def __init__(self, project_id: str):
        super().__init__()

        self.project_id = project_id
        self.project_path = ProjectController().get_project_path(project_id=project_id)

    def get_file_extension(self, file_id: str):
        return os.path.splitext(file_id)[-1]

    def get_file_loader(self, file_id: str):

        file_ext = self.get_file_extension(file_id=file_id)
        file_path = os.path.join(
            self.project_path,
            file_id
        )

        if file_ext in [ProcessingEnum.TXT.value, ProcessingEnum.PDF.value]:
            return SimpleDirectoryReader(input_files=[file_path])

        return None

    def get_file_content(self, file_id: str):

        loader = self.get_file_loader(file_id=file_id)
        return loader.load_data() if loader else None

    def process_file_content(self, file_content: list, file_id: str,
                            chunk_size: int=1000, overlap_size: int=200):

        text_splitter = SentenceSplitter(chunk_size=chunk_size, chunk_overlap=overlap_size)

        chunks = []
        for doc in file_content:
            split_texts = text_splitter.split_text(doc.get_content())
            for chunk_text in split_texts:
                chunks.append(Document(text=chunk_text, metadata=doc.metadata))

        return chunks