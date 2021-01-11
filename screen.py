from pyfiglet import Figlet
f = Figlet(font="big")


class MainScreen:

    def __init__(self, master):
        self.master = master

        # The menu
        self.title = self.master.add_block_label(f"{f.renderText('DND-Tools')}", 0, 0, row_span=2, column_span=6,
                                                 center=True)
        self.menu = self.master.add_scroll_menu("", 3, 0, column_span=4)

        # Textbox for entering new items
        self.new_todo_textbox = self.master.add_text_box('TODO Item', 6, 0, column_span=2)

    def add_menu_item(self, name=""):
        self.menu.add_item()
