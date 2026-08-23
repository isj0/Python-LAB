pizza = []

prompt = "\nWhat toppings would you like on your pizza: "

toppings = ""
active = True

while active:
    toppings = input(prompt)

    if toppings == 'quit':
        active = False
    else:
        pizza.append(toppings)
        print(f"\n{toppings} is being added to your Pizza.")

print(f"\nHere is your Pizza with")
print(pizza)
    