import csv
import random

# Load places from CSV file
with open('places.csv') as file:
    reader = csv.reader(file)
    places = []
    for row in reader:
        name, country, rating, visited = row
        places.append((name, country, int(rating), visited == 'v'))

# Define menu options
def list_places():
    print_places(places)

def recommend_place():
    unvisited_places = [place for place in places if not place[3]]
    if unvisited_places:
        place = random.choice(unvisited_places)
        print(f"Not sure where to visit next?\nHow about... {place[0]} in {place[1]}?")
    else:
        print("You've visited all the places! Congrats!")

def add_place():
    name = input("Enter the name of the place: ")
    country = input("Enter the country the place is located in: ")
    rating = int(input("Enter a rating for the place (1-10): "))
    places.append((name, country, rating, False))
    print("Place added successfully!")

def mark_place_visited():
    print_places(places)
    num = int(input(f"{len(places)} places. You still want to visit {count_unvisited(places)} places.\nEnter the number of a place to mark as visited\n"))
    while num <= 0 or num > len(places):
        print("Invalid place number")
        num = int(input("Enter a valid place number\n"))
    if places[num-1][3]:
        print(f"You have already visited {places[num-1][0]}")
    else:
        places[num-1] = (places[num-1][0], places[num-1][1], places[num-1][2], True)
        print(f"{places[num-1][0]} visited!")

def print_places(places):
    for i, place in enumerate(places):
        print(f"{'*' if not place[3] else ''}{i+1}. {place[0]} in {place[1]} {place[2]}")
    print(f"{len(places)} places. You still want to visit {count_unvisited(places)} places.")

def count_unvisited(places):
    return sum(not place[3] for place in places)

# Main program loop
while True:
    print("Menu:")
    print("L - List places")
    print("R - Recommend random place")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")
    choice = input(">>> ").strip().lower()
    if choice == 'l':
        list_places()
    elif choice == 'r':
        recommend_place()
    elif choice == 'a':
        add_place()
    elif choice == 'm':
        mark_place_visited()
    elif choice == 'q':
        break
    else:
        print("Invalid menu choice")
