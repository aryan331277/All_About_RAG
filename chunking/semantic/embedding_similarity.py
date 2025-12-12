import re
docs = []

def embedding_similarity(text,threshold):
  sentences=re.split(r'(?<=[.!?])\s+', text.strip())
  chunks = []
  current_chunk = [sentences[0]] if sentences else []
  for i in range(1,len(sentences)):
    prev_words = set(current_chunk[-1].lower().split())
    curr_words = set(sentences[i].lower().split())
    similarity = (len(prev_words & curr_words) / len(prev_words | curr_words)
    if prev_words or curr_words
    else 1.0)
    if threshold>similarity:
      chunks.append(' '.join(current_chunk))
      current_chunk=[sentences[i]]
    else:
      current_chunk.append(sentences[i])
  if current_chunk:
    chunks.append(' '.join(current_chunk))
  return chunks
