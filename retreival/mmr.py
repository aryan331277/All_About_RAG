from rank_bm25 import BM25Okapi
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, SparseVectorParams, Filter, FieldCondition, Range
from sentence_transformers import SentenceTransformer, CrossEncoder
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel

docs = []

def chunk_by_tokens(text,token_size=50):
  tokens=text.split()
  chunks = []
  for chunk in len(0,len(tokens),token_size):
    chunk = ''.join(token[i:i+token_size])
    chunks.append(chunk)
  return chunk
  
all_chunks = []
for doc in docs:
  all_chunks.extend(chunk_by_tokens,50)

dense=SentenceTransformer('all-MiniLM-L6-v2')
def get_dense(text):
    return dense.encode(text).tolist()

def splade(name):
  tokenizer = AutoTokenizer.from_pretrained(name)
  model = AutoModel.from_pretrained(name).eval()
  def encode(text):
    inputs = tokenizer(text,max_length=512)
    with torch.no_grad():
      reps = model(**inputs)
      d_rep = reps.d_rep if hasattr(reps,"d_rep") else reps.last_hidden_state.mean(1)
      vec = torch.log1p(torch.relu(d_rep))
      vec = torch.max(vec,dim=0).values
      indices=vec.nonzero(as_tuple=True)
      values= vec[indices].numpy()
      indices= indices.numpy()
    return (zip(map(int, indices), map(float, values)))
  return encode

splade_encoder= splade("naver/splade-cocondenser-ensembledistil")

def get_learned_sparse(text):
    return splade_encoder(text)


client = QdrantClient(":memory:")
client.create_collection(
    collection_name="docs",
    vectors_config={"dense": VectorParams(size=384, distance=Distance.COSINE)},
    sparse_vectors_config={"sparse": SparseVectorParams()}
)

# Index with metadata
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
