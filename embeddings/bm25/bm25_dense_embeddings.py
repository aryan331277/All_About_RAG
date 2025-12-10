from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize#tokeniser
import re

chunks=[#define chunk here]
tokenized=[word_tokenize(chunk.lower()) for chunk in chunks]#tokenised chunk

model=SentenceTransformer("all-MiniLM-L6-v2")
chunk_embeds=model.encode(chunks,normalize_embeddings=True)

query = ""  # define query
query_tokenized=word_tokenize(query.lower())

bm25_scores=np.array(bm25.get_scores(query_tokenized))

query_embed=model.encode([query], normalize_embeddings=True)[0]
dense_scores=chunk_embeds @ query_embed


alpha=0.5  
if bm25_scores.max()>0:
    bm25_norm=bm25_scores/bm25_scores.max()
else:
    bm25_norm=bm25_scores

hybrid_scores=alpha * bm25_norm +(1 - alpha) * dense_scores


sorted_chunks = sorted(zip(hybrid_scores,chunks),key=lambda x: -x[0])

for rank,(score,chunk) in enumerate(sorted_chunks,start=1):
  print(f"Rnak: {rank} (score={score:.4f}): {chunk}")




