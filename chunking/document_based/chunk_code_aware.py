import re
docs=[]
def code_aware(text):
  chunks = [] 
  parts = re.split(r'(```[\w]*\n.*?```)', text, flags=re.DOTALL)
  for part in parts:
    if part.strip():
      if part.strip().startswith('|'):
        chunks.append({'type': 'code', 'content': part.strip()})
      else:
        chunks.append({'type': 'text', 'content': part.strip()})
return chunks

results=code_aware(docs)
