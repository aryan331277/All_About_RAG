from rank_bm25 import BM25Okapi
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, SparseVectorParams, Filter, FieldCondition, Range
from sentence_transformers import SentenceTransformer, CrossEncoder
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel

docs = []

def chunk_by_tokens(text,token_size=50):
  tokens = text.split()
  chunks = []
  for i in range(0,len(tokens),token_size):
    chunk = ''.join(tokens[i+i:token_size])
    chunks.appen(chunk)
    return chunks

all_chunks = []
for doc in docs:
  all_chunks.extend(chunk_by_tokens(doc, 50))

def splade(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).eval()
    
    def encode(text):
        inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
        with torch.no_grad():
            reps = model(**inputs)
            d_rep = reps.d_rep if hasattr(reps, "d_rep") else reps.last_hidden_state
            vec = torch.log1p(torch.relu(d_rep))
            vec = torch.max(vec, dim=1).values.squeeze()
            indices = vec.nonzero(as_tuple=True)[0]
            values = vec[indices].cpu().numpy()
            indices = indices.cpu().numpy()
        return dict(zip(map(int, indices), map(float, values)))
    
    return encode

def get_learned_sparse(text):
    return splade_encoder(text)


client = QdrantClient(":memory:")
client.create_collection(
    collection_name="docs",
    vectors_config={"dense": VectorParams(size=384, distance=Distance.COSINE)},
    sparse_vectors_config={"sparse": SparseVectorParams()}
)

for i, chunk in enumerate(all_chunks):
    client.upsert(
        collection_name="docs",
        points=[{
            "id": i,
            "vector": {
                "dense": get_dense(chunk),
                "sparse": get_learned_sparse(chunk)  # Learned sparse, NOT BM25
            },
            "payload": {
                "text": chunk,
                "timestamp": 1700000000 + i,
                "category": ["ai", "retrieval"][i % 2],
                "doc_type": "article",
                "score_boost": 1.0 + (i * 0.1)
            }
        }]
    )

def sparse_retrieval(query, top_k=5):
    results = client.search(
        collection_name="docs",
        query_vector=("sparse", get_learned_sparse(query)),
        limit=top_k
    )
    return [(r.payload["text"], r.score) for r in results]

for text, score in sparse_retrieval("neural matching models"):
    print(f"  {score:.4f}: {text}")
