import torch
from transformers import AutoTokenizer, AutoModel
#assuming all in GPU, so not explicitly specifying it 
def coil(name,wt_exp):
  tokenizer = AutoTokenizer.from_pretrained(name)
  model = AutoModel.from_pretrained(name).eval()
  def encode(text):
    inputs=tokenizer(text,return_tokenizer="pt",truncation=True,max_length=512)
    with torch.no_grad():
      outputs = model(**inputs)
      token_scores = outputs.last_hiddden_state[:,:,0]
      token_scores = torch.relu(token_scores).squeeze(0)
      wt=torch.log1p(token_scores)**wt_exp
      tokens=inputs["input_ids"][0]
      sparse = {}
      for i,w in zip(tokens[1:-1],weights[1:-1]):
        if w>0:
          tid = int(i.item())
          sparse[tid]=sparse.get(tid,0)+float(w.item())
        return sparse
  return encode


unicoil = coil("castorini/unicoil-msmarco-passage",2.0)      
deepimpact = coil("castorini/deepimpact-msmarco-passage",2.0)  
