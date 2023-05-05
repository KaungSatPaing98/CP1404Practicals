
import csv


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            year = int(year)
            cost = float(cost)
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def save_guitars(filename, guitars):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)
    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

    print("\nEnter details of a new guitar:")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)

    save_guitars(filename, guitars)
    print(f"\n{len(guitars)} guitars saved to {filename}.")


if __name__ == '__main__':
    main()

