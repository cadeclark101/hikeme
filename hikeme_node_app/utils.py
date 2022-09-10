import random

def loadFile(fileName):
    file = open(fileName).read().splitlines()
    return file