# errors
# Created by marquiskurt
# robot-octodollop-fork (C) 2018 MechaMonarchs Team.
# Licensed under Apache 2.0 License
#
# A list of all possible errors in apps


class ConfigureError:
    open_file = 'The selected file could not be opened.'
    enter_key = 'One or more fields contains an enter key. Please enter the values without hitting ENTER.'
    alliance_entry = 'Invalid argument for alliance field.'
    position_entry = 'Invalid argument for position field.'
    user_cancel = 'The user cancelled the operation.'
    save_file_success = 'Your Akinom configuration file has been successfully saved.'

    def __init__(self):
        print("Error init complete")
