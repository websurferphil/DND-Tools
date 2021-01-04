from pyfiglet import Figlet
import config

dndconf = config.Config.MENU_OPTIONS

import diceroll.dice as dice
dndconf["dice"] = {
    "name": "Dice Roller",
    "app": dice
}


f = Figlet(font="big")
print(f.renderText('DND-Tools'))


def main():
    print(dice.rolldice("4d6k3+1-2d4"))
    print("-------")
    print(dice.statroller())



if __name__ == "__main__":
    main()
