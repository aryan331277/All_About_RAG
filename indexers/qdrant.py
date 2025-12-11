from qdrant_client import QdrantClient
from qdrant_client.http.models import SparseVectorParams
from rank_bm25 import BM25Okapi
import re
docs=[]#your documents
def chunk_by_tokens(text,token_size):
  tokens=text.split()
  chunks= []
  for i in range(0,len(tokens), token_size):
    chunk= ' '.join(tokens[i:i + token_size])
    chunks.append(chunk)
  return chunks

all_chunks = []
for doc in docs:
    all_chunks.extend(chunk_by_tokens(doc, 50))

print(f"{len(all_chunks)} chunks ready\n")

tokenized =[chunk.lower().split() for chunk in all_chunks]
bm25 = BM25Okapi(tokenized)

def bm25(text):
    qtokens=text.lower().split()
    scores= bm25.get_scores(qtokens)
    return {i: float(s) for i, s in enumerate(scores) if s > 0}

client= QdrantClient(":memory:")
client.create_collection(
    collection_name="docs",
    sparse_vectors_config={"sparse": SparseVectorParams()}
)

for i, chunk in enumerate(all_chunks):
    client.upsert(
        collection_name="docs",
        points=[{
            "id": i,
            "vector": {"sparse": get_bm25_sparse(chunk)},
            "payload": {"text": chunk}
        }]
    )
