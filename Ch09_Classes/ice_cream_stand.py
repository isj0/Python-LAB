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

class IceCreamStand(Restaurant):
    """Represent aspects of a Restaurant, specific to Ice Cream Stands."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'mango']

    def flavors_offered(self):
        """Print flavors offered by the ice cream stand."""

        print("\nWe offer the following favors of ice cream.")
        for flavor in self.flavors:
            print(f" -{flavor}.")

stand = IceCreamStand('Fun-Ice', 'Ice cream stand')
stand.describe_restaurant()
stand.flavors_offered()

    