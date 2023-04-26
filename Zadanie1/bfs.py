import numpy as np
from functions import *


def bfs(puzzles):
    pozX, puzY = setStart(puzzles)
    printPuzzles(puzzles)
    print("")
    switchPositions("D",pozX,puzY,puzzles)
    printPuzzles(puzzles)
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

"""
sprawdza jakie ruchy są możliwe z danej pozycji
uzględnia ostatnią pozycję na której znajdowało się 0
"""
def checkpossibilities(puzzles, pozX, pozY, last = None):
    possibilities = []
    NOT = []

    if last != None:
        if last == "U":
            last = "D"
        if last == "D":
            last = "U"
        if last == "L":
            last = "P"
        if last == "P":
            last = "L"

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

    if last in possibilities:
        possibilities.remove(last)
        NOT.append(last)

    print(possibilities)
    print(NOT)

    return possibilities

def switchPositions(move,pozX,pozY,puzzles):

    if move == "U":
        puzzles[pozY][pozX] = puzzles[pozY+1][pozX]
        puzzles[pozY + 1][pozX] = "0"
    elif move == "D":
        puzzles[pozY][pozX] = puzzles[pozY - 1][pozX]
        puzzles[pozY - 1][pozX] = "0"
    elif move == "L":
        puzzles[pozY][pozX] = puzzles[pozY][pozX-1]
        puzzles[pozY][pozX-1] = "0"
    elif move == "P":
        puzzles[pozY][pozX] = puzzles[pozY][pozX + 1]
        puzzles[pozY][pozX + 1] = "0"

    return puzzles