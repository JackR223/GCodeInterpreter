#at the moment, only working in coordinates, need to translate from coordinates to mm/step
#could add multithreading?
#need to also add some sort of cancel function

import ZeroMachine
import FileSelector
import GetXYZF
import StepperController

#import gcode commands
import Commands.G0RapidPosition as G0
import Commands.G1LinearInterpol as G1
import Commands.G2CWInterpol as G2
import Commands.G3CCWInterpol as G3

#variable setup
currCommand = ""
currPosition = [0, 0, 0, 70] #xyzf (xyz are coordinates, f is feed speed); POSITION WILL ALWAYS BE IN TERMS OF STEPS, NOT DISTANCE!

mmPerStep = 0.1 #value for converting distances to steps


try:#can perform interupt at any time and return machine to zero position
    #run zero function to set machine up:
    ZeroMachine.runZeroFunc()

    #code for selecting which file to get GCode from:
    selectedFile = FileSelector.selectFile()

    #get commands from selected file:
    commands = open("GCodeFiles\\" + selectedFile)


    #iterate through and perform these commands:
    for command in commands:
        if "M" in command:
            break
        elif "G" in command: #allows singular 'Gxx' command to cover multiple lines, will update when new command given
            currCommand = command

        if "G0 " in currCommand or "G00 " in currCommand: #FAST MOVE
            #run G0 command
            targetPosition = GetXYZF.getXYZF(command, currPosition, mmPerStep)
            path = G0.interpolate(targetPosition, currPosition)
            currPosition = StepperController.move(path, currPosition)
        elif "G1 " in currCommand or "G01 " in currCommand: #STRAIGHT LINE
            #run G1 command
            #print(command)
            targetPosition = GetXYZF.getXYZF(command, currPosition, mmPerStep)
            path = G1.interpolate(targetPosition, currPosition)
            #print(path)
            currPosition = StepperController.move(path, currPosition)
            #print(currPosition)
        elif "G2 " in currCommand or "G02 " in currCommand: #CLOCKWISE CURVE
            #run G2 command
            path = G2.interpolate(command, currPosition, mmPerStep)
            currPosition = StepperController.move(path, currPosition)
        elif "G3 " in currCommand or "G03 " in currCommand: #ANTI-CLOCKWISE CURVE
            #run G3 command
            path = G3.interpolate(command, currPosition)
            currPosition = StepperController.move(path, currPosition)

    #close command read as we have reached end of file:
    commands.close()
    
    #return machine to zero position

except KeyboardInterrupt:
    print("ERROR whilst cutting")
    print("returning to zero")
    print("...")
    #return to zero position, first in z direction, then x and y
    target = []
    target.append((currPosition[0],currPosition[1],0,70)) #return to zero on z axis first to lift tool clear of work surface
    StepperController.move(target, currPosition)
    target = []
    target.append((0,0,0,70)) #can now return in x and y directions
    StepperController.move(target,currPosition)
