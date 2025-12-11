from rank_bm25 import BM25Okapi
import pinecone

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



pinecone.init(api_key="your-key")
index = pinecone.Index("docs")

vectors=[]
for i, chunk in enumerate(all_chunks):
    sparse=get_bm25_sparse(chunk)
    vectors.append({
        "id": str(i),
        "values": [],  # No dense
        "sparse_values": {
            "indices": list(sparse.keys()),
            "values": list(sparse.values())
        },
        "metadata": {"text": chunk}
    })
index.upsert(vectors)
