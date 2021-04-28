def make_album(singer_name, album_name, number_of_songs=None):
    if number_of_songs == None:
        album = {'singer': singer_name, 'album_name': album_name}
    else:
        album = {
            'singer': singer_name,
            'album_name': album_name,
            'number': number_of_songs
        }
    return album


album1 = make_album('Jay Chou', '七里香')
print(album1)
album2 = make_album('Jay Chou', '七里香')
print(album2)
album3 = make_album('Jay Chou', '七里香')
print(album3)
album4 = make_album('Jay Chou', '七里香', 8)
print(album4)
