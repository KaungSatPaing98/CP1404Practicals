import csv

WELCOME_MESSAGE = "Travel Tracker 1.0 - by Kaung Sat Paing"
MENU = ("Menu:  \nL - List places \nR - Recommend random place \nA - Add new place \nM - Mark a place as visited \nQ "
        "- Quit")
print(WELCOME_MESSAGE)
print("3 places loaded from places.csv")
print(MENU)


def main():
    choice = input(">>> ").lower()
    if choice == 'l':
        pass
    elif choice == 'r':
        pass
    elif choice == 'a':
        pass
    elif choice == 'm':
        pass
    elif choice == 'q':
        pass
    else:
        print("Invalid menu choice")


main()

