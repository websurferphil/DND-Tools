import tkinter as tk
from tkinter import ttk


class EntryNeeded:

    def __init__(self, master, func):
        my_frame = tk.Frame(master)
        my_frame.pack()
        self.func = func

        self.my_entry = ttk.Entry(master)
        self.my_entry.bind('<Return>', self.runfunc)
        self.my_entry.pack(fill="x")

        self.my_label = ttk.Label(master, text="Type a roll")
        self.my_label.pack(fill="x")

    def runfunc(self, event):
        self.my_label.config(text=self.func(self.my_entry.get()))

