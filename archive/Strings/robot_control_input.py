# Command input for robot control
# command = input('Enter command for the robot (move, stop, turn): ').lower()

# if command == 'move':
#     print('Robot moving...')
# elif command == 'stop':
#     print('Robot stopping...')
# elif command == 'turn':
#     direction = input('Which direction to turn (left or right)? ').lower()
#     print(f'Robot turning {direction}')
# else:
#     print('Unknown command.')

# Setting robot speed
# speed = input('Enter robot speed (1-10): ')
# speed = int(speed)  # Conver the input from string to integer
# print(f'Robot speed set to {speed}')

# Simulate setting sensor threshold
# threshold = input('Set sensor threshold (e.g,. temperature, distance): ')
# threshold = float(threshold)

# print(f'Sensor threshold set at {threshold} units.')

# Accepting multiple configuration values
configurations = input('Enter robot configurations separated by commas(arm lengthm camera resolution, wheel diameter, torso width):')

config_list = configurations.split(',')

print('Robot configurations set:', config_list)

    