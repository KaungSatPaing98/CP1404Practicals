CODE_TO_COLOR = {"#0048ba": "Absolute Zero", "#b0bf1a": "Acid Green", "#f0f8ff": "AliceBlue",
                 "#e32636": "Alizarin crimson",
                 "#e52b50": "Amaranth", "#ffbf00": "Amber", "#9966cc": "Amethyst"}
print(CODE_TO_COLOR)

color_code = input("Enter short code of color: ")
while color_code != "":
    if color_code in CODE_TO_COLOR:
        print(color_code, "is", CODE_TO_COLOR[color_code])
    else:
        print("Invalid color code")
    color_code = input("Enter short code of color: ")

for color_code, color_name in CODE_TO_COLOR.items():
    print(f"{color_code:<3} is {color_name}")
