import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tab Widget")
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
print(tab1)

tab_control.add(tab1, text="Tab 1")

ttk.Label(tab1, text="Welcome to test").grid(column=0,
                                             row=0,
                                             padx=30,
                                             pady=30)

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Tab 2")


ttk.Label(tab1, text="Welcome to test again").grid(column=0,
                                                   row=0,
                                                   padx=30,
                                                   pady=30)

tab_control.pack(expand=1, fill="both")

root.mainloop()
