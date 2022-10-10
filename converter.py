# import PySimpleGUI as sg

# layout=[ # rows in GUI
#     [sg.Text('Text', enable_events=True, key='-TEXT-'), sg.Spin(['item1', 'item2'])], 
#     [sg.Button('Button', key='-BUTTON1-')], 
#     [sg.Input(key='-INPUT-')],
#     [sg.Text('Test'), sg.Button('Test Button', key='-BUTTON2-')]
#     ] 
# window=sg.Window(title='converter', layout=layout) #.read()

# while True:
#     event, values = window.read()
#     if event==sg.WIN_CLOSED:
#         break
    
#     if event == '-BUTTON1-':
#         # print('button pressed')
#         # print(values['-INPUT-'])
#         window['-TEXT-'].update(values['-INPUT-'])
#         window['-TEXT-'].update(visible= False)
#     if event == '-BUTTON2-':
#         print('test button pressed')

#     if event=='-TEXT-':
#         print('Text')

# window.close()

import PySimpleGUI as sg
# sg.theme_previewer()
sg.theme('DarkGrey8')
layout=[
    [sg.Input(key='-INPUT-'), 
            sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key='-UNITS-'),
            sg.Button('Convert', key='-CONVERT-')],
    [sg.Text('Output', key='-OUTPUT-')]
]

window=sg.Window('Converter', layout)

while True:
    event, values=window.read()

    if event==sg.WIN_CLOSED:
        break
    if event == '-CONVERT-':
        input_value=values['-INPUT-']
        # print(input_value)
        if input_value.isnumeric():
            # print(input_value)
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value)*0.6214, 2)
                    output_string=f'{input_value} km = {output} miles '
                case 'kg to pound':
                    output = round(float(input_value)*2.20462, 2)
                    output_string=f'{input_value} kg = {output} pounds '
                case 'sec to min':
                    output = round(float(input_value)/60, 2)
                    output_string=f'{input_value} seconds = {output} minutes '
            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('please enter a number')
        


window.close()
