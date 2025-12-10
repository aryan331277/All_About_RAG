def chunk_by_characters(text,char_length= 200):
    chunks = []
    for i in range(0, len(text), char_length):
        chunks.append(text[i:i + char_length])
    return chunks
