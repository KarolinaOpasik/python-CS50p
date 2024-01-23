# https://cs50.harvard.edu/python/2022/psets/4/figlet/

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    random.choice(figlet.getFonts())
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" or sys.argv[1] != "-font":
        sys.exit("Invalid usage")
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

text = input("Input: ")

print(figlet.renderText(text))
