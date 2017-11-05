import matplotlib
import matplotlib.pyplot as pl
import pandas as pd
import os

matplotlib.rcParams['font.sans-serif'] = ['Kozuka Gothic Pro', 'sans-serif']
matplotlib.rcParams.update({'font.size':5})

countLocal = ''
pngLocal = ''
allFile = os.listdir(countLocal)

for file in allFile:
    print(file)
    fileName = file.split('.')
    word = pd.read_table(countLocal + file, encoding='utf-8', sep=',')

    data = pd.DataFrame(word, columns=['word', 'count'])
    data = data.sort_values(by=['count'], ascending=False)
    data.reset_index(drop=True, inplace=True)
    #print(data['word'])

    plot = data.plot(kind='bar', title=fileName[0])
    plot.set_xticklabels(data.word, rotation=80)
    plot.set_xlim(-1, 50)
    plot.legend_.remove()

    pl.savefig(pngLocal + fileName[0] + ".png", dpi=300)
    #pl.show()

