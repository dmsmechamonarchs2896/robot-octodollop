# frc_functions
# Created by marquiskurt
# robot-octodollop (C) 2018 MechaMonarchs Team.
# Licensed under Apache 2.0 License
#
# Provides the primary functions in the robot, regardless of competition rules

import time


# Move forward for 'run_time' seconds
def move_forward(run_time: float):
    """
    Moves the robot forward for a set amount of time.

    :param run_time: How long the function should run in seconds
    :return:
    """
    end_time = time.time() + run_time
    print("Moving forward")

    while time.time() < end_time:
        print("^")
        # Input code here to move robot forward

    print("Moved forward for " + str(run_time) + " seconds.")


# Move backward for 'run_time' seconds
def move_backward(run_time: float):
    """
    Moves the robot backward for a set amount of time.

    :param run_time: How long the function should run in seconds.
    :return:
    """
    end_time = time.time() + run_time
    print("Moving backward")

    while time.time() < end_time:
        print("v")
        # Input code here to move robot backward

    print("Moved backward for " + str(run_time) + " seconds.")


# Stop the robot from moving at all
def stop():
    """
    Stops the robot from moving.

    :return:
    """
    print("Stopping...")
    # Input code here to make robot stop

    print("The robot has stopped.")
