def celcius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

temperatures_celcius = [0, 20 , 30, 40]
temperatures_fahrenheit = list(map(celcius_to_fahrenheit, temperatures_celcius))

print(temperatures_fahrenheit)