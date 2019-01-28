
import pandas as pd
import numpy as np
# import os
from konlpy.tag import Mecab
import re
from difflib import SequenceMatcher
mecab = Mecab()


#reading file

def read_file(file1, file2):
    if 'xlsx' in str(file1): 
        data1 = pd.read_excel(str(file1))
    else:
        data1 = pd.read_csv(str(file1))
    if 'xlsx' in str(file2):
        data2 = pd.read_excel(str(file2))
    else:
        data2 = pd.read_csv(str(file2))
    return data1, data2


#cleaning data

def cleaning_data(data1, data2):
    data1['title_refined'] = data1.제목.str.replace(r'[/W\”\“\‘\,\’\"\'\.\∙\…\[\]\(\)]+', " ")
    data2['title_refined'] = data2.title.str.replace(r'[/W\”\“\‘\,\’\"\'\.\∙\…\[\]\(\)]+', " ")
    data1['title_refined'] = data1['title_refined'].str.strip()
    data2['title_refined'] = data2['title_refined'].str.strip()
    return (data1, data2)


#tokenizing

def ngrams(string, num_ngram): 
#     string = re.sub(r'[,-./]|\sBD',r'', string)
    ngrams = zip(*[string[i:] for i in range(num_ngram)])
    return [''.join(ngram) for ngram in ngrams]
# print(ngrams(string))

def tagging_morphs(string):
    return mecab.morphs(string)

def tagging_nouns(string):
    return mecab.nouns(string)



# finding matching data

def intersect(data1, data2):
    inter = []
    for i in data1:
        for j in data2:
            inter.append(len(set(i).intersection(set(j))))
    return inter

def similar(data1, data2):
    sim=[]
#     threshold = 0.4
    for i in data1:
        for j in data2:
            t.append(SequenceMatcher(None, i, j).ratio())
    return sim


#vecterize and send to columns

def vecterize_to_cols(data1_col_tagged, data2_col_tagged):
    vect = np.array(similar(data1_col_tagged, data2_col_tagged)).reshape(len(data1.shape),len(data2.shape))
    arg_count = np.argmax(vect, axis=1)
    max_count = np.max(vect, axis=1)
    data1['arg_count']=pd.Series(arg_count)
    data1['max_count']=pd.Series(max_count)
    return


#matched data to columns

def match_to_cols(data1, data2):
    matching_title= []
    matching_aT = []
    t = int(data2.columns.get_loc('title'))
    aT = int(data2.columns.get_loc('articleText')) 
    for i in data1.arg_count:
        matching_title.append(data2.iloc[i,t])
        matching_aT.append(data2.iloc[i,aT])
    data1['matching_title'] = matching_title
    data1['matching_aT'] = matching_aT
    return


#save to file

def save_to_file(data1, file_name):
    pd.to_pickle(data1, file_name+'.pkl')
    data['verify'] = 0
    file_name = data[['제목', 'matching_title', 'verify','max_count', 'matching_aT']]
    file_name.to_csv(file_name+'.csv')


