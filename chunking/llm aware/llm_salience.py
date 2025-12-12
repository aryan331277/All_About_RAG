import re
docs= []

def chunk_llm_salience(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    important_words = {'machine learning', 'deep learning', 'neural', 'algorithm'}
    chunks=[]
    curr_chunk=[]
    
    for sent in sentences:
        sent_lower=sent.lower()
        imp =any(word in sent_lower for word in important_words)
        
        if imp and curr_chunk:
            chunks.append(' '.join(curr_chunk))
            curr_chunk = [sent]
        else:
            curr_chunk.append(sent)
    
    if curr_chunk:
        chunks.append(' '.join(curr_chunk))
    
    return chunks
