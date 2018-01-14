# libitina
# Created by marquiskurt
# robot-octodollop-fork (C) 2018 MechaMonarchs Team.
# Licensed under Apache 2.0 License
#
# Hosts the properties of the robot, including alliance information and position on the field
from libitina.frc_functions import *
from libitina.frc_2018 import *


class Libitina:

    third_eye = False

    def enable_third_eye(self):
        """
        Enables the debugging mode for the robot. Should be only called for testing purposes.

        :return:
        """
        third_eye = True
        print("Third eye has been opened. Use this mode only for debugging.")
        print("Enabling the third eye on the field may cause unintended side effects!")

    def disable_third_eye(self):
        """
        Disables the debugging mode for the robot.

        :return:
        """
        third_eye = False
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

    def __init__(self):
        print("Libitina is initialized")