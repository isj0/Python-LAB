guests = ["Ronaldo", "Divith", "Messi", "Neil", "Alphonso Davies"]

print("We can unfortunately invite only 2 people.")

rem1 = guests.pop(3)
print(f"Sorry, {rem1}, we are unable to invite you for the party.")
rem2 = guests.pop(-1)
print(f"Sorry, {rem2}, we are unable to invite you for the party.")
rem3 = "Messi"
guests.remove(rem3)
print(f"Sorry, {rem3}, we are unable to invite you for the party.")
print(guests)

del guests[1]
print(guests)

del guests[0]
print(guests)