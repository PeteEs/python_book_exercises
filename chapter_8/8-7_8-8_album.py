def make_album(artist,title):
    album = {'Artist' : artist.title(), 'Title' : title.title()}
    return album

dict_1 = make_album("John","3 pots")

dict_2 = make_album("Ann","Heaven")

dict_3 = make_album("Ross","Tomatoe")

album_list = [dict_1,dict_2,dict_3]

print(album_list)

for one in album_list:
    for x,y in one.items():
        print(x,y)


def make_album(artist,title,songs = None):
    album = {'Artist' : artist.title(), 'Title' : title.title()}
    if songs:
        album['Songs'] = songs
    return album

dict_4 = make_album("John","3 pots",9)

print(dict_4)

# -----------------------------------

def make_album(artist,title):
    album = {'Artist' : artist.title(), 'Title' : title.title()}
    return album

while True:
    print("\nPlease enter album info:")
    print("(enter 'q' at any time to quit)")

    w_artist = input("Artist name: ")
    if w_artist == 'q':
        break

    w_title = input("Album's title: ")
    if w_title == 'q':
        break

    album = {w_artist.title(),w_title.title()}
    print(album)