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
    # Import fake Libitina info
    selected_alliance = "red"
    selected_position = "left"

    # Create the alliance and position elements
    alliance_label = Label(text="Selected alliance")
    alliance_entry = Entry()
    position_label = Label(text="Selected position")
    position_entry = Entry()

    # List all of the possible errors
    enter_key_error = 'One or more fields contains an enter key. Please enter the values without hitting ENTER.'
    alliance_entry_error = 'Invalid argument for alliance field.'
    position_entry_error = 'Invalid argument for position field.'
    save_file_success_message = 'Your Libitina configuration file has been successfully saved.'

    # Initializes the window and puts everything into a grid
    def __init__(self):
        # Place alliance and position elements into grid
        self.alliance_label.grid(row=0, column=0)
        self.alliance_entry.grid(row=0, column=1)
        self.position_label.grid(row=1, column=0)
        self.position_entry.grid(row=1, column=1)

        # Place the load config button into grid
        load_settings_button = Button(text="Load config", command=self.load_config)
        load_settings_button.grid(row=2, column=0)

        # Place the save config button into grid
        save_settings_button = Button(text="Save config", command=self.save_config)
        save_settings_button.grid(row=2, column=1)

    # Loads Libitina info into entry fields
    def load_config(self):
        # Grab alliance info and place into entry field
        self.selected_alliance = linecache.getline('libitina.chr', 1)
        self.alliance_entry.insert(0, str(self.selected_alliance))

        # Grab position info and place into entry field
        self.selected_position = linecache.getline('libitina.chr', 2)
        self.position_entry.insert(0, str(self.selected_position))

    # Save Libitina info into .chr file
    def save_config(self):
        # Check if alliance field has proper entry
        if self.alliance_entry.get() != "red" or self.alliance_entry.get() != "blue":
            # Print error and stop
            messagebox.showerror('Error', self.alliance_entry_error)
            return 1
        else:
            # Set Libitina alliance info
            self.selected_alliance = self.alliance_entry.get()

            # Check if position field has proper entry
            fy = self.position_entry.get()
            if fy != "left" or fy != "middle" or fy != "right":
                # Print error and stop
                messagebox.showerror('Error', self.position_entry_error)
                return 1
            else:
                # Set Libitina position info
                self.selected_position = self.alliance_entry.get()

                # Create a file opener and save the data
                with open('libitina.chr', 'w+') as f:
                    f.write(str(self.selected_alliance) + "\n" + str(self.selected_position))

                # Print success and stop
                messagebox.showinfo('Success', self.save_file_success_message, icon="warning")


if __name__ == "__main__":
    # Call the program and open the window
    program = Program()
    mainloop()