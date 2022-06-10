import math

def interpolate(cmdIn, currPosition, mmPerStep):
    #print(currPosition)

    #array to store points for program to pass through in
    points = []
    
    startX = currPosition[0] #start position
    startY = currPosition[1]
    startZ = currPosition[2]

    endX = currPosition[0] #end position
    endY = currPosition[1]
    endZ = currPosition[2]

    f = currPosition[3] #feed speed

    i = 0
    j = 0

    values = cmdIn.split() #split command

    #pass values into variables
    for value in values:
        if value.startswith("X"):
            endX = float(value[1:len(value)])/mmPerStep
        elif value.startswith("Y"):
            endY = float(value[1:len(value)])/mmPerStep
        elif value.startswith("Z"):
            endZ = float(value[1:len(value)])/mmPerStep
        elif value.startswith("F"):
            f = float(value[1:len(value)])
        elif value.startswith("I"):
            i = float(value[1:len(value)])/mmPerStep
        elif value.startswith("J"):
            j = float(value[1:len(value)])/mmPerStep

    #i or j could be negative
    centerX = startX + i
    centerY = startY + j

    #radius = sqrt((change in x)^2 + (change in y)^2) 
    radius = math.sqrt(i**2 + j**2)

    #Given a radius length r and an angle t in radians and a circle's center (h,k),
    #you can calculate the coordinates of a point on the circumference as follows
    #(this is pseudo-code, you'll have to adapt it to your language):
    #float x = r*cos(t) + h;
    #float y = r*sin(t) + k;
    
    #t = arccos((x - h)/r)
    #t = arcsin((x - h)/r)

    #print((startX - centerX)/radius)
    startAngleX = math.acos((startX - centerX)/radius)
    startAngleY = math.asin((startY - centerY)/radius)

    #print((endX - centerX)/radius)
    endAngleX = math.acos((endX - centerX)/radius)
    endAngleY = math.asin((endY - centerY)/radius)

    #print(startAngleX)
    #print(startAngleY)
    #print("------------")
    #print(endAngleX)
    #print(endAngleY)


    intervalX = (endAngleX - startAngleX) / 10
    intervalY = (endAngleY - startAngleY) / 10

    for i in range(10):
        #print(i+1)
        currAngleX = startAngleX + (i+1)*intervalX
        currAngleY = startAngleY + (i+1)*intervalY
        currPosX = (math.cos(currAngleX)*radius)+centerX
        currPosY = (math.sin(currAngleY)*radius)+centerY
        #print(str(currPosX) + ", " + str(currPosY))
        points.append((currPosX, currPosY, startZ, f))

 

    #print(points)

    return points


#interpolate("X50.0723 Y66.3536 I8.5376 J0.924", [0,0,0,0]
#interpolate("X-0.5 Y5.5 I0 J2.5", [2,3,0,0], 1)    #X is end_pos_x, Y is end_pos_y, I is x distance from start to center,
                                                #j is y distance from start to center
#interpolate("X2 Y8 I2.5 J0", [-0.5,5.5,0,0], 1)
#interpolate("X4.5 Y5.5 I0 J-2.5", [2,8,0,0], 1)
#interpolate("X2 Y3 I-2.5 J0", [4.5,5.5,0,0], 1)