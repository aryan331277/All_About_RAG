import re
docs=[]#define your documents here
def chunk_by_sentences(text,sentence_count=3):
  sentences = re.split(r'(?<=[.!?])\s+', text.strip())
  chunks= []
  for i in range(0,len(sentence), sentence_count):
    chunk= ' '.join(sentence[i:i + sentence_count])
    chunks.append(chunk)

result = chunk_by_sentences(docs,50)
print(result)
