import MeCab
from collections import Counter

def extractWord(text):
    '''
    Extract word
    :param text: sentence
    :return: word list
    '''
    tagger = MeCab.Tagger('-Ochasen')
    node = tagger.parseToNode(text)
    wordList = []
    while node:
        if node.feature.split(",")[0] in ("名詞", "動詞", "形容詞"):
            wordList.append(node.surface)
        node = node.next
    return wordList

def count(wordList):
    '''
    count word appear number
    :param wordList:
    :return: map('word':'count')
    '''
    count = Counter(wordList)
    return count

def map2Str(map):
    '''
    trans map to str
    :param map:
    :return: string
    '''
    string = ""
    for key, value in map.items():
        text = str(key) + "," + str(value)
        string = string + text + '\n'

    return string