## EMPTY window snippet
# import PySimpleGUI as sg

# layout=[[]]

# window = sg.Window('CWindow name', layout)

# while True:
#     event, values=window.read()
#     if event==sg.WIN_CLOSED:
#         break

# window.close()

import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    # g.theme_previewer()
    # sg.theme('Black') # Contrast dark
    # sg.theme('DarkGrey11') # Dark
    # sg.theme('Default') # Contrast light
    # sg.theme('Graygraygray') # Light
    sg.set_options(font='Calibri 14') # wlidth and height in characters notpixels
    bs=button_size=(3, 1)
    layout=[
        [sg.Text('', 
                font='Calibri 26', 
                justification='center', 
                expand_x=True, pad=(2, 3), 
                right_click_menu=theme_menu,
                key='-TEXT-')],
        [sg.Button('Clear', expand_x=True), sg.Button('Enter', expand_x=True)],
        [sg.Button(7, size=bs), sg.Button(8, size=bs), sg.Button(9, size=bs), sg.Button('*', size=bs)],
        [sg.Button(4, size=bs), sg.Button(5, size=bs), sg.Button(6, size=bs), sg.Button('/', size=bs)],
        [sg.Button(1, size=bs), sg.Button(2, size=bs), sg.Button(3, size=bs), sg.Button('-', size=bs)],
        [sg.Button(0, expand_x=True), sg.Button('.', size=bs), sg.Button('+', size=bs)],
        ]
    return sg.Window('Calculator', layout)

theme_menu=['menu', ['DarkGrey11', 'Black', 'Graygraygray', 'Default', 'random']]

window = create_window('DarkGrey11')

current_num=[]
full_operation=[]

while True:
    event, values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event in theme_menu[1]:
        # print(event)
        # window,close()
        window=create_window(event)

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        if event=='.':
            if len(current_num)>0 and '.' not in current_num:
                current_num.append(event)
        else:
            current_num.append(event)
            num_string=''.join(current_num) 
            print(num_string)
            window['-TEXT-'].update(num_string)


    if event in ['+', '-', '/', '*']:
        full_operation.append(''.join(current_num))
        current_num=[]
        full_operation.append(event)
        # print(full_operation)
        window['-TEXT-'].update('')


    if event == 'Enter':
        full_operation.append(''.join(current_num))
        result=eval(''.join(full_operation))
        window['-TEXT-'].update(result)

    if event=='Clear':
        window['-TEXT-'].update('')
        current_num=[]
        full_operation=[]



window.close()
