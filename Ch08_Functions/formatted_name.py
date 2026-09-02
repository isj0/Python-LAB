# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name}, {middle_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('michael', 'lee', 'jackson')
# print(musician)

def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

artist = get_formatted_name('jimi', 'hendrix')
print(artist)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)