COLOR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2",
               "CadetBlue": "5f9ea0", "CornflowerBlue": "#6495ed", "DarkGoldenrod": "#b8860b", "DarkGreen": "#006400"}

color = input("Enter color name: ")
while color != "":
    if color in COLOR_NAMES:
        print(COLOR_NAMES[color])
    else:
        print("Color not in dictionary")
    color = input("Enter color name: ")

