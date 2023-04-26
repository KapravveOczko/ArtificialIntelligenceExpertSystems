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

    # sprawdz U
    if pozY + 1 < len(puzzles):
        if puzzles[pozY + 1][pozX] != "0":
            possibilities.append("U")
    else:
        NOT.append("U")

    # sprawdz D
    if pozY - 1 >= 0:
        if puzzles[pozY - 1][pozX] is not None:
            possibilities.append("D")
    else:
        NOT.append("D")

    # sprawdz P
    if pozX + 1 < len(puzzles[0]):
        if puzzles[pozY][pozX + 1] is not None:
            possibilities.append("P")
    else:
        NOT.append("P")

    # sprawdz L
    if pozX - 1 >= 0:
        if puzzles[pozY][pozX - 1] is not None:
            possibilities.append("L")
    else:
        NOT.append("L")

    print(possibilities)
    print(NOT)

    return 0