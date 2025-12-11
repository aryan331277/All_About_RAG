from rank_bm25 import BM25Okapi
import weaviate 

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
