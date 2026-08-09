age = 9

if age > 0 and age < 2:
    stage = 'baby'
elif age > 2 and age < 4:
    stage = 'toddler'
elif age >= 4 and age < 13:
    stage = 'kid'
elif age >= 13 and age < 20:
    stage = 'teenager'
elif age >= 20 and age < 65:
    stage = 'adult'
elif age >= 65:
    stage = 'elder'
    
print(f"{stage}")                    