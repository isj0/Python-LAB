alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

del alien_0['points']
print(alien_0)

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# alien_0['color'] = 'yellow'
# print(f'The alien is now {alien_0['color']}.')

# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {'x_postion': 0, 'y_position': 25, 'speed': 'medium'}
# print(f'Original position: {alien_0['x_postion']}')

# # Move the alien to the right
# # Determine how far tomove the alien based on its current speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be fast alien
#     x_increment = 3

# # This new poistion is the old position plus the increment.
# alien_0['x_postion'] = alien_0['x_postion'] + x_increment
# print(f"New Position: {alien_0['x_postion']}")