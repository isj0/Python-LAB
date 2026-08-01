pizzas = ["Cheese", "Veggie", "Tandori"]
friends_pizza = pizzas[:]

print("My favorite Pizzas are: ")
for my in pizzas:
    print(my)

print("\nMy friends favorite Pizzas are: ")
for your in friends_pizza:
    print(your)

pizzas.append("Paneer")
friends_pizza.append("Chicken")

print("\nMy favorite Pizzas are: ")
for my in pizzas:
    print(my)

print("\nMy friends favorite Pizzas are: ")
for your in friends_pizza:
    print(your)