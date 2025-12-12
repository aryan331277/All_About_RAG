import re

docs = []
def chunk_scene_events(text):
  markers = r'(The future|Applications|Types of|Introduction to)'
  chunks = re.split(markers,text)
  result = []
  for i in chunks:
    clean = i.strip()
    if clean and len(clean)>20:
      result.append(clean)
      
  return result

