def interpolate(targetPosition, currPosition): 

    n = 10 #number of points on line to interpolate

    points = []
    
    for i in range(n+1):
        a = float(i) / n    #rescale 0 < i < n --> 0 < a < 1
        x = (1 - a) * currPosition[0] + a * targetPosition[0]    #interpolate x coordinate
        y = (1 - a) * currPosition[1] + a * targetPosition[1]    #interpolate y coordinate
        z = (1 - a) * currPosition[2] + a * targetPosition[2]    #interpolate z coordinate
        
        #array to store list of points to pass through 
        points.append((x, y, z))