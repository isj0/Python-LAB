# create a simple list of bicycles
bicycles = ['trek', 'canondale', 'redline', 'specialized']

# index positions start at 0 not 1
# print(bicycles[0].title())
# print(bicycles[3].title())

# acess the last element, -1 for last
# -2 for second last and so on ...
# this is helpful when you do not know 
# the length of the list

# print(bicycles[-1])
# print(bicycles[-2])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)