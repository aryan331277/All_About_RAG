import re

docs=[]

def chunk_query_aware(text,exp_query):    
    sentences=re.split(r'(?<=[.!?])\s+',text.strip())
    chunks=[]
    curr_chunk=[]
    
    for sent in sentences:
        sent_lower = sent.lower()
        rel=any(q.lower() in sent_lower for q in exp_query)
        
        if rel and curr_chunk:
            chunks.append(' '.join(curr_chunk))
            curr_chunk = [sent]
        else:
            curr_chunk.append(sent)
    
    if curr_chunk:
        chunks.append(' '.join(curr_chunk))
    
    return chunks
