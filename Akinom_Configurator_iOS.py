# Akinom_Configurator_iOS
# Created by marquiskurt
# robot-octodollop (C) 2018 MechaMonarchs Team.
# Licensed under Apache 2.0 License
#
# Provide a mobile port of Akinom Configurator
# NOTE: This will only WRITE files to monika.amc, the default config.
import ui
import notification

file = open('monika.amc', 'w+')
ally_select = 'red'
pos_select = 'left'

def reset_config(sender):
	alliance_control.selected_index = 0
	position_control.selected_index = 0

def save_config(sender):
	ally = alliance_control.selected_index
	pos = position_control.selected_index
	
	# print(str(pos) + '\n' + str(ally)) [Use this as a debug!]
	
	if ally == 0:
		ally_select = 'red'
		print('Selected target is: RED')
	elif ally == 1:
		ally_select = 'blue'
		print('Selected target is: BLUE')
	else:
		print('No selected target')
		return
		
	if pos == 0:
		pos_select = 'left'
		print('Selected target is: LEFT')
	elif pos == 1:
		pos_select = 'middle'
		print('Selected target is: MIDDLE')
	elif pos == 2:
		pos_select = 'right'
		print('Selected target is: RIGHT')
	else:
		print('No selected target')
		return
		
	file.writelines(ally_select + "\n" + pos_select)
	file.close()
	toast = notification.schedule('The file has been successfully saved.', 0)

v = ui.load_view('Akinom_Configurator')
v.frame = (0, 0, 480, 320)
alliance_control = v.subviews[5]
position_control = v.subviews[6]
v.present('sheet')

