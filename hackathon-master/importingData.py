import csv
import embed as e
import torch
def read_products(path: str):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        products = list(reader)    
    return(products)

def prepareVectore(l):
    text_to_embed = " ".join([l[2], l[5]])  
    v = e.txtVector(text_to_embed)
    v = v / v.norm(dim=1, keepdim=True)
    v = v.squeeze(0)
    v_list = v.tolist()

    return (v)

