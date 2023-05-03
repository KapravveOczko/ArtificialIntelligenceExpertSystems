from functions import *
from queue import *
import copy
import time

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
    startTime = time.time()

    last = None
    queue = Queue()
    pozX,pozY = setStart(puzzles)
    possibilities = checkpossibilities(puzzles,pozX,pozY)
    visited = ""
    statesVisited = 1

    for i in range(len(possibilities)):
        entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]), copy.copy(visited)]
        queue.enqueue(entry)

    while queue.isEmpty != True :

        statesVisited = statesVisited +1

        entry = queue.dequeue()
        puzzles = entry[0]
        wayToGo = entry[1]
        visited = entry[2]

        pozX, pozY = setStart(puzzles)

        print("------------------")
        print("wczytane wartości:")
        print(puzzles)
        print("ruch: " + str(wayToGo))
        print("ścierzka: " + str(visited))

        puzzles = switchPositions(wayToGo,pozX,pozY,puzzles)
        visited = str(visited) + wayToGo

        if checkPuzzles(puzzles, puzzlesAnswer) == True:
            print(visited)
            endTime = time.time()
            return visited, statesVisited, endTime-startTime

        pozX, pozY = setStart(puzzles)
        possibilities = checkpossibilities(puzzles, pozX, pozY, last)

        print("po zmianie: " + str(puzzles))
        print("możliwości: " + str(possibilities))

        last = wayToGo
        for i in range(len(possibilities)):
            entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]),copy.copy(visited)]
            queue.enqueue(entry)

    endTime = time.time()
    return -1,statesVisited, startTime-endTime

def saveBfsAnswerInfo(fileName, visited, iter, time):
    '''
1 linia (liczba całkowita): długość znalezionego rozwiązania - o takiej samej wartości jak w pliku z rozwiązaniem (przy czym gdy program nie znalazł rozwiązania, wartość ta to -1);
2 linia (liczba całkowita): liczbę stanów odwiedzonych;
3 linia (liczba całkowita): liczbę stanów przetworzonych;
4 linia (liczba całkowita): maksymalną osiągniętą głębokość rekursji;
5 linia (liczba rzeczywista z dokładnością do 3 miejsc po przecinku): czas trwania procesu obliczeniowego w milisekundach.
    '''

    with open("./puzzlesAnswers/" + fileName + "_bfs_sol_info" + ".txt", "w") as file:
        if visited != -1:
            strings = [str(len(visited)), str(iter),str(iter),str(len(visited)),str(time)]
        else:
            strings = ["-1", str(iter),str(iter),str(iter),str(time)]

        file.writelines([s + "\n" for s in strings])
    return 0

def saveBfsAnswer(fileName, visited):

    with open("./puzzlesAnswers/" +fileName + "_bfs_sol" + ".txt", "w") as file:
        if visited != -1:
            strings = [str(len(visited)), str(visited)]
            file.writelines([s + "\n" for s in strings])
        else:
            file.writelines("-1")
    return 0

def doBfs(fileName,puzzlesAnswer):
    visited,iter,time = bfs(loadPuzzles(fileName),puzzlesAnswer)
    time = round(time, 3)
    saveBfsAnswer(fileName, visited)
    saveBfsAnswerInfo(fileName, visited, iter, time)
    return 0