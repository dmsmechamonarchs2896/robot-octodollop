# yuri
# Created by marquiskurt
# robot-octodollop-fork (C) 2018 MechaMonarchs Team.
# Licensed under Apache 2.0 License
#
# Hosts the properties of the robot, including alliance information and position on the field
from akinom.frc_functions import *
from akinom.frc_2018 import *
import linecache


class Monika(object):
    third_eye = False
    selected_alliance = "red"
    selected_position = "left"

    def enable_third_eye(self):
        """
        Enables the debugging mode for the robot. Should be only called for testing purposes.

        :return:
        """
        self.third_eye = True
        print("Third eye has been opened. Use this mode only for debugging.")
        print("Enabling the third eye on the field may cause unintended side effects!")

    def disable_third_eye(self):
        """
        Disables the debugging mode for the robot.

        :return:
        """
        self.third_eye = False
        print("Third eye has been closed.")

    def enable_debugging(self):
        """
        Enables the debugging mode for the robot. (friendlier version)

        :return:
        """
        self.enable_third_eye()

    def disable_debugging(self):
        """
        Disables the debugging mode for the robot. (friendlier version)

        :return:
        """
        self.disable_third_eye()

    def load_settings(self):
        """
        Loads settings from a configuration file (akinom.akmcfg)

        :return:
        """
        print("Loading settings...")
        self.selected_alliance = linecache.getline('monika.akmcfg', 1)
        self.selected_position = linecache.getline('monika.akmcfg', 2)

        print("Settings loaded")

    def report_self_information(self):
        """
        Reports system information, including alliance and position information, from a config file (akinom.akmcfg).

        :return:
        """
        if self.third_eye:
            print("Selected alliance is: " + self.selected_alliance)
            print("Selected position is: " + self.selected_position)
        else:
            print("Sorry, this command can only be run when the Third Eye has been enabled.")

    def __init__(self):
        print("Libitina is initialized")
        self.third_eye = False
