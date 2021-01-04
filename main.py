from pyfiglet import Figlet
from consolemenu import *
from consolemenu.items import *

import config

dndconf = config.Config.MENU_OPTIONS

f = Figlet(font="big")
menu = ConsoleMenu(f.renderText('DND-Tools'), "Subtitle")

import diceroll.dice as dice
dndconf["dice"] = {
    "name": "Dice Roller",
    "app": dice,
    "options":dice.options
}


def main():
    print(dice.rolldice("4d6k3+1-2d4"))
    print("-------")
    print(dice.statroller())
    print("\n\n\n\n Menu")
    print(dndconf["dice"]["options"])




if __name__ == "__main__":
    main()
