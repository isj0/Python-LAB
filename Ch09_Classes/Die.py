from random import randint

class Die:
    """A simple attempt to model Die."""

    def __init__(self, sides=6):
        """Initialize attributes."""
        self.sides = sides

    def roll_die(self):
        print(f"-Current roll: {randint(1, self.sides)}")

die6 = Die(6)
print("Rolling a 6 sided die 10 times:")
for i in range(10):
    die6.roll_die()

die10 = Die(10)
print("\nRolling a 10 sides die 10 times.")
for i in range(10):
    die10.roll_die()

die20 = Die(20)
print("\nRolling a 20 sides die 10 times.")
for i in range(20):
    die20.roll_die()