# 1
user_name = input("Enter your name: ")
in_file = open("name.txt", "w")
in_file.write(user_name)
in_file.close()

# 2
open_file = open("name.txt", "r")
print("Your Name is", user_name)

# 3
number_files = open("numbers.txt", "r")
number_1 = int(number_files.readline())
number_2 = int(number_files.readline())
result = number_1 + number_2
print("Total first two result is:", result)
number_files.close()

# 4
number_files = open("numbers.txt", "r")
total = 0
for line in number_files:
    num = int(line.strip())
    total += num
print("Total all lines result is:", total)

