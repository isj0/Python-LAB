def divide_with_multiple_exceptions(x, y):
    try:
        # Convert inputs to float to handle string inputs
        x = float(x)
        y = float(y)
        result = x / y
        print(f'The result is {result}.')
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("Please enter valid numbers!")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

# Test cases
print('Test 1: Normal Division')
divide_with_multiple_exceptions(10, 2)

print("\nTest 2: Division by Zero")
divide_with_multiple_exceptions(10, 0)

print("\nTest 3: Invalid input")
divide_with_multiple_exceptions("abc", 2)

print("\nTest 4: Float division")
divide_with_multiple_exceptions(10.5, 2.5)
