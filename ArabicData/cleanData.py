# import csv
# file= 'jamalon datasetclean.csv'
# def row_factory(row):
#     return [x if x != '' else 'NaN' for x in row]
#
#
# with open('jamalon datasetclean.csv', 'r', newline='') as f:
#     reader = csv.reader(f, delimiter=';',in)

#     for row in reader:
#         print(row_factory(row))

import pandas as pd

df = pd.read_csv('jamalon datasetclean.csv', header=0,
                 names=['Author'])


# print (df)
# for row in df:
#     for x in row:
#         print (x)
# df.to_csv('nameData.csv')

def conversion(text):

    if (
              ( ' لا يوجد' in text) or ( 'لايوجد' in text)or ( 'مركز التدبر للإستشارات التربوية والتعليمية' in text) or ( 'مجموعة مؤلفين' in text) or ( 'لجنة التأليف التربوي' in text) or ( 'مجموعة باحثين' in text)):
        return "1"
    else:
        return "- [{}](name)".format(text)

df.drop_duplicates(subset=['Author'])
# df['index'] = df['index'].map(conversion)
# print(df)
df.to_csv('nameDatawithoutduplicate.csv')
