rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'Mississippi': 'usa'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe following are the 3 famous rivers.")

for river in rivers.keys():
    print(f"The river {river.title()}.")

print("\nThe above rivers are located in the following countries.")
for country in rivers.values():
    print(f"{country.title()}")

