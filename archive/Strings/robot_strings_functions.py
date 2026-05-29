# message = 'Hello, Advanced Intelligent Machines'
# print(len(message))
# print(message.upper())
# print(message.lower())
# print(message.title())

# command_str = 'MOVE:FORWARD'
# command, parameter = command_str.split(':')
# print('Command:', command)
# print('Parameter:', parameter)

# distance_str = '12.6m'
# distance_str = distance_str.strip('m')
# distance = float(distance_str)
# print('Distance:', distance)

status_message = 'Error: Sensor disconnected'
print(status_message)
status_message = status_message.replace('Error', 'Warning')
print(status_message)
