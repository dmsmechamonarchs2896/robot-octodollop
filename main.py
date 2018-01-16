# main
# Created by marquiskurt
# robot-octodollop (C) 2018 MechaMonarchs Team.
# Licensed under Apache 2.0 License
#
# Calls all functions needed and runs the main program
from akinom.master import Monika
from akinom.frc_2018 import *


robot = Monika()

# Start the main process
if __name__ == '__main__':
    # Put some main code here!
    robot.enable_third_eye()
    robot.load_settings()
    robot.report_self_information()
    run_automatically()

