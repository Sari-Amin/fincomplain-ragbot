import faiss
import numpy as np
import pickle
from typing import List, Dict

class VectorStoreBuilder:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add_embeddings(self, embeddings: np.ndarray, meta: List[Dict]):
        self.index.add(embeddings)
        self.metadata.extend(meta)

    def save(self, index_path: str, metadata_path: str):
        faiss.write_index(self.index, index_path)
        with open(metadata_path, 'wb') as f:
            pickle.dump(self.metadata, f)
