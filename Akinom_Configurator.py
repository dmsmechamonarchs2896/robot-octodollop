# Akinom_Configurator
# Created by marquiskurt
# robot-octodollop (C) 2018 MechaMonarchs Team.
# Licensed under Apache 2.0 License
#
# Offers a dialog for changing settings such as position and alliance
import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile
from akinom.errors import ConfigureError

import linecache

error = ConfigureError()


class Program:
    # Import fake Akinom info
    selected_alliance = "red"
    selected_position = "left"

    null_field = ''

    # List all of the possible errors


    # Initializes the window and puts everything into a grid
    def __init__(self, master):
        self.master = master
        master.title("Akinom Configurator")

        # Create the alliance and position elements
        self.alliance_label = tkinter.Label(text="Selected alliance")
        self.alliance_entry = tkinter.Entry()
        self.position_label = tkinter.Label(text="Selected position")
        self.position_entry = tkinter.Entry()

        # Place alliance and position elements into grid
        self.alliance_label.grid(row=0, column=0)
        self.alliance_entry.grid(row=0, column=1)
        self.position_label.grid(row=1, column=0)
        self.position_entry.grid(row=1, column=1)

        # Place the load config button into grid
        load_settings_button = tkinter.Button(text="Load from file", command=self.load_config)
        load_settings_button.grid(row=2, column=0)

        # Place the save config button into grid
        save_settings_button = tkinter.Button(text="Save to disk", command=self.save_config)
        save_settings_button.grid(row=2, column=1)

    # Loads Akinom info into entry fields
    def load_config(self):

        file = askopenfilename(filetypes=(("Akinom config files", "*.amc"),
                                           ("All files", "*.*")))
        if file:
            try:
                # Grab alliance info and place into entry field
                self.selected_alliance = linecache.getline(file, 1)
                self.selected_position = linecache.getline(file, 2)
                if self.alliance_entry.get() == self.null_field:
                    self.alliance_entry.insert(0, self.selected_alliance)
                else:
                    self.alliance_entry.delete(0, 'end')
                    self.alliance_entry.insert(0, self.selected_alliance)

                if self.position_entry.get() == self.null_field:
                    self.position_entry.insert(0, self.selected_position)
                else:
                    self.position_entry.delete(0, 'end')
                    self.position_entry.insert(0, self.selected_position)

            except:
                messagebox.showerror('Error', error.open_file)
            return

    # Save Akinom info into .chr file
    def save_config(self):
        ally = self.alliance_entry.get()
        pos = self.position_entry.get()
        file = asksaveasfile(mode="w", defaultextension='.amc')

        if file is None:
            messagebox.showerror('Error', error.user_cancel)
            return

        assert isinstance(file, object)
        file.writelines(ally + "\n" + pos)
        file.close()


# Call the program and open the window
root = tkinter.Tk()
program = Program(root)
root.resizable(False, False)
root.mainloop()