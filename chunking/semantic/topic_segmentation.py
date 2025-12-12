import re
docs = []
def chunk_topic_segmentation(text):
    paragraphs = re.split(r'\n\s*\n', text.strip())
    chunks=[]
    current_chunk=[]
    current_keywords=set()
    
    for para in paragraphs:
        words = set(re.findall(r'\b[a-z]{4,}\b',para.lower()))
        if not current_keywords or len(current_keywords & words) > 2:
            current_chunk.append(para)
            current_keywords.update(words)
        else:
            if current_chunk:
                chunks.append('\n\n'.join(current_chunk))
            current_chunk=[para]
            current_keywords=words
    
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks
