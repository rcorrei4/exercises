def make_album(album_title, artist_name, num_tracks = ''):
    music_album = {'Title': album_title, 'Artist': artist_name}
    if num_tracks:
        music_album['Tracks'] = num_tracks
    return music_album

forro = make_album('Calcinha', 'Calcinha Preta')
print(forro)

funk = make_album('Vida Loka', 'Mc Doido', num_tracks= 20)
print(funk)


