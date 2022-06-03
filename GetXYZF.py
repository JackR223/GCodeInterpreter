def getXYZF(cmdIn, currPosition):

    values = cmdIn.split()
    
    x = currPosition[0]
    y = currPosition[1]
    z = currPosition[2]
    f = currPosition[3]

    #pass values into variables
    for value in values:
        if value.startswith("X"):
            x = float(value[1:len(value)])
        elif value.startswith("Y"):
            y = float(value[1:len(value)])
        elif value.startswith("Z"):
            z = float(value[1:len(value)])
        elif value.startswith("F"):
            f = float(value[1:len(value)])
            
    return[x, y, z, f]