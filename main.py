# Importing modules
from config import Config

import tkinter as tk
from tkinter import ttk

# Importing the menu items

import diceroll.dice as dice

# Set up

dndconf = Config.MENU_OPTIONS
root = tk.Tk()
root.title("DND-Tools by WebSurferPhil")
root.minsize(800, 600)
tab_ctrl = ttk.Notebook(root)


dndconf["dice"] = {
    "name": "Dice Roller",
    "app": dice,
    "options": dice.options
}


class AppTab:
    def __init__(self, app):
        self.app_tab = ttk.Frame(tab_ctrl)
        print(dndconf[app]["name"])
        print("---")
        tab_ctrl.add(self.app_tab, text=dndconf[app]["name"])
        ttk.Label(self.app_tab, text=dndconf[app]["name"]).grid(column=0,
                                                                row=0,
                                                                padx=30,
                                                                pady=30)


def main():

    for module in dndconf:
        AppTab(app=module)

    tab_ctrl.pack(expand=1, fill="both")

    print(dice.rolldice("6d6k4+1-2d4+2d4-9d6"))
    print("-------")
    print(dice.statroller())
    print("\n\n\n\n Menu")
    root.mainloop()


if __name__ == "__main__":
    main()
