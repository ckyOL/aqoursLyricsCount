import matplotlib
import matplotlib.pyplot as pl
import pandas as pd
import os

matplotlib.rcParams['font.sans-serif'] = ['Kozuka Gothic Pro', 'sans-serif']
matplotlib.rcParams.update({'font.size':5})

countLocal = ''
pngLocal = ''
allFile = os.listdir(countLocal)

total = pd.read_table(countLocal + 'all.csv', encoding='utf-8', sep=',')
data = pd.DataFrame(total, columns=['word', 'total'])
data = data.sort_values(by=['total'], ascending=False)
data.reset_index(drop=True, inplace=True)
#print(data)

#data.to_csv(countLocal + 'total.csv')

plot = data.plot(kind='bar', title=u'Aqours歌詞単語頻度分布')
plot.set_xticklabels(data.word, rotation=80)
plot.set_xlim(4.5,55)
plot.legend_.remove()

pl.savefig(pngLocal + "Aqours歌詞単語頻度分布.png", dpi=300)
pl.show()

