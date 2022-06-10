import PySimpleGUI as sg
import time

layout = [  [sg.Text("Centre machine: ")],
            [sg.Button("Forward")],
            [sg.Button("Left"), sg.Button("Right")],
            [sg.Button("Back")],
            [sg.Button("Up"), sg.Button("Down")],
            [sg.Button("OK")],
            [sg.Text("Lower tool until contact is made with face of material.\nYou can use a single sheet of paper between the tool and material face, in order to ensure correct spacing.")]]

#create window
window = sg.Window("Center", layout)

def runZeroFunc():
    while True:
        event, values = window.read()
        if event == "Forward":
            print("F")
            #time.sleep(0.5)
        if event == "Left":
            print("L")
        if event == "Right":
            print("R")
        if event == "Back":
            print("B")
        if event == "Up":
            print("U")
        if event == "Down":
            print("D")
        #close window if user selects ok button or closes window
        if event == "OK" or sg.WIN_CLOSED:
            break

    window.close()