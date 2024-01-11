# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

import sys
import random

from pyfiglet import Figlet

# figlet = Figlet()
# figlet.setFont(random.choice(figfonts))

# print(figlet.renderText("Hello World"))


def main():

    figlet = Figlet()
    figfonts = figlet.getFonts()

    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(figfonts))
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        try: 
            figlet.setFont(font=str(sys.argv[2]))
        except:
            sys.exit("Invalid usage")
            return True

    else:
        sys.exit("Invalid usage")
        return True

    s = input("Input: ")
    try:
        print(figlet.renderText(s))
    except ValueError:
        sys.exit("Incorrect try")

if __name__ == "__main__":
    main()