import pandas as pd
# import os
from konlpy.tag import Mecab
# import re

mecab = Mecab()

def ngrams(string, num_ngram): 
#     string = re.sub(r'[,-./]|\sBD',r'', string)
    ngrams = zip(*[string[i:] for i in range(num_ngram)])
    return [''.join(ngram) for ngram in ngrams]
# print(ngrams(string))

def tagging_morphs(string):
    return mecab.morphs(string)

def tagging_nouns(string):
    return mecab.nouns(string)




