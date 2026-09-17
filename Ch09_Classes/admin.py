# class Users:
#     """A simple model describing users."""

#     def __init__(self, first_name, last_name, age, gender, height, weight):
#         """Initialize user attributes."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.gender = gender
#         self.height = height
#         self.weight = weight

#     def describe_user(self):
#         """Description of a user."""
#         print(f"First name: {self.first_name}.")
#         print(f"Last name: {self.last_name}.")
#         print(f"Age: {self.age}")
#         print(f"Weight: {self.weight} kgs")
#         print(f"Height: {self.height} cms.")

#     def greet_user(self):
#         print(f"Hello {self.first_name} {self.last_name}, welcome to Hogwarts !")

from users import Users

class Privileges:
    """A simple attempt to model privileges of an Admin."""

    def __init__(self):
        """Initialize Privileges attributes."""
        self.privileges = [
            "can add post", 
            "can delete post", 
            "can ban user"
        ]

    def show_privileges(self):
            """Display the privileges of an Administrator."""
    
            print("\nThe following are the privileges of an Administrator.")
            for privi in self.privileges:
                print(f"-{privi.title()}")

class Admin(Users):
    """Represents aspects of a user, specific to an Administrator."""

    def __init__(self, first_name, last_name, age, gender, height, weight):
        """
        Initialize attributes of the Parent class.
        Then initialize attributes specific to an Admin.
        """
        super().__init__(first_name, last_name, age, gender, height, weight)
        # self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = Privileges()
        

admin = Admin('Star', 'boy', 18, 'M', 179, 85)
admin.describe_user()
admin.privileges.show_privileges()

