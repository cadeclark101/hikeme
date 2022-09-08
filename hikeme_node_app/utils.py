from random import randrange

def getRandomWarning(warningFile, default=None):
    line = default
    for i, aline in enumerate(warningFile, start=1):
        if randrange(i) == 0:
            line = aline
    return line

def loadFile(fileName, mode):
    file = open(fileName, mode)
    return file