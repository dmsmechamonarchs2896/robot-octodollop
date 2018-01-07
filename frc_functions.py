# This file should be used to define general robotics functions.

import time


def move_forward(seconds):
    end_time = time.time() + seconds
    print("Moving forward")

    while time.time() < end_time:
        print("^")
        # Input code here to move robot forward

    print("Moved forward for " + str(seconds) + " seconds.")