from rank_bm25 import BM25Okapi
from opensearchpy import OpenSearch, helpers


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

os = OpenSearch(["http://localhost:9200"])
os.indices.create(
    index="docs",
    body={
        "mappings": {
            "properties": {
                "text": {"type": "text"},
                "sparse": {"type": "rank_features"}
            }
        }
    },
    ignore=400
)

actions = []
for i, chunk in enumerate(all_chunks):
    actions.append({
        "_index": "docs",
        "_id": i,
        "_source": {
            "text": chunk,
            "sparse": get_bm25_sparse(chunk)
        }
    })
helpers.bulk(os, actions)
