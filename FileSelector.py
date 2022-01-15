import os
import PySimpleGUI as sg

def selectFile():
    availableFiles = os.listdir("GCodeFiles")

    layout = [  
                [sg.Text("Select a file to run:")],
                [sg.Button(file) for file in availableFiles]
             ]

    window = sg.Window("File Selector", layout)

    #event loop
    while True:
        event, values = window.Read()
        if event is None:
            break
        #return selected file
        return event