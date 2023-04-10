CODE_TO_COLOR = {"#0048ba": "Absolute Zero", "#b0bf1a": "Acid Green", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")

for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:<3} is {state_name}")