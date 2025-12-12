import re
docs = []

def chunk_dialogue_turns(text):
    sentences=re.split(r'(?<=[.!?])\s+',text.strip())
    chunks=[]
    for i, sent in enumerate(sentences):
        if '?' in sent or i % 2 == 0:  # Simplified Q/A detection
            chunks.append(sent)
    return chunks
