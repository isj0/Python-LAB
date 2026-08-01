languages = ['python', 'C', 'Cpp', 'java script', 'java', 'spanish', 'japanese', 'english', 'hindi']

print("The first three items in the list are: ")

for lang in languages[:3]:
    print(lang.title())

print("\nThe three items for the middle are: ")

for lang in languages[3:6]:
    print(lang.title())

print("\nThe last three items in the list are: ")

for lang in languages[6:]:
    print(lang.title())