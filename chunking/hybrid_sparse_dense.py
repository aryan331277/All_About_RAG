import re
docs = []

def chunk_hybrid_sparse_dense(text: str) -> Dict[str, List[str]]:
    lex = []
    paras = re.split(r'\n\s*\n', text.strip())
    for para in paras:
        if re.search(r'\b(machine learning|algorithm|neural)\b', para, re.I):
            lex.append(para)
        semantic = chunk_embedding_similarity(text, threshold=0.5)
    
    return {
        'lex': lex,
        'semantic': semantic
    }
