<img width = "128px" align = "right" src = "./icon.png" />

# Libitina
**Codename Octodollop**

Official MechaMonarchs robot software for FRC 2018

## About Libitina
For the past few years, Team 2896 has used LabVIEW, a solid programming language, to code the robot. Although LabVIEW gets the job done, it isn't the most elegant solution or the most forward-thinking. Furthermore, LabVIEW's syntax and interface isn't easy to pick up for aspiring developers, especially those who come from text-based languages. This year, we wanted to try creating a robot program in Python 3 with the RobotPy frameworks to control the robot while at the same time creating a shell for future competitions.

Libitina is a master collection of tools to make the robot function. The Libitina Configurator (`libiconfig.py`) provides an easy way to configure the robot's information regarding alliance and field position information into a configuration file (`libitina.chr`). The robot's main code and its functions work with that configuration file to move the robot autonomously and through teleoperated modes accordingly. We plan to add more soon.

A LabVIEW-compatible version is available in the `robot-octodollop-labview` repository, though it will not rely on `libitina.chr`. [View code &rsaquo;](http://www.github.com/dmsmechamonarchs2896/robot-octodollop-labview)

> Note: It may be very tempting to take the `libitina.chr` file and copying it (or renaming an existing .chr file) into the `characters` folder of an existing _Doki Doki Literature Club!_ installation. Please, do **not** attempt to do this; it is unclear if this will damage the game or your robot.

## Required Modules
* `robotpy-wpilib-utilities`
* `pygame`
* `pyinstaller`
* `tkinter`

> Note: In PyCharm/PIP, the dependencies will be fetched and installed automatically.

## Contribute
Contribution information, including issue tracking and a list of contributors to the project, can be found in the [CONTRIB.md](CONTRIB.md) file.



