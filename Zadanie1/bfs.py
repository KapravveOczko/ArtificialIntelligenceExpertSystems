import  functions
from functions import *
from queue import *
import copy

'''
THE PLAN:

 -> sprawdzić stan na wejściu
 -> inicjować kolejkę (możliwe ścierzki i aktualny stan)
 
 -> LOOP
    -> pop z kolejki
    -> sprawdzić stan
        -> jeśli sukces zwracamy sukces
    -> sprawdzić możliwe ścierzki
    -> dodac ścierzki do kolejki (ścierzka + kolejka)
    
-> kolejka się skończyła bez sukcesu (zwracamy porażkę)

-------

jak zadziała robimy zapis jak nie mamy problem
 
'''


def bfs(puzzles, puzzlesAnswer):

    #sprawdzamy dane wejściowe
    if functions.checkPuzzles(puzzles,puzzlesAnswer) == True:
        return True
    last = None
    queue = Queue()

    #uzupełniamy początkową kolejkę
    pozX,pozY = setStart(puzzles)
    possibilities = checkpossibilities(puzzles,pozX,pozY)
    visited = None #stany odiwedzone

    for i in range(len(possibilities)):
        entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i])]
        queue.enqueue(entry)

    #przeszukujemy w szerz dopuki kolejka nie jest pusta
    while queue.isEmpty != True :

        entry = queue.dequeue()
        puzzles = entry[0]
        wayToGo = entry[1]

        pozX, pozY = setStart(puzzles)

        print("------------------")
        queue.print_queue()
        print("------------------")
        print(puzzles)
        print(wayToGo)
        print("===")
        puzzles = switchPositions(wayToGo,pozX,pozY,puzzles)
        pozX, pozY = setStart(puzzles)
        possibilities = checkpossibilities(puzzles, pozX, pozY, last)

        print(puzzles)

        if functions.checkPuzzles(puzzles, puzzlesAnswer) == True:
            return True
        last = wayToGo

        for i in range(len(possibilities)):
            entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i])]
            queue.enqueue(entry)

    return False

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
        if last == "D":
            last = "U"
        if last == "L":
            last = "P"
        if last == "P":
            last = "L"

        # sprawdz U
    if pozY + 1 < len(puzzles):
        if puzzles[pozY + 1][pozX] is not None:
            possibilities.append("D")


        # sprawdz D
    if pozY - 1 >= 0:
        if puzzles[pozY - 1][pozX] is not None:
            possibilities.append("U")

    # sprawdz P
    if pozX + 1 < len(puzzles[0]):
        if puzzles[pozY][pozX + 1] is not None:
            possibilities.append("P")

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
    elif move == "P":
        puzzles[pozY][pozX] = puzzles[pozY][pozX + 1]
        puzzles[pozY][pozX + 1] = "0"

    return puzzles