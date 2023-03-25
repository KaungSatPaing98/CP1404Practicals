def main():
    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_result(score)
            print("Result:", result)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid Choice")
        choice = input("Choice: ").upper()
    print("Fare Well")


def get_valid_score():
    score = int(input("Enter Your Score:"))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Enter Your Score:"))
    return score


def get_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * score)


main()
