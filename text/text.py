import os
import codecs
from text import text_seg as ts

lyric_local = ''
count_local = ''
all_file = os.listdir(lyric_local)

for lyric in all_file:
    #print(lyricOne)
    file = codecs.open(lyric_local + lyric, 'r', 'utf-8')
    lrc = file.readlines()

    string = ""

    # combine lyric to a sentence
    for line in lrc:
        string += line

    word_list = ts.extract_word(string)
    map = ts.count(word_list)
    write_data = ts.map2str(map)

    file.close()

    # write count data to file
    count_file = open(count_local + lyric, 'wb')
    count_file.write(write_data.encode('utf-8'))

    count_file.close()