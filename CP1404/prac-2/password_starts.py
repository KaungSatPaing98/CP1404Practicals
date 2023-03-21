MINIMUM_LENGTH = 5
while True:
    password = (input("Enter password: "))
    if len(password) <= MINIMUM_LENGTH:
        message = f"Password is too short. It must be at least {MINIMUM_LENGTH} characters long"
    else:
        message = "*" * len(password)
    print(message)




