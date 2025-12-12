import re
docs = [] 

def chunk_llm_guided(text,ts):
    sentences=re.split(r'(?<=[.!?])\s+', text.strip())
    chunks=[]
    curr=[]
    curr_len = 0
    
    for sent in sentences:
        sent_len=len(sent.split())
        if curr_len+sent_len > ts and curr:
            chunks.append(' '.join(curr))
            curr = [sent]
            curr_len =sent_len
        else:
            curr.append(sent)
            curr_len=curr_len+ sent_len
    
    if curr:
        chunks.append(' '.join(curr))
    
    return chunks
