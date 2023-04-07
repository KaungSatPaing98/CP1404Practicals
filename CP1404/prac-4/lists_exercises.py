list = []
for i in range(0, 5):
    numbers = int(input(f"Number: "))
    list.append(numbers)
print(f"The first number is {list[0]}")
print(f"The last number is {list[-1]}")
print(f"The smallest number is {min(list)}")
print(f"The largest number is {max(list)}")
sum_number = sum(list)
average = sum_number / len(list)
print(f"The smallest number is {average}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_name = input("Enter user name: ").lower()
if user_name in usernames:
    print("Access granted")
else:
    print("Access denied")

