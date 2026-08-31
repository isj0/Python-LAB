def describe_pet(pet_name, animal_type = 'dog'):

# def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'kutta')
describe_pet(animal_type='cat', pet_name='billi')
describe_pet(pet_name='gadha', animal_type='donkey')
describe_pet(pet_name='Timmy')