import math

def interpolate(cmdIn, currPosition):

    values = cmdIn.split()
    points = []

    startpointX = currPosition[0]
    startpointY = currPosition[1]
    startpointZ = currPosition[2]

    endpointX = currPosition[0]
    endPointY = currPosition[1]
    endPointZ = currPosition[2]

    #pass values into variables
    for value in values:
        if value.startswith("X"):
            endpointX = float(value[1:len(value)])
        elif value.startswith("Y"):
            endPointY = float(value[1:len(value)])
        elif value.startswith("Z"):
            endPointZ = float(value[1:len(value)])


    n = 10 #number of points on line to interpolate

    points = []
    for i in range(n+1):
        a = float(i) / n    #rescale 0 < i < n --> 0 < a < 1
        x = (1 - a) * startpointX + a * endpointX    #interpolate x coordinate
        y = (1 - a) * startpointY + a * endPointY    #interpolate y coordinate
        z = (1 - a) * startpointZ + a * endPointZ    #interpolate z coordinate
        #points1.append((round(x),round(y),round(z)))
        
        #array to store list of points to pass through 
        points.append((x, y, z))

    return points
