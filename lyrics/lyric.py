from lyrics import lyrics_get as lyric

play_list_url = 'http://music.163.com/playlist?id=430139321'
save_local = ''
music = lyric.get_musicid(play_list_url)
#print(music.keys())

for musicid in music.keys():
    lrc = lyric.get_lyrics(music[musicid])
    file = open(save_local + str(musicid) + '.txt', "ab")
    file.write(lrc.encode('utf-8'))
    file.close()
