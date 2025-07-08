from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

class TextChunker:
    def __init__(self, chunk_size: int = 300, chunk_overlap: int = 50):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def chunk_texts(self, texts: List[str]) -> List[str]:
        return self.splitter.split_texts(texts)
