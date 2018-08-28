HEX_COLOURS = {"AliceBlue": "#f0f8ff", "azure1": "#f0ffff",
               "azure2": "#e0eeee", "azure3": "#c1cdcd",
               "beige": "#f5f5dc", "black": "#000000",
               "brown": "#a52a2a", "coral": "#ff7f50"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    if colour_name in HEX_COLOURS:
        print(colour_name, "is", HEX_COLOURS[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ")

