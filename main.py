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
    print(dice.rolldice("4d6d3-10+2d4"))
    print("-------")
    # print(dice.rolldice("4d6d2"))
    # print("-------")
    # print(dice.rolldice("5d5k"))
    # print("-------")
    # print(dice.rolldice("5d8+2-1d6"))
    # print("-------")
    # print(dice.rolldice("Hello"))
    print(dice.rolldice("10d10k3+100-2d4"))
    print("-------")
    print(dice.rolldice("10d10d3-1000+2d4"))



if __name__ == "__main__":
    main()
