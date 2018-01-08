# frc_functions
# Created by marquiskurt
# robot-octodollop (C) 2018 MechaMonarchs Team.
# Licensed under Apache 2.0 License
#
# Provides the primary functions in the robot, regardless of competition rules

import time


def move_forward(seconds):
    end_time = time.time() + seconds
    print("Moving forward")

    while time.time() < end_time:
        print("^")
        # Input code here to move robot forward

    print("Moved forward for " + str(seconds) + " seconds.")