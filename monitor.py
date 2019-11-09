import gi
gi.require_version('Budgie', '1.0')
from gi.repository import Gtk, Gdk, GLib, Budgie

class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        
        
        self.label = Gtk.Label(data, halign=Gtk.Align.START, width_chars=5, max_width_chars=5)
        self.label.set_line_wrap(False)
        self.add(self.label)

    def set_text(self, text):
        self.label.set_text(text)

class Monitor(Budgie.Applet):
    def __init__(self, uuid):

        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.HISTORY_LENGTH = 10
        self.history = []
        self.rows = []
        self.row_activated_flag = False

        self.start()
        self.display()


    def __update_history(self, item):

        self.history.insert(0, item)
        
        if len(self.history) > self.HISTORY_LENGTH:
            out = self.history.pop()
            out = None

    def update_handler(self, *args):
        item = self.clipboard.wait_for_text()

        if len(self.history) < self.HISTORY_LENGTH and not self.row_activated_flag:
            self.__insert_row(item)
        
        self.row_activated_flag = False
        self.__update_history(item)
        self.__update_ui(item)

    def start(self):
        self.clipboard.connect('owner-change',self.update_handler)

    def display(self):
        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        self.listbox.set_activate_on_single_click(True)
        self.box_outer = Gtk.EventBox()
        self.box_outer.add(self.listbox)   
        self.add(self.box_outer)

        self.box_outer.show_all()
        self.show_all()

        self.listbox.connect('row-activated', self.__on_row_activated)
        self.box_outer.connect("button-press-event", self.__on_press)

    def __on_press(self):
        self.box_outer.show_all()

    def __on_row_activated(self, listbox, row):
        idx = row.get_index()
        item = self.history[idx]

        self.history.pop(idx)
        self.row_activated_flag = True
        self.clipboard.set_text(item, -1)

    def __insert_row(self, item):
        row = ListBoxRowWithData(item)
        self.rows.append(row)
        self.listbox.add(row)
        return row

    def __update_ui(self, item):
        for row, item in zip(self.rows, self.history):
            if len(item) > 17:
                out = item[:30] + '...'
            else:
                out = item
            
            out = out.replace('\n', ' ')
            row.set_text(out)
        self.listbox.show_all()

        