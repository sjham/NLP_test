import re
def cleaning_data(data1, data2):
    data1['title_refined'] = data1.제목.str.replace(r'[/W\”\“\‘\,\’\"\'\.\∙\…\[\]\(\)]+', " ")
    data2['title_refined'] = data2.title.str.replace(r'[/W\”\“\‘\,\’\"\'\.\∙\…\[\]\(\)]+', " ")
    data1['title_refined'] = data1['title_refined'].str.strip()
    data2['title_refined'] = data2['title_refined'].str.strip()
    return



# data = data.dropna(subset=['제목'],axis=0, how='any')
