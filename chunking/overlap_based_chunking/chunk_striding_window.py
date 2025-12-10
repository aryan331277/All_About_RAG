docs=[]
def chunk_striding_window(text,window_size,stride):
  tokens=text.split()
  chunks=[]
  for i in range(0,len(tokens),stride):
    chunk=''.join(tokens[i:i+window_size])
    chunk.append(chunk)
  return chunk

result=chunk_striding_window(docs,100,20)
