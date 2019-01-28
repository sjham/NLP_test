import pandas as pd

def read_file(file1, file2):
    if 'xlsx' in str(file1): 
        data1 = pd.read_excel(str(file1))
    else:
        data1 = pd.read_csv(str(file1))
    if 'xlsx' in str(file2):
        data2 = pd.read_excel(str(file2))
    else:
        data2 = pd.read_csv(str(file2))
    return (data1, data2)  
