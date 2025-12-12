import re
docs= []

def chunk_information_density(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    chunks =[]
    curr_chunk= []
    t_density = 0.4
    
    for sent in sentences:
        words=sent.split()
        ur=len(set(words)) / len(words) if words else 0
        
        if ur > t_density and curr_chunk:
            chunks.append(' '.join(curr_chunk))
            curr_chunk=[sent]
        else:
            curr_chunk.append(sent)
            if len(curr_chunk) >= 5:
                chunks.append(' '.join(curr_chunk))
                curr_chunk=[]
    
    if curr_chunk:
        chunks.append(' '.join(curr_chunk))
    
    return chunks
