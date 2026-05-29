# Creating a dictionary
robot_parts = {'wheels': 4, 'motors': 2, 'sensors': 5}
print('Robot Parts Dictionary', robot_parts)
print('')

# Dictionary with various data types
robot_specs = {
    'name': 'AutoBot',
    'parts': robot_parts,
    'features': ['autonomous', 'solar_powered', 'waterproof'],
    'dimensions': {'height': 120, 'width': 75, 'weight': 150}
}

print('Robot Specifications dictionary:', robot_specs)
print('')

# Accessing and modifying dictionary values
print('Robot Height: ', robot_specs['dimensions']['height'])
print('')
robot_specs['speed'] = '25 km/h'
print('Updated Robot Specifications dictionary:', robot_specs)
print('')

# Removing an item
del robot_specs['speed']
print('After deletion:', robot_specs)
print('')

# Looping through a dictionary
for key, value in robot_parts.items():
    print(key, ': ', value)

