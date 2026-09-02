def build_person(first_name, last_name, age = None):
    """Return a dictionary of informatino about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

artist = build_person('jimi', 'hendrix', age = 27)
print(artist)