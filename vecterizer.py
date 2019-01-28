
import numpy as np

def vecterize_to_cols(data1.clo_tagged, data2.col_tagged):
    vect = np.array(similar(data1.clo_tagged, data2.col_tagged)).reshape(len(data1.shape),len(data2.shape))
    arg_count = np.argmax(vect, axis=1)
    max_count = np.max(vect, axis=1)
    data1['arg_count']=pd.Series(arg_count)
    data1['max_count']=pd.Series(max_count)
    return
