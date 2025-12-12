import re
docs =[]

def chunk_summarization_prelinked(text):
    paras=re.split(r'\n\s*\n', text.strip())
    chunks = []
    
    for p in paras:
        sentences=re.split(r'(?<=[.!?])\s+', p.strip())
        summary= sentences[0] if sentences else ""
        chunks.append({'content': p, 'summary': summary})
    
    return chunks
