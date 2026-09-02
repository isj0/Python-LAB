def make_album(artist_name, album_title, genre = None):
    """Return a dictionary containing album information."""
    album = {'artist': artist_name, 'title': album_title}
    if genre:
        album['genre'] = genre
    return album

album1 = make_album('black sabbath', 'iron man')
album2 = make_album('pink floyd', 'comfortably numb', 'rock')
album3 = make_album('the rolling stones', 'Sympathy for the Devil', 'Rock')
print(album1)
print(album2)
print(album3)
