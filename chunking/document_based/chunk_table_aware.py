import re
docs=[]
def table_aware(text):
  parts = re.split(r'(\|.+\|[\s\S]+?\n\n)', text)
  for part in parts:
    if part.strip():
      if part.strip().startswith('|'):
        chunks.append({'type': 'table', 'content': part.strip()})
      else:
        chunks.append({'type': 'text', 'content': part.strip()})
return chunks

results=table_aware(docs)
