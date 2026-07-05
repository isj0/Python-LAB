motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

# append method -> adds a new element to the end of the list
# motorcycles.append('ducati')
# print(motorcycles)

# insert method -> add a new element at a specified position
# this operation shifts every other value in the list one 
# position to the right
# motorcycles.insert(1, 'ducati')
# print(motorcycles)

# del -> remove the item from list, if you know its index
# del motorcycles[0]
# print(motorcycles)

# pop -> remove item from any position using index
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycles I owned was a {first_owned.title()}.")

# remove -> if you know the value of the item you want to remove
# motorcycles = ['honda', 'yamaha', 'ducati', 'suzuki']
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")