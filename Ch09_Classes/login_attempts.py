class Users:
    """A simple model describing users."""

    def __init__(self, first_name, last_name, age, gender, height, weight):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        # adding a new attribute 
        self.login_attempts = 0

    def describe_user(self):
        """Description of a user."""
        print(f"First name: {self.first_name}.")
        print(f"Last name: {self.last_name}.")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kgs")
        print(f"Height: {self.height} cms.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, welcome to Hogwarts !")

    def increment_login_attempts(self):
        """Increments the value of login attempts by 1."""
        self.login_attempts += 1

    def read_login_attempts(self):
        """Print the values of login attempts by the user."""
        print(f"\nUser {self.first_name} has attempted {self.login_attempts} logins.")

    def reset_login_attempts(self):
        """Reset the value of login attempts to 0."""
        self.login_attempts = 0


user1 = Users('Harry', 'Potter', 12, 'Male', 135, 40)
user2 = Users('Hermoine', 'Granger', 12, 'Female', 130, 36)
user1.describe_user()
print()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

user1.read_login_attempts()
user1.reset_login_attempts()
user1.read_login_attempts()