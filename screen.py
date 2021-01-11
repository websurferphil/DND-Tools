class MainScreen:

    def __init__(self, master):
        self.master = master

        # The scrolled list cells that will contain our tasks in each of the three categories
        self.title = self.master.add_scroll_menu('', 0, 0, row_span=6, column_span=2)
        self.in_progress_scroll_cell = self.master.add_scroll_menu('In Progress', 0, 2, row_span=7, column_span=2)
        self.done_scroll_cell = self.master.add_scroll_menu('Done', 0, 4, row_span=7, column_span=2)

        # Textbox for entering new items
        self.new_todo_textbox = self.master.add_text_box('TODO Item', 6, 0, column_span=2)