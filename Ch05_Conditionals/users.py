users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user.title()}, would like to see the status report")
        else:
            print(f"Hello {user.title()}, thank you logging in again.")
else:
    print("We need to find some users.")