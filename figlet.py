import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    print("Invalid usage")
    sys.exit(1)

availableFonts = figlet.getFonts()

if not isRandomFont:
    try:
        selected_font = sys.argv[2]
        if selected_font not in availableFonts:
            print(f"Font '{selected_font}' not available.")
            sys.exit(1)
        figlet.setFont(font=selected_font)
    except IndexError:
        print("Invalid usage. Please provide a font name.")
        sys.exit(1)

msg = input("Input: ")
print("Output:")
print(figlet.renderText(msg))
