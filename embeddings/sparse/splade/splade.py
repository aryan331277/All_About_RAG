import torch
from transformers import AutoTokenizer, AutoModel

def splade(name):
  tokenizer = AutoTokenizer.from_pretrained(name)
  model = AutoModel.from_pretrained(name).eval()
  def encode(text):
    inputs = tokenizer(text,max_length=512)
    with torch.no_grad():
      reps = model(**inputs)
      d_rep = reps.d_rep if hasattr(reps,"d_rep") else reps.last_hidden_state.mean(1)
      vec = torch.max(vec,dim=0)



splade_ensemble = splade("naver/splade-cocondenser-ensembledistil")      # SPLADE-Ensemble Distil
splade_pp = get_splade("naver/splade-v3")                           # Splade++
distil_splade = get_splade("naver/splade-v3-distil")                # Distil-Splade
