# Equal to 
print('10 == 10:', 10 == 10)

print('10 == 5:', 10 == 5)

# Not Equal to
print('10 != 5:', 10 != 5)

print('10 != 10:', 10 != 10)

# Less than
print('5 < 10:', 5 < 10)

# Greater than
print('5 > 10: ', 5 > 10)

# Less than or equal to
print('12.5 <= 12.1:', 12.5 <= 12.1)

# Greater than or equal to 
print('3.141 >= 1.619:', 3.141 >= 1.619)

# Robot sensor threshold check
sensor_threshold = 10
sensor_reading = 12

if sensor_reading >= sensor_threshold:
    print('Sensor threshold exceeded, take action.')
else:
    print('Sensor levels normal, no action required.')

# String comparison
print("'abc' < 'def': ", 'abc' < 'def')