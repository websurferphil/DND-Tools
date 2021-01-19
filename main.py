# Importing modules
from config import Config
import utils
from classes import *

import tkinter as tk
from tkinter import ttk

# Importing the menu items

import diceroll.dice as dice
import npc.npc as npc

# Set up

dndconf = Config.MENU_OPTIONS
root = tk.Tk()
root.minsize(800, 600)
root.columnconfigure(10, weight=1, minsize=80)
root.columnconfigure(10, weight=1, minsize=60)
root.title("DND-Tools by WebSurferPhil")
tab_ctrl = ttk.Notebook(root)

dndconf["dice"] = utils.conf("Dice Rollers", dice, dice.options)
dndconf["npc"] = utils.conf("NPC Generators", npc, npc.options)

dice_frame = tk.Frame(tab_ctrl, bg="blue")
npc_frame = tk.Frame(tab_ctrl, bg="red")

dice_one = EntryNeeded(dice_frame, dndconf["dice"]["options"][0]["function"])

def main():
    tab_ctrl.add(dice_frame, text=dndconf["dice"]["name"])
    tab_ctrl.add(npc_frame, text=dndconf["npc"]["name"])

    tab_ctrl.pack(expand=1, fill="both")

    root.mainloop()


if __name__ == "__main__":
    main()
