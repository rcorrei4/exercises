def make_album(album_title, artist_name, num_tracks = ''):
    music_album = {'Title': album_title, 'Artist': artist_name}
    if num_tracks:
        music_album['Tracks'] = num_tracks
    return music_album

while True:
    print('\nEnter the Music Album, Artist and the number of tracks (optional)')
    print("(enter 'q' at any time to quit)")

    album = input('\nAlbum Name: ')
    if album == 'q':
        break
    artist = input('\nArtist Name: ')
    if artist == 'q':
        break
    numtrack = input('\nNumber of Tracks (enter "0" if you dont want to): ')
    if numtrack == 'q':
        break
    
    if numtrack == '0':
        formatted_album = make_album(album, artist)
        print(formatted_album)
    else:
        formatted_album = make_album(album, artist, numtrack)
        print(formatted_album)
