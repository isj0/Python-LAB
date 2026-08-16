users = []

users = ['tom', 'jerry', 'admin', 'sunny', 'nimi']

for user in users:
    if user == 'admin':
        print(f"Hello {user}, would like yo see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")