import PySimpleGUI as sg
from time import time

def create_window():
    sg.theme('black')
    layout=[
        [sg.Push(), sg.Button(u' \u00D7 ', key='-CLOSE-', button_color='#FF0000', pad=0, border_width=0)],
        [sg.VPush()],
        [sg.Text('', font='Toung 50', key='-TIME-')],
        [
            sg.Button('Start', button_color=('#FFFFFF', '#FF0000'), border_width=0, key='-STARTSTOP-'),
            sg.Button('Lap', button_color=('#FFFFFF', '#FF0000'), border_width=0, key='-LAP-', visible=False)

        ],
        [sg.Column([[]], key='-LAPSE-')],
        [sg.VPush()]
        ]
    return sg.Window(
                    'Stopwatch', 
                    layout,
                    size=(300, 300),
                    no_titlebar=True,
                    element_justification='center')

window = create_window()
start_time=0
active=False
lap_amount=1

while True:
    event, values=window.read(timeout=10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event=='-STARTSTOP-':
        if active:
            # from active to stop
            active=False
            window['-STARTSTOP-'].update('Reset')
            window['-LAP-'].update(visible=False)
        else:
            # from stop to reset
            if start_time>0:
                window.close()
                window=create_window()
                start_time=0
                lap_amount=1
            else:
                # from start to active
                start_time=time()   
                active=True
                window['-STARTSTOP-'].update('Stop')
                window['-LAP-'].update(visible=True)
    
    if active:
        elapsed_time=round(time()-start_time,2)
        window['-TIME-'].update(elapsed_time)

    if event=='-LAP-':
        window.extend_layout(window['-LAPSE-'], [[sg.Text(lap_amount), sg.VSeparator(), sg.Text(elapsed_time)]])
        lap_amount+=1


    
