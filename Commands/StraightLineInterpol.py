def interpolate(targetPosition, currPosition):
    #print(targetPosition)

    #SHOULD BASE THIS VALUE ON LENGTH OF LINE -> LONGER = MORE POINTS
    #SHOULD ULTIMATELY RESULT IN EACH LINE HAVING EQUIDISTANT POINTS
    n = 10 #number of points on line to interpolate

    points = []
    
    if currPosition[0] != targetPosition[0] or currPosition[1] != targetPosition[1] or currPosition[2] != targetPosition[2]:
        for i in range(n+1):
            a = float(i) / n    #rescale 0 < i < n --> 0 < a < 1
            x = round((1 - a) * currPosition[0] + a * targetPosition[0])    #interpolate x coordinate (round because cannot have fractional coord)
            y = round((1 - a) * currPosition[1] + a * targetPosition[1])    #interpolate y coordinate
            z = round((1 - a) * currPosition[2] + a * targetPosition[2])    #interpolate z coordinate
        
            #array to store list of points to pass through 
            points.append((x, y, z, currPosition[3]))

    return points