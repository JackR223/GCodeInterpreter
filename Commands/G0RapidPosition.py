import Commands.StraightLineInterpol #needs this when run from interpreter.py
import StraightLineInterpol

def interpolate(targetPosition, currPosition):

    points = StraightLineInterpol.interpolate(targetPosition, currPosition)

    return points
