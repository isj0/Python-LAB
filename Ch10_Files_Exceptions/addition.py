print("Addition Calculator")


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    answer = num1 + num2
except ValueError:
    print("Please enter an integer.")
else:
    print(answer)