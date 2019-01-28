
import pandas as pd

def save_to_file(data1, file_name):
    pd.to_pickle(data1, file_name+'.pkl')
    data['verify'] = 0
    file_name = data[['제목', 'matching_title', 'verify','max_count', 'matching_aT']]
    file_name.to_csv(file_name+'.csv')
