import ZeroMachine
import FileSelector

#import gcode commands
import Commands.G0RapidPosition as G0
import Commands.G1LinearInterpol as G1
import Commands.G2CWInterpol as G2
import Commands.G3CCWInterpol as G3

#variable setup
currCommand = ""
abortRun = False    #abort current run and return to home coordinate if something goes wrong

#code for dealing with motor control:

#run zero function to set machine up:
ZeroMachine.runZeroFunc()

#code for selecting which file to get GCode from:
selectedFile = FileSelector.selectFile()

#machine ready to start:

#get commands from file:
commands = open("GCodeFiles\\" + selectedFile)

#iterate through commands:
for command in commands:
    if "M" in command:
        break
    elif "G" in command:
        currCommand = command

    if "G0 " in currCommand or "G00 " in currCommand:
        #run G0 command
        G0.test()
    elif "G1 " in currCommand or "G01 " in currCommand:
        #run G1 command
        G1.test()
    elif "G2 " in currCommand or "G02 " in currCommand:
        #run G2 command
        G2.test()
    elif "G3 " in currCommand or "G03 " in currCommand:
        #run G3 command
        G3.test()

#close command read as we have reached end of file:
commands.close()
