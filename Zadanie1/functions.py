import numpy as np

def  loadPuzzles(fileName):
    fileName = "./puzzles/" + fileName + ".txt"
    with open(fileName, 'r') as file:
        content = file.read()
        content = content.replace("\n", " ")
        # print (content)

        w = int(content[0])  # Konwersja na liczbę całkowitą
        k = int(content[2])  # Konwersja na liczbę całkowitą
        content = content[4:]

        # print(content)

        array = []
        for i in content.split():
            array.append(int(i))
        puzzle = [array[i:i + w] for i in range(0, len(array), k)]

        for i in range(w):
            for j in range(k):
                puzzle[i][j] = str(puzzle[i][j])
                puzzle[i][j] = puzzle[i][j].replace(" ","")

        # print(puzzle)

    return puzzle
'''
:return True if puzzles are equal
:return False if puzzles not equal
'''
def checkPuzzles(A, B):
    result = True
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != B[i][j]:
                result = False
                break

    #print(result)
    return result

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
                break

    return pozX, pozY

"""
sprawdza jakie ruchy są możliwe z danej pozycji
uzględnia ostatnią pozycję na której znajdowało się 0
"""
def checkpossibilities(puzzles, pozX, pozY, last = None):
    possibilities = []

    if last != None:
        if last == "U":
            last = "D"
        elif last == "D":
            last = "U"
        elif last == "L":
            last = "R"
        elif last == "R":
            last = "L"

        # sprawdz U
    if pozY + 1 < len(puzzles):
        if puzzles[pozY + 1][pozX] is not None:
            possibilities.append("D")

        # sprawdz D
    if pozY - 1 >= 0:
        if puzzles[pozY - 1][pozX] is not None:
            possibilities.append("U")

    # sprawdz R
    if pozX + 1 < len(puzzles[0]):
        if puzzles[pozY][pozX + 1] is not None:
            possibilities.append("R")

    # sprawdz L
    if pozX - 1 >= 0:
        if puzzles[pozY][pozX - 1] is not None:
            possibilities.append("L")

    if last in possibilities:
        possibilities.remove(last)

    return possibilities

def switchPositions(move,pozX,pozY,puzzles):

    if move == "D":
        puzzles[pozY][pozX] = puzzles[pozY+1][pozX]
        puzzles[pozY + 1][pozX] = "0"
    elif move == "U":
        puzzles[pozY][pozX] = puzzles[pozY - 1][pozX]
        puzzles[pozY - 1][pozX] = "0"
    elif move == "L":
        puzzles[pozY][pozX] = puzzles[pozY][pozX-1]
        puzzles[pozY][pozX-1] = "0"
    elif move == "R":
        puzzles[pozY][pozX] = puzzles[pozY][pozX + 1]
        puzzles[pozY][pozX + 1] = "0"

    return puzzles