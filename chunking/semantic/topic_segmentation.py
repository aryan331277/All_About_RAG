import re
docs = []
def chunk_topic_segmentation(text):
    paragraphs=re.split(r'\n\s*\n', text.strip())
    chunks=[]
    current_chunk=[]
    current_keywords=set()
    
