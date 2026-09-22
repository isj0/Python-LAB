from pathlib import Path

guests = ''

path = Path('guest_book.txt')

for i in range(5):
    guest = input("Enter your name: ")
    guests += guest + '\n'

path.write_text(guests)

