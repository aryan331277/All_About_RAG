from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize#tokeniser
import re

docs=[#define document here]
tokenized=[word_tokenize(doc.lower()) for doc in docs]#tokenised documents

bm25=BM25OKapi(tokenized)

query=""#define the query here
query_tokenized=word_tokenize(query.lower())
scores=bm25.get_scores(query_tokenized)

sorted_docs=sorted(zip(scores,docs),key=lambda x: -x[0])

for rank,(score,doc) in enumerate(sorted_docs,start=1):
  print(f"Rnak: {rank} (score={score:.4f}): {doc}")
