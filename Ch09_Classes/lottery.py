from random import randint
from random import choice

# class Lottery:
#     """Simple Lottery Model."""

#     def __init__(self, numbers, letters, set):
#         self.numbers = numbers
#         self.letters = letters
#         self.set = set

#     def select_set(self):
#         self.letters = ['a', 'e', 'i', 'o', 'u']
#         self.numbers = []
#         self.set = []

#         for i in range(10):
#             self.numbers.append(randint(0, 9))

#         self.set.append(self.letters)
#         self.set.append(self.numbers)

#     def select_winner(self):
#         winner = []
#         for i in range(5):
#             select = choice(self.set)
#             winner.append(select)

letters = ['a', 'e', 'i', 'o', 'u']
set = []

for i in range(10):
    set.append(randint(0, 9))

for c in letters:
    set.append(c)


my_ticket = [9, 'a', 6]
count = 0

while True:
    winner = []
    for i in range(3):
        w = choice(set)
        winner.append(w)

    count += 1

    if my_ticket == winner:
        print(f"You won ! after {count} tries.")
        break
    elif count == 1000:
        print(f"You have tried {count} times.")
        break

