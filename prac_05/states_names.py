STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

for state in STATE_NAMES:
    print("{:3} is {}".format(state, STATE_NAMES[state]))

state = input("Enter short state: ")
state = state.upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ")
    state = state.upper()
