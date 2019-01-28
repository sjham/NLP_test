
from difflib import SequenceMatcher

def intersect(a, b):
    inter = []
    for i in a:
        for j in b:
            inter.append(len(set(i).intersection(set(j))))
    return inter

def similar(a, b):
    t=[]
#     threshold = 0.4
    for i in a:
        for j in b:
            t.append(SequenceMatcher(None, i, j).ratio())
    return t
