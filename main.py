# Octodollop Version 0.0.1
# (C) 2017 | Damien MechaMonarchs. 
# Licensed under Apache 2.0 License
#
# main.py
# This file is responsible for making the application run properly.

# Import the important stuff required to make Octodollop work

# Import the system
import sys

# Fetch the required PyQt libraries
from PyQt5 import QtWidgets, Qt, QtGui

# Fetch the MainWindow and its primary object
# Note: This is generated from uic!
from mainwindow import Ui_MainWindow

# Start the main process
if __name__ == '__main__':

    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Link the main window to the application
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Show the UI
    MainWindow.show()

    # Create a new notification to show a fake error
    systemtray_icon = QtWidgets.QSystemTrayIcon(app)
    systemtray_icon.show()
    systemtray_icon.showMessage('Compiler Error', 'The identifier bendy.exe could not be resolved.',
                                QtWidgets.QSystemTrayIcon.Warning)
    sys.exit(app.exec_())
