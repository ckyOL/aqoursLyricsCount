import pandas as pd
import os

countLocal = ''
allFile = os.listdir(countLocal)

allData = pd.DataFrame({'word':[], 'count':[]})

for file in allFile:
    print(file)
    word = pd.read_table(countLocal + file, encoding='utf-8', sep=',')
    data = pd.DataFrame(word, columns=['word', 'count'])

    allData = pd.merge(allData, data, on='word', how='outer')

print(allData)

allData.to_csv(countLocal + 'all.csv')

