import time

mmStep = 0.1

#deals wih motor control
def move(path, currPosition):

    retValue = currPosition #base case

    for target in path:
        retValue[0] = target[0]
        retValue[1] = target[1]
        retValue[2] = target[2]
        retValue[3] = target[3]
        #print(str(retValue[0]) + ',' + str(retValue[1]) + ',' + str(retValue[2]))
        print(str(retValue[0]) + ',' + str(retValue[1]))

        #move in x, then y, then z sleeping each time
            #sleep required amonunt to maintain feed speed
            #stepsMin = target[3]/mmStep #this many steps per minute as a target        UNCOMMENT LATER!!!
            #waitTime = 60/stepsMin
            #time.sleep(waitTime)

    return(retValue) #return retValue as final position