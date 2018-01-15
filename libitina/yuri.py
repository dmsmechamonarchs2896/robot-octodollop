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
    selected_alliance = 0 # 0 = red, 1 = blue
    selected_position = 0 # 0 = left, 1 = middle, 2 = right

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

    def save_settings(self):
    	"""
    	Writes any settings into a configuration file (libitina.chr)
    	
    	:return:
    	"""
    	print("Saving settings...")
    	with open('libitina.chr', 'w+') as f:
    		f.write('0\n1')
    	
    
    def __init__(self):
        print("Libitina is initialized")
        self.third_eye = False

