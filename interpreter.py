import ZeroMachine
import Commands.G0RapidPosition as G0
import Commands.G1LinearInterpol as G1
import Commands.G2CWInterpol as G2
import Commands.G3CCWInterpol as G3

#code for dealing with motor control:

#run zero function to set machine up:
ZeroMachine.runZeroFunc()

#machine ready to start:
#testing:
G0.test()
G1.test()
G2.test()
G3.test()

#will be used to abort machine and return to home coordinate if something goes wrong
abortRun = False
