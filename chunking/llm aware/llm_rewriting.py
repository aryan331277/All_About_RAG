import re
docs= []

def chunk_llm_rewriting(text,target= 100):
    paras=re.split(r'\n\s*\n', text.strip())
    chunks= []
    for para in paras:
        words =para.split()
        if len(words) > target:
            chunks.append(' '.join(words[:target]))
        else:
            chunks.append(para)
    return chunks
