# Created by: Gavin Zhou
# Created on: Oct 2017
# Created for: ICS3U
# This program displays area and perimeter of a rectangle,
# but this time the user can enter different lengths and widths

import ui

def calculate_Temperature_Fahrenheit(Temperature_Celsius):
    # calculate Temperature_Fahrenheit
    
    Temperature_Fahrenheit = (9/5)*(Temperature_Celsius)+32
    view['Temperature_Fahrenheit_answer_label'].text = 'The anwser is: ' + str(Temperature_Fahrenheit)

def calculate_button_touch_up_inside(sender):
    # input
    Temperature_Celsius = int(view['Temperature_Celsius_textbox'].text)
    calculate_Temperature_Fahrenheit(Temperature_Celsius)

view = ui.load_view()
view.present('full_screen')
