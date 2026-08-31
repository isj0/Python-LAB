def describe_city(city='cold city', country='Iceland'):
    """Displays description of city."""
    print(f"\n{city.title()} is in {country.title()}")

describe_city()
describe_city('Rykjavik')
describe_city('Dilli', 'india')
describe_city(country='canada', city='ottawa')

