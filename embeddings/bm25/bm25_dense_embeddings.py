from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize#tokeniser
import re

docs=[#define document here]
tokenized=[word_tokenize(doc.lower()) for doc in docs]#tokenised documents

model=SentenceTransformer("all-MiniLM-L6-v2")
doc_embeds=model.encode(docs,normalize_embeddings=True)

query = ""  # define query
query_tokenized=word_tokenize(query.lower())

bm25_scores=np.array(bm25.get_scores(query_tokenized))

query_embed=model.encode([query], normalize_embeddings=True)[0]
dense_scores=doc_embeds @ query_embed


alpha=0.5  
if bm25_scores.max()>0:
    bm25_norm=bm25_scores/bm25_scores.max()
else:
    bm25_norm=bm25_scores

hybrid_scores=alpha * bm25_norm +(1 - alpha) * dense_scores


sorted_docs = sorted(zip(hybrid_scores,docs),key=lambda x: -x[0])

for rank,(score,doc) in enumerate(sorted_docs,start=1):
  print(f"Rnak: {rank} (score={score:.4f}): {doc}")




