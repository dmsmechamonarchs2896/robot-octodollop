# This file should be used to define general robotics functions.

import time


def move_forward(seconds):
    n = 0
    print("Starting to move forward...")

    while n < (seconds + 1):
        print("^")
        time.sleep(1)
        n = n + 1

    print("Moved forward for " + str(seconds) + " seconds.")
