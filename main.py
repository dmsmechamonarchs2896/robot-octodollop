# main
# Created by marquiskurt
# robot-octodollop (C) 2018 MechaMonarchs Team.
# Licensed under Apache 2.0 License
#
# Calls all functions needed and runs the main program
from libitina.frc_2018 import *

# TODO: Simplify Libitina import statement
from libitina.libitina import Libitina()

robot = Libitina()

# Start the main process
if __name__ == '__main__':
    # Put some main code here!
    print("Hi, Monika.")
    robot.enable_third_eye()
    run_automatically()