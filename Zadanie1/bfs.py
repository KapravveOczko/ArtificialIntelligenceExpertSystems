import numpy as np
from functions import *


def bfs(puzzles):
    pozX, puzY = setStart(puzzles)

    return 0

"""
znajduje pozycję 0
"""
def setStart(puzzles):

    pozX = None
    pozY = None

    for i in range(len(puzzles)):
        for j in range(len(puzzles[0])):
            if puzzles[i][j] == "0":
                pozY = i
                pozX = j
                return pozX, pozY

    return pozX, pozY


def checkpossibilities(puzzles, pozX, pozY):

    possibilities = []
    NOT = []

    #sprawdz U
    try:
        if puzzles[pozY+1][pozX] != None:
            possibilities.append("U")
    except:
        NOT.append("U")

    #sprawdz D
    try:
        if puzzles[pozY -1][pozX] != None:
            possibilities.append("D")
    except:
        NOT.append("D")

    #sprawdz P
    try:
        if puzzles[pozY][pozX+1] != None:
            possibilities.append("P")
    except:
        NOT.append("P")

    # sprawdz L
    try:
        if puzzles[pozY][pozX -1] != None:
            possibilities.append("L")
    except:
        NOT.append("L")

    print(possibilities)
    print(NOT)

    return 0