'''
Digital clock on PySimpleGui
'''
# --------------------IMPORTS-------------------- #
import time
import PySimpleGUI as sg
# --------------------THEME AND SETTINGS-------------------- #
THEME = sg.theme("DarkBrown4")
CLOCK = sg.Text('', key='clock', justification='center')

# --------------------LAYOUT-------------------- #
window = sg.Window('Python digital clock', size=(380, 180), grab_anywhere=True,
                   layout=[[CLOCK]],
                   font=('Impact', 50, 'bold'))
# --------------------TIME LOOP-------------------- #
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%d/%m/%Y \n%H:%M:%S'))
    match event:
        case sg.WIN_CLOSED:
            break
