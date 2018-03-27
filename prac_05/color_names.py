COLOR_NAME_TO_HEX = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2",
               "CadetBlue": "#5f9ea0", "CornflowerBlue": "#6495ed", "DarkGoldenrod": "#b8860b", "DarkGreen": "#006400"}

color_name = input("Enter color name: ")
while color_name != "":
    if color_name in COLOR_NAME_TO_HEX:
        print(COLOR_NAME_TO_HEX[color_name])
    else:
        print("Color not in dictionary")
    color_name = input("Enter color name: ")
