class Restaurant:
    """A simple model of a Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Description of the restaurant."""
        print(f"Welcome to, {self.restaurant_name}")
        print(f"And we offer {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now Opened!")

my_restaurant = Restaurant("Vegan Fusion", "Indian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print()
restaurant2 = Restaurant("Ocean Paradise", "Mediterrnean")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()