def make_pizza(size, *toppings):
    """Prints the list of toppings that have been requested."""
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the follwing toppings:")
    for topping in toppings:
        print(f" - {topping}")
