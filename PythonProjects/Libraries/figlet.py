import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1: 
    user_input = input("Input: ")
    fonts = figlet.getFonts()
    figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(user_input))
else: 
    font = sys.argv[2]
    figlet.setFont(font = font)
    user_input = input("Input: ")
    print(figlet.renderText(user_input))


