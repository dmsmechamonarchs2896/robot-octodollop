# libiconfig
# Created by marquiskurt
# robot-octodollop (C) 2018 MechaMonarchs Team.
# Licensed under Apache 2.0 License
#
# Offers a dialog for changing settings such as position and alliance
from tkinter import *
import tkinter
from tkinter import messagebox
import linecache


class Program():
    selected_alliance = "red"
    selected_position = "left"

    alliance_label = Label(text="Selected alliance")
    alliance_entry = Entry()
    position_label = Label(text="Selected position")
    position_entry = Entry()

    icon = tkinter.BitmapImage('icon.icns')

    enter_key_error = 'One or more fields contains an enter key. Please enter the values without hitting ENTER.'
    alliance_entry_error = 'Invalid argument for alliance field.'
    position_entry_error = 'Invalid argument for position field.'
    save_file_success_message = 'Your Libitina configuration file has been successfully saved.'

    def __init__(self):
        self.alliance_label.grid(row=0, column=0)
        self.alliance_entry.grid(row=0, column=1)
        self.position_label.grid(row=1, column=0)
        self.position_entry.grid(row=1, column=1)

        load_settings_button = Button(text="Load config", command=self.load_config)
        load_settings_button.grid(row=2, column=0)

        save_settings_button = Button(text="Save config", command=self.save_config)
        save_settings_button.grid(row=2, column=1)

        BitmapImage('icon.icns')

    def load_config(self):
        self.selected_alliance = linecache.getline('libitina.chr', 1)
        self.alliance_entry.insert(0, str(self.selected_alliance))

        self.selected_position = linecache.getline('libitina.chr', 2)
        self.position_entry.insert(0, str(self.selected_position))

    def save_config(self):
        if self.alliance_entry.get() != "red" or self.alliance_entry.get() != "blue":
            messagebox.showerror('Error', self.alliance_entry_error)
            return 1
        else:
            self.selected_alliance = self.alliance_entry.get()
            fy = self.position_entry.get()
            if fy != "left" or fy != "middle" or fy != "right":
                messagebox.showerror('Error', self.position_entry_error)
                return 1
            else:
                self.selected_position = self.alliance_entry.get()
                with open('libitina.chr', 'w+') as f:
                    f.write(str(self.selected_alliance) + "\n" + str(self.selected_position))
                messagebox.showinfo('Success', self.save_file_success_message, icon="warning")


program = Program()
mainloop()
