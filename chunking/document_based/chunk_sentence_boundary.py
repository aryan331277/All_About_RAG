import re
docs = []
def sentence_boundary(text):
  raw_sentences = re.split(r'(?<=[.!?])\s+', cleaned_text)
  sentences = [sentence.strip() for sentence in raw_sentences if sentence.strip()]
  
result=sentence_boundary(docs)
