print("Hello, please say the secret word to enter: ")

word = input("secret word? ")

if word == 'please':
    print('You may enter !')
elif word == 'thank you':
    print('Ok master, your wish is my command')
elif word == 'wonderful':
    print('Not quite, my friend')
elif word == 'yummy':
    print("Not quite yet")
else:
    print("Sorry you can't enter now")

