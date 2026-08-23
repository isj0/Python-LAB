age = int(input("Enter your age ('0' to quit): "))

active = True

while active:
    if age == 0:
        active = False
    elif age <= 3:
        print("Free entry !")
    elif age <= 12:
        print(f"Your ticket price is $10.")
    else:
        print(f"Your ticket price is $15.")

    age = int(input("Enter your age ('0' to quit): "))

    

