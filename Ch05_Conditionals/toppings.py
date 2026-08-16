# requested_topping = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_topping:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_topping:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_topping:
#     print("Adding extra cheese.")

# print("\n Finished making your Pizza.")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in requested_toppings:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {topping}")

print("\nFinished making your Pizza.!")