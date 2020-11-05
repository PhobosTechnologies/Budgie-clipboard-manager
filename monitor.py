import gi
gi.require_version('Budgie', '1.0')
from gi.repository import Gtk, Gdk, GLib, Budgie

class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data, callback):
        super(Gtk.ListBoxRow, self).__init__()

        button = Gtk.Button(relief=Gtk.ReliefStyle.NONE)
        button.connect("clicked", callback)
        self.label = Gtk.Label(data, halign=Gtk.Align.START, width_chars=5, max_width_chars=5)
        self.label.set_line_wrap(False)
        button.add(self.label)
        self.add(button)


    def set_text(self, text):
        self.label.set_text(text)

class Monitor(Budgie.Applet):
    manager = None
    def __init__(self, uuid):
        Budgie.Applet.__init__(self)
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.HISTORY_LENGTH = 10
        self.history = []
        self.rows = []
        self.row_activated_flag = False

        self.display()
        self.start()


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
        icon = Gtk.Image.new_from_icon_name(
            "clipboard",
            Gtk.IconSize.MENU,
        )
        self.icon_box = Gtk.EventBox()
        self.icon_box.add(icon)
        self.add(self.icon_box)
        self.icon_box.show_all()

        self.pop_win = Budgie.Popover.new(relative_to=self.icon_box)
        self.pop_win.set_border_width(10)

        self.listbox = Gtk.ListBox()
        # self.listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        # self.listbox.set_activate_on_single_click(True)

        self.pop_win.add(self.listbox)
        self.pop_win.get_child().show_all()


        self.show_all()

        # self.listbox.connect('row-activated', self.__on_row_activated)
        self.icon_box.connect("button-press-event", self.__on_press)

    def __on_press(self, widget, event_btn):
        # self.icon_box.show_all()
        self.manager.show_popover(self.icon_box)

    def __on_row_activated(self, button):
        idx = self.rows.index(button.get_parent())
        item = self.history[idx]

        self.history.pop(idx)
        self.row_activated_flag = True
        self.clipboard.set_text(item, -1)

        self.pop_win.hide()

    def __insert_row(self, item):
        row = ListBoxRowWithData(item, self.__on_row_activated)
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

    def do_update_popovers(self, manager):
        self.manager = manager
        self.manager.register_popover(self.icon_box, self.pop_win)

