
import pandas as pd

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
