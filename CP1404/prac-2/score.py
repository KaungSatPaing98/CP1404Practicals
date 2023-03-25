"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    user_result = get_result(score)
    print(f"Your result is : {user_result}")
    random_score = random.randint(0, 100)
    random_result = get_result(random_score)
    print(f"Random score {random_score} has a result of {random_result}")


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
