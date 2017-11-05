import os
import codecs
import textSeg as ts

lyricLocal = ''
countLocal = ''
allFile = os.listdir(lyricLocal)

for lyricOne in allFile:
    #print(lyricOne)
    file = codecs.open(lyricLocal + lyricOne, 'r', 'utf-8')
    lrc = file.readlines()

    string = ""

    # combine lyric to a sentence
    for line in lrc:
        string += line

    wordList = ts.extractWord(string)
    map = ts.count(wordList)
    writeData = ts.map2Str(map)

    file.close()

    countFile = open(countLocal + lyricOne, 'wb')
    countFile.write(writeData.encode('utf-8'))

    countFile.close()