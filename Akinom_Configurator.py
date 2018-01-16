# AkinomConfigurator
# Created by marquiskurt
# robot-octodollop (C) 2018 MechaMonarchs Team.
# Licensed under Apache 2.0 License
#
# Offers a dialog for changing settings such as position and alliance
import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile

import linecache


class Program():
    # Import fake Akinom info
    selected_alliance = "red"
    selected_position = "left"

    # Create the alliance and position elements
    alliance_label = tkinter.Label(text="Selected alliance")
    alliance_entry = tkinter.Entry()
    position_label = tkinter.Label(text="Selected position")
    position_entry = tkinter.Entry()

    null_field = ''

    # List all of the possible errors
    open_file_error = 'The selected file could not be opened.'
    enter_key_error = 'One or more fields contains an enter key. Please enter the values without hitting ENTER.'
    alliance_entry_error = 'Invalid argument for alliance field.'
    position_entry_error = 'Invalid argument for position field.'
    user_cancel_error = 'The user cancelled the operation.'
    save_file_success_message = 'Your Akinom configuration file has been successfully saved.'

    # Initializes the window and puts everything into a grid
    def __init__(self):
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

        file = askopenfilename(filetypes=(("Akinom config files", "*.akmcfg"),
                                           ("All files", "*.*")))
        if file:
            try:
                # Grab alliance info and place into entry field
                self.selected_alliance = linecache.getline(file, 1)
                self.selected_position = linecache.getline(file, 2)
                if self.alliance_entry.get() == self.null_field:
                    self.alliance_entry.insert(0, str(self.selected_alliance))
                else:
                    self.alliance_entry.delete(0, 'end')
                    self.alliance_entry.insert(0, str(self.selected_alliance))

                if self.position_entry.get() == self.null_field:
                    self.position_entry.insert(0, str(self.selected_position))
                else:
                    self.position_entry.delete(0, 'end')
                    self.position_entry.insert(0, str(self.selected_position))

                # Grab position info and place into entry field


            except Exception as e:
                messagebox.showerror('Error', self.open_file_error)
            return

    # Save Akinom info into .chr file
    def save_config(self):
        ally = self.alliance_entry.get()
        pos = self.position_entry.get()
        file = asksaveasfile(mode="w", defaultextension='.akmcfg')

        if file is None:
            messagebox.showerror('Error', self.user_cancel_error)
            return
        else:
            assert isinstance(file, object)
            file.writelines(ally + "\n" + pos)
            file.close()

            # Print success and stop
            messagebox.showinfo('Success', self.save_file_success_message, icon="warning")


# Call the program and open the window
program = Program()
tkinter.mainloop()