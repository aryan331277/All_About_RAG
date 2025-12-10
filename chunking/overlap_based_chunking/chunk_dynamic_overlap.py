import re
docs = []
def chunk_dynamic_overlap(text,size):
  sentences= re.split(r'(?<=[.!?])\s+', text.strip())
  chunks = []
  i=0
  while i < len(sentences):
    if len(sentences[i].split())>15:
      overlap_size=1
    else:
      overlap_size=2
    end_idx= min(i+3,len(sentences))
    chunk = ''.join(sentences[i:end_idx])
    chunk.append(chunk)
    i = i+(3-overlap_size)
  return chunks

result=chunk_dynamic_overlap(docs,100)
