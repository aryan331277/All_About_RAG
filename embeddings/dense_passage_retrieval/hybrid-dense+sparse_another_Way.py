from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
import numpy as np

dense=SentenceTransformer("all-MiniLM-L6-v2")

docs = []

tokenized =[word_tokenize(chunk.lower()) for chunk in chunks]
bm25 = BM25Okapi(tokenized)

query = ""

dense_q = dense.encode(query)
dense_d = dense.encode(docs)

bm25_scores = bm25.get_scores(query.lower().split())
dense_scores = dense_q @ dense_d.T

hybrid_scores = 0.5 * dense_scores + 0.5 * bm25_scores
print(hybrid_scores)
