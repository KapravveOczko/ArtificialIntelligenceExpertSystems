from functions import *
from stack import *
import copy

'''
lifo
kolejka stanów odwiedzonych

    sprawdzamy stan
    sprawdzamy możliwości poruszenia się z aktualnego stanu
    dodajemy te stany do kolejki lifo
    dodajemy do nich tablice odwiedzonych stanów
    

'''

def dfs(puzzles, puzzlesAnswer):
    if checkPuzzles(puzzles, puzzlesAnswer):
        return True

    stack = Stack()
    last = None
    pozX, pozY = setStart(puzzles)
    possibilities = checkpossibilities(puzzles, pozX, pozY)
    visited = []
    visited.append(copy.deepcopy(puzzles))
    path = ''

    for i in range(len(possibilities)):
        entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]), copy.deepcopy(visited), copy.copy(path)]
        stack.push(entry)

    while not stack.is_empty():
        entry = stack.pop()
        puzzles = entry[0]
        wayToGo = entry[1]
        visited = entry[2]
        path = entry[3]

        pozX, pozY = setStart(puzzles)
        path = str(path) + wayToGo

        print("------------------")
        print("wczytane wartości:")
        print(puzzles)
        print("ruch: " + str(wayToGo))
        print("odwiedzone" + str(visited))
        print("ścierzka: " +  str(path))

        puzzles = switchPositions(wayToGo, pozX, pozY, puzzles)
        if checkPuzzles(puzzles, puzzlesAnswer):
            print()
            print()
            print(path)
            return True

        is_visited = False
        for i in range(len(visited)):
            if visited[i] == puzzles:
                is_visited = True
                break

        if is_visited:
            continue

        pozX, pozY = setStart(puzzles)
        visited.append(copy.deepcopy(puzzles))

        if len(visited) == 7:
            continue

        possibilities = checkpossibilities(puzzles, pozX, pozY)

        print("po zmianie: " + str(puzzles))
        print("możliwości: " + str(possibilities))

        last = wayToGo

        for i in range(len(possibilities)):
            entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]), copy.deepcopy(visited), copy.copy(path)]
            stack.push(entry)


    return -1
