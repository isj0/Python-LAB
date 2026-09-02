def make_album(artist_name, album_title, songs = None):
    """Return a dictionary containing album information."""
    album = {'artist': artist_name, 'title': album_title}
    if songs:
        album['songs'] = songs
    return album

# Enter album information
while True:
    print("\nPlease enter album details:")
    print("(enter 'q' at any time to quit...)")
    name = input("Enter artist name: ")
    if name == 'q':
        break

    title = input("Enter album title: ")
    if title == 'q':
        break

    album = make_album(name, title)

    print(f"\nWe have {album}")