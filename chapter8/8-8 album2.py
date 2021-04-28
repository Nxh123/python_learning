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


while True:

    print('\nPlease input some information about the album')

    print('(Enter "q" to quit)')

    singer = input('Please input the singer name: ')

    if singer == 'q':

        break

    album_name = input('Please input the album name: ')

    if album_name == 'q':

        break
    print(make_album(singer, album_name))
