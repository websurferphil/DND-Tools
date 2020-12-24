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
    print(dice.a)
    print(dice.rolldice("2d10k3+10+6d8"))


if __name__ == "__main__":
    main()
