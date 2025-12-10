from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

chunks=[#documents here]

model=SentenceTransformer('all-MiniLM-L6-v2')

embeddings=model.encode(chunks)

dim=embeddings.shape[1]#dimensions of embeddings
index =faiss.IndexFlatIP(dim)#cosine sim
faiss.normalize_L2(embeddings) #normalize for cosine similarity
index.add(embeddings) #add embeddings to the index

query = ""#define query

qembedding=model.encode([query])
faiss.normalize_L2(qembedding)  

distances, indices =index.search(qembedding,3)#search for faiss index here 3 top results would be retrieved as k=3

# Print results
print(f"Query: {query}\n")
for i, (distance, idx) in enumerate(zip(distances[0], indices[0]), start=1):
    print(f"Rank {i} (similarity={distance:.4f}): {chunks[idx]}")
