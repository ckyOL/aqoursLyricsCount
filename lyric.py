import lyricsGet as lyric

playListUrl = 'http://music.163.com/playlist?id=430139321'
saveLocal = ''
music = lyric.getMusicID(playListUrl)
#print(music.keys())

for musicid in music.keys():
    lrc = lyric.getLyrics(music[musicid])
    file = open(saveLocal + str(musicid) + '.txt', "ab")
    file.write(lrc.encode('utf-8'))
    file.close()
