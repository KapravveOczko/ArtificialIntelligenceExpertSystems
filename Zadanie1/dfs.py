from functions import *
from stack import *
import copy
import time

'''
lifo
kolejka stanów odwiedzonych

    sprawdzamy stan
    sprawdzamy możliwości poruszenia się z aktualnego stanu
    dodajemy te stany do kolejki lifo
    dodajemy do nich tablice odwiedzonych stanów
    
'''

def dfs(puzzles, puzzlesAnswer):

    startTime = time.time()

    stack = Stack()
    pozX, pozY = setStart(puzzles)
    possibilities = checkpossibilities(puzzles, pozX, pozY)
    visited = []
    visited.append(copy.deepcopy(puzzles))
    path = ''

    statesVisited = 0
    maxDepth = 0 #trzeba dodać 1 na końcu bo stan początkowy

    if checkPuzzles(puzzles, puzzlesAnswer):
        return path, statesVisited, maxDepth + 1, time.time() - startTime

    for i in range(len(possibilities)):
        entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]), copy.deepcopy(visited), copy.copy(path)]
        stack.push(entry)

    while not stack.is_empty():
        entry = stack.pop()
        puzzles = entry[0]
        wayToGo = entry[1]
        visited = entry[2]
        path = entry[3]

        statesVisited = statesVisited + 1
        pozX, pozY = setStart(puzzles)
        path = str(path) + wayToGo

        if len(path) > maxDepth:
            maxDepth = len(path)

        print("------------------")
        print("wczytane wartości:")
        print(puzzles)
        print("ruch: " + str(wayToGo))
        print("odwiedzone" + str(visited))
        print("ścierzka: " +  str(path))

        puzzles = switchPositions(wayToGo, pozX, pozY, puzzles)
        if puzzles in visited:
            continue
        if checkPuzzles(puzzles, puzzlesAnswer):
            return path, statesVisited,  maxDepth + 1, time.time() - startTime

        pozX, pozY = setStart(puzzles)
        visited.append(copy.deepcopy(puzzles))
        possibilities = checkpossibilities(puzzles, pozX, pozY)
        if len(visited) == 15:
            continue

        print("po zmianie: " + str(puzzles))
        print("możliwości: " + str(possibilities))

        for i in range(len(possibilities)):
            entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]), copy.deepcopy(visited), copy.copy(path)]
            stack.push(entry)


    return -1, statesVisited, maxDepth + 1, time.time() - startTime


def saveDfsAnswerInfo(fileName, path, statesVisited,maxDepth, time):
    '''
1 linia (liczba całkowita): długość znalezionego rozwiązania - o takiej samej wartości jak w pliku z rozwiązaniem (przy czym gdy program nie znalazł rozwiązania, wartość ta to -1);
2 linia (liczba całkowita): liczbę stanów odwiedzonych;
3 linia (liczba całkowita): liczbę stanów przetworzonych;
4 linia (liczba całkowita): maksymalną osiągniętą głębokość rekursji;
5 linia (liczba rzeczywista z dokładnością do 3 miejsc po przecinku): czas trwania procesu obliczeniowego w milisekundach.
    '''

    with open("./puzzlesAnswers/" + fileName + "_dfs_sol_info" + ".txt", "w") as file:
        if path != -1:
            strings = [str(len(path)), str(statesVisited), str(statesVisited), str(maxDepth), str(time)]
        else:
            strings = ["-1", ]

        file.writelines([s + "\n" for s in strings])
    return 0

def saveDfsAnswer(fileName, path):

    '''
    1 linia (liczba całkowita): długość roziwązania
    2 linia (permutacja roziwązania):
    '''

    with open("./puzzlesAnswers/" +fileName + "_dfs_sol" + ".txt", "w") as file:
        if path != -1:
            strings = [str(len(path)), str(path)]
            file.writelines([s + "\n" for s in strings])
        else:
            file.writelines("-1")
    return 0
def doDfs(fileName,puzzlesAnswer):
    path, statesVisited, maxDepth, time = dfs(loadPuzzles(fileName),puzzlesAnswer)
    time = round(time, 3)
    saveDfsAnswer(fileName, path)
    saveDfsAnswerInfo(fileName, path, statesVisited,maxDepth, time)
    return 0