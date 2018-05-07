import pandas as pd
import os

count_local = ''
all_file = os.listdir(count_local)

all_data = pd.DataFrame({'word':[], 'count':[]})

for file in all_file:
    print(file)
    word = pd.read_table(count_local + file, encoding='utf-8', sep=',')
    data = pd.DataFrame(word, columns=['word', 'count'])

    all_data = pd.merge(all_data, data, on='word', how='outer')

print(all_data)

all_data.to_csv(count_local + 'all.csv')

