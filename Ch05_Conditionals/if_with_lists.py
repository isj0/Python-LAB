requested_toppings = []

# Returns true if the list contains atleast one item
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}")
    print("\nFinished making your Pizza!")
else:
    print("Are you sure you want a plain Pizza?")