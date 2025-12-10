import re
def chunk_by_words(text,token_size):
  words=text.split()
  chunks= []
  for i in range(0,len(words), token_size):
    chunk= ' '.join(words[i:i + token_size])
    chunks.append(chunk)

#calling the function
result = chunk_by_words(docs,50)
print(result)
