class Restaurant:
    """A simple model of a Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Description of the restaurant."""
        print(f"Welcome to, {self.restaurant_name}")
        print(f"And we offer {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Describes the status of the restaurant."""
        print(f"{self.restaurant_name} is now Opened!")

    def set_number_served(self, served):
        """Set the number of customer served."""
        self.number_served = served

    def increment_number_served(self, customers):
        """Add the number of customers served till now."""
        self.number_served += customers

my_restaurant = Restaurant("Vegan Fusion", "Indian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print(f"\nThe number of customer served = {my_restaurant.number_served}.")
my_restaurant.number_served = 3
print(f"\nThe number of customer served = {my_restaurant.number_served}.")

my_restaurant.set_number_served(2)
print(f"\nThe number of customer served = {my_restaurant.number_served}.")

my_restaurant.increment_number_served(5)
print(f"\nThe number of customer served = {my_restaurant.number_served}.")

