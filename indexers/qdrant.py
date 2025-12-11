from qdrant_client import QdrantClient
from qdrant_client.http.models import SparseVectorParams

docs = []

client= QdrantClient(":memory:")
client.create_collection(
    collection_name="docs",
    sparse_vectors_config={"sparse": SparseVectorParams()}
)
