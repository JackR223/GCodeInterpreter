import StraightLineInterpol

def interpolate(cmdIn, currPosition):

    values = cmdIn.split()

    endpointX = currPosition[0]
    endpointY = currPosition[1]
    endpointZ = currPosition[2]

    #pass values into variables
    for value in values:
        if value.startswith("X"):
            endpointX = float(value[1:len(value)])
        elif value.startswith("Y"):
            endPointY = float(value[1:len(value)])
        elif value.startswith("Z"):
            endPointZ = float(value[1:len(value)])

    points = StraightLineInterpol.interpolate(currPosition, endpointX, endPointY, endPointZ)

    return points
