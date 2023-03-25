def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temp_celsius = 20
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
print(f"{temp_celsius} Celsius is {temp_fahrenheit} Fahrenheit")

temp_fahrenheit = 68
temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit} Fahrenheit is {temp_celsius} Celsius")
