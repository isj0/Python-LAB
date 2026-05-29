# Lambda function is a small anonymous function
# Have only one expression - can take any number of arguments

# x = lambda a: a + 10
# print(x(5))

# prod = lambda a, b: a * b
# print(prod(5, 6))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 7))

def my_func(n):
    return lambda a: a*n

mydoubler = my_func(2)
mytripler = my_func(3)

print(mydoubler(11))
print(mytripler(11))