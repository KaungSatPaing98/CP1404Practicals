import csv


def main():
    data = read_csv_file("wimbledon.csv")
    champions = count_champions(data)
    display_champions(champions)
    countries = get_countries(data)
    display_countries(countries)


def read_csv_file(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            data.append(row)
    return data


def count_champions(data):
    champions = {}
    for row in data[1:]:
        name = row[2]
        if name in champions:
            champions[name] += 1
        else:
            champions[name] = 1
    return champions


def display_champions(champions):
    print("Wimbledon Champions: ")
    for name, count in champions.items():
        print(name, count)


def get_countries(data):
    countries = set()
    for row in data[1:]:
        country = row[1]
        countries.add(country)
    return sorted(countries)


def display_countries(countries):
    print("These", len(countries), "countries have won Wimbledon: ")
    print(", ".join(countries))


main()
