def chunk_by_sliding_window(text,window_size,overlap):
  tokens= text.split()# can tokenise in any way using the simplest here
  chunks = []
  step= window_size-overlap
  for i in range(0, len(tokens), step):
    chunk=''.join(tokens[i:i+window_size])
    chunk.append(chunk)
  return chunks
