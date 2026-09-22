from pathlib import Path

guests = []
guest = input("Please enter your name: ")
guests.append(guest)

path = Path('guest.txt')
path.write_text(guest)