import re
docs=[]#your documents
def chunk_by_tokens(text,token_size):
  tokens=text.split()
  chunks= []
  for i in range(0,len(tokens), token_size):
    chunk= ' '.join(tokens[i:i + token_size])
    chunks.append(chunk)
  return chunks

#calling the function
result = chunk_by_tokens(docs,50)
print(result)
