# Simple for loop with a list
colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
    print('Color:', color)

# For loop with range function
for i in range(4):      # Generate numbers from 0 to 3
    print('Number:', i)

# Iterating over a string
for char in 'robotics':
    print('Character:', char)

# looping through a dictionary
robot_parts = {'wheels': 4, 'motors': 2, 'sensors': 5}
for part, quantity in robot_parts.items():
    print('Part:', part, 'Quantity:', quantity)

# Nested for loops
for outer in range(3):
    for inner in range(3):
        print('Position:', outer, inner)

