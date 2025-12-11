import torch
from transformers import AutoTokenizer, AutoModel
#assuming all in GPU, so not explicitly specifying it 
def coil(name,wt_exp):
  tokenizer = AutoTokenizer.from_pretrained(model)
  model = AutoModel.from_pretrained(model).eval()
