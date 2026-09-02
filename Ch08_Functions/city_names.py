def city_country(city, country):
    """Return formatted city and country name"""
    city_country = f'"{city}, {country}"'
    return city_country.title()

city1 = city_country('los angeles', 'usa')
print(city1)
city2 = city_country('melbourne', 'australia')
print(city2)
city3 = city_country('osaka', 'japan')
print(city3)