import re
docs = []
def paragraph_boundary(text):
  raw_paragraphs = re.split(r'\n\s*\n', text.strip())
  paragraphs = [paragraph.strip() for paragraph in raw_paragraphs if paragraph.strip()]
  
result=paragraph_boundary(docs)
