from prac_06.guitar import Guitar

my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 500)

print(f"{my_guitar.name} get_age() - Excepted {my_guitar.get_age()}. Got {my_guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Excepted {another_guitar.get_age()}. Got {another_guitar.get_age()}")


print(f"{my_guitar.name} is_vintage() - Excepted {my_guitar.is_vintage()}. Got {my_guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Excepted {another_guitar.is_vintage()}. Got {another_guitar.is_vintage()}")