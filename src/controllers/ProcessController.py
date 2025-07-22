from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from llama_index.core import SimpleDirectoryReader
from models import ProcessingEnum
from chunkers.ChunkingProviderFactory import ChunkingProviderFactory
from models.db_schemas import DataChunk
from models.ChunkModel import ChunkModel

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
        
        if not os.path.exists(file_path):
            return None

        return None

    def get_file_content(self, file_id: str):

        loader = self.get_file_loader(file_id=file_id)
        if loader:
            return loader.load_data()
        return None

    def process_file_content(self, file_content: list, file_id: str):

        chunker = ChunkingProviderFactory.get_chunker()
        return chunker.chunk_documents(file_content=file_content)

    async def chunk_and_save(self, file_content: list, file_id: str, asset_id: str, project: object, db_client: object, do_reset: int):

        chunk_model = await ChunkModel.create_instance(
            db_client=db_client
        )

        if do_reset == 1:
            _ = await chunk_model.delete_chunks_by_project_id(
                project_id=project.id
            )

        file_chunks = self.process_file_content(
            file_content=file_content,
            file_id=file_id
        )

        if file_chunks is None or len(file_chunks) == 0:
            return None

        file_chunks_records = [
            DataChunk(
                chunk_text=chunk.text,
                chunk_metadata=chunk.metadata,
                chunk_order=i+1,
                chunk_project_id=project.id,
                chunk_asset_id=asset_id
            )
            for i, chunk in enumerate(file_chunks)
        ]

        no_records = await chunk_model.insert_many_chunks(chunks=file_chunks_records)

        return no_records