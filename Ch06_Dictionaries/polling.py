favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

take_poll = ['hulk', 'sarah', 'spidey', 'phil', 'edward', 'jen', 'wolverine']

for name in take_poll:

    if name in favorite_languages.keys():
        print(f"\nThank you, {name.title()} for taking the poll.")
    else:
        print(f"\nHello, {name.title()}! please take the poll ASAP.")
