# A decorator is a function that takes another function
# as input and returns a new function

# decorator
def change_case(func):
    def myinner():
        return func().upper()
    return myinner

@change_case        # function below being decorated - @ symbol
def myfunction():       # function that gets decorated
    return "Hello world"

@change_case
def other_function():
    return "Good bye"

@change_case
def another_function(nam):
    return "Hello " + nam

print(myfunction())
print(other_function())
print(another_function("demo"))