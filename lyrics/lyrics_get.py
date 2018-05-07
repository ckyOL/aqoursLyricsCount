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

def get_musicid(play_list_url):
    '''
    Get music ID
    :param playListUrl:
    :return: musicID list
    '''
    s = requests.session()
    s = BeautifulSoup(s.get(play_list_url, headers=headers).content, "lxml")
    main = s.find('ul', {'class': 'f-hide'})
    music_info = main.find_all('a')

    music_list = {}

    for music in music_info:
        music_text = music.text
        music_id = music['href'].split('=')
        music_list[music_text] = music_id[1]
        #print('{} : {}'.format(musicText, musicID[1]))

    return music_list

def get_lyrics(music_id):
    '''
    Get lyrics
    :param musicID:
    :return: lyric string
    '''
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(music_id) + '&lv=1&kv=1&tv=-1'
    lyric = requests.get(lrc_url)
    json_obj = lyric.text
    j = json.loads(json_obj)
    lrc = j['lrc']['lyric']
    pat = re.compile(r'\[.*\]')
    lrc = re.sub(pat, "", lrc)
    lrc = lrc.strip()
    #print(lrc)
    return lrc