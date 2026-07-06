# Places i would like to visit
places = ["Rome", "Banff", "Maldives", "Antartica","Santorini"]

print("Here is a list of places I would like to visit:")
print(places)

# Sorted list without modifying the original list
print("Here is a list of places I would like to visit:")
print(places)
print("\nSorted list:")
print(sorted(places))
print("\nAgain the list of places I would like to visit:")
print(places)

# Print Sorted list in reverse order, without modifying original
print("\nSorted list in reverse order:")
print(sorted(places, reverse = True))
print("\nAgain the list of places I would like to visit:")
print(places)

# Print the list in revers order
places.reverse()
print("\nPlaces reverse order")
print(places)

# Now reversing to change the order back to original
places.reverse()
print("\nNow reversed the list to original order:")
print(places)

# Sort and print the list in alphabetical order
places.sort()
print("\nPlaces in alphabetical order:")
print(places)

# Sort and print the list in reversed-alphabetical order
places.sort(reverse=True)
print("\nPlaces listed in reversed alphabetical order:")
print(places)