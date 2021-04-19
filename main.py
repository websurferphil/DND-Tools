# Importing modules
from config import Config
import utils

import eel

# Importing the menu items

import diceroll.dice as dice
import npc.npc as npc

# Set up

dndconf = Config.MENU_OPTIONS


eel.init('web')
eel.start('main.html', geometry={'size': (200, 100), 'position': (300, 50)})


dndconf["dice"] = utils.conf("Dice Rollers", dice, dice.options)
dndconf["npc"] = utils.conf("NPC Generators", npc, npc.options)


def main():

    print("something")


if __name__ == "__main__":
    main()
