import math

def interpolate(cmdIn, currPosition):
    #array to store points for program to pass through in
    points = []
    
    startX = currPosition[0]
    startY = currPosition[1]

    endX = currPosition[0]
    endY = currPosition[1]
    endZ = currPosition[2]
    f = currPosition[3]
    i = 0
    j = 0

    values = cmdIn.split()

    #pass values into variables
    for value in values:
        if value.startswith("X"):
            endX = float(value[1:len(value)])
        elif value.startswith("Y"):
            endY = float(value[1:len(value)])
        elif value.startswith("Z"):
            endZ = float(value[1:len(value)])
        elif value.startswith("F"):
            f = float(value[1:len(value)])
        elif value.startswith("I"):
            i = float(value[1:len(value)])
        elif value.startswith("J"):
            j = float(value[1:len(value)])

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

    startAngleX = math.acos((startX - centerX)/radius)
    startAngleY = math.asin((startY - centerY)/radius)

    print(startAngleX)
    print(startAngleY)
    print("------------")
    #print(endAngleX)
    #print(endAngleY)


    return points


interpolate("X50.0723 Y66.3536 I8.5376 J0.924", [0,0,0,0])