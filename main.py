# Importing modules

from blessed import Terminal
from config import Config
from screen import MainScreen
import py_cui

# Importing the menu items

import diceroll.dice as dice

dndconf = Config.MENU_OPTIONS
term = Terminal()


dndconf["dice"] = {
    "name": "Dice Roller",
    "app": dice,
    "options": dice.options
}


def main():
    print(dice.rolldice("6d6k4+1-2d4+2d4-9d6"))
    print("-------")
    print(dice.statroller())
    print("\n\n\n\n Menu")
    with term.location(0, term.height - 1):
        print('This is ' + term.green_on_yellow(term.underline('underlined')) + '!')
        print(f"{term.link('https://github.com/websurferphil/DND-Tools', 'Github')}")

    root = py_cui.PyCUI(7, 6)
    root.toggle_unicode_borders()
    root.set_title('DND-Tools by WebSurferPhil')
    s = MainScreen(root)
    root.start()

    s.add_menu_item(name=dndconf["dice"]["name"])


if __name__ == "__main__":
    main()
