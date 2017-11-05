import requests
import json
import re
from bs4 import BeautifulSoup

headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

def getMusicID(playListUrl):
    '''
    Get music ID
    :param playListUrl:
    :return: musicID list
    '''
    s = requests.session()
    s = BeautifulSoup(s.get(playListUrl, headers=headers).content, "lxml")
    main = s.find('ul', {'class': 'f-hide'})
    musicInfo = main.find_all('a')

    musicList = {}

    for music in musicInfo:
        musicText = music.text
        musicID = music['href'].split('=')
        musicList[musicText] = musicID[1]
        #print('{} : {}'.format(musicText, musicID[1]))

    return musicList

def getLyrics(musicID):
    '''
    Get lyrics
    :param musicID:
    :return: lyric string
    '''
    lrcUrl = 'http://music.163.com/api/song/lyric?' + 'id=' + str(musicID) + '&lv=1&kv=1&tv=-1'
    lyric = requests.get(lrcUrl)
    jsonObj = lyric.text
    j = json.loads(jsonObj)
    lrc = j['lrc']['lyric']
    pat = re.compile(r'\[.*\]')
    lrc = re.sub(pat, "", lrc)
    lrc = lrc.strip()
    #print(lrc)
    return lrc