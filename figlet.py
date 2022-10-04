import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

#reject CLA that is not 1 or 3 in len
if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage.") #system exits with the following error

elif sys.argv[2] not in figlet.getFonts(): #if the last CLI = a font
            sys.exit("Invalid usage.") #system exits with the following error

#run if CLI len = 1
elif len(sys.argv) == 1:
    asciify = input("Please enter a specific text you would like in ASCII, the font will be random unless you specify -f or --font [FONT] in the command line: ")
    r_font = random.choice(figlet.getFonts()) #randomise font
    figlet.setFont(font=r_font) #set to random font
    print(figlet.renderText(asciify)) #print output

#run if CLI input = 3
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        asciify = input("Please enter a specific text you would like in ASCII: ")
        chosen_font = sys.argv[2]
        figlet.setFont(font=chosen_font)
        print(figlet.renderText(asciify))
    else:
        sys.exit("Invalid usage.") #system exits with the following error

