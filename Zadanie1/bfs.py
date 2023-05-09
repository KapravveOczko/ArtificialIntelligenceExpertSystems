from functions import *
from queue import *
import copy
import time

def bfs(puzzles, puzzlesAnswer,permutaction):

    """
    inicjujemy potrzebne wartości:
    startTime: czas rozpoczęcia działania programu
    last: ostatnio wykonany ruch
    queue: inicjalizacja kolejki fifo
    pozX,pozY: pozycja 0
    possibilities: możliwe przesunięcia
    visited: lista wykonaych ruchów
    statesVisited: lista odwiedzonych stanów
    """
    startTime = time.time()
    last = None
    queue = Queue()
    pozX,pozY = setStart(puzzles)
    possibilities = sortPossibilities(checkpossibilities(puzzles, pozX, pozY, last), permutaction)
    print(possibilities)
    path = ""
    statesVisited = 0
    maxDepth = 0
    """
    sprawdzamy czy stan początkowy to stan poszukiwany
    wypełniamy kolejkę fifo możliwymi ruchami
    entry: aktualny stan łamigłówki, ruch do wykonania, lista wykonanych już ruchów
    """

    if checkPuzzles(puzzles, puzzlesAnswer) == True:
        print("\tpath: " + str(path))
        print("\tlength: " + str(len(path)))
        print("\ttime: " + str(time.time() - startTime))
        return path,statesVisited + queue.size(), statesVisited,maxDepth, time.time()-startTime

    for i in range(len(possibilities)):
        entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]), copy.copy(path)]
        queue.enqueue(entry)

    """
    rozpoczyna się pętla wykonywana tak długo jak kolejka nie jest pusta
    
    pop'ujemy kolejkę wpełniając zmienne
    iterujemy ilość odwiedzonych stanów
    ustanawiamy nowe pozycje x,y
    wykonujemy ruch 
    dodajemy wykonany ruch do listy wykonaych ruchów
    sprawdzamy czy nowy stan jest rozwiązaniem
        jeśli tak tu konczy się funkcja, jej czas trwania jest pobierany przez zmienną endTime
    aktualizujemy "last"
    wypełniamy kolejkę fifo możliwymi ruchami
    
    """

    while queue.isEmpty != True :
        entry = queue.dequeue()
        puzzles = entry[0]
        wayToGo = entry[1]
        path = entry[2]

        last = wayToGo
        statesVisited = statesVisited + 1
        pozX, pozY = setStart(puzzles)

        # print("------------------")
        # print("wczytane wartości:")
        # print(puzzles)
        # print("ruch: " + str(wayToGo))
        # print("ścierzka: " + str(visited))

        puzzles = switchPositions(wayToGo,pozX,pozY,puzzles)
        path = str(path) + wayToGo

        if len(path) > maxDepth:
            maxDepth = len(path)

        if checkPuzzles(puzzles, puzzlesAnswer) == True:

            print("\ttime: " + str(path))
            print("\tlength: " + str(len(path)))
            print("\ttime: " + str(time.time() - startTime))
            return path,statesVisited + queue.size(), statesVisited,maxDepth, time.time()-startTime

        pozX, pozY = setStart(puzzles)
        possibilities = sortPossibilities(checkpossibilities(puzzles, pozX, pozY, last), permutaction)

        # print("po zmianie: " + str(puzzles))
        # print("możliwości: " + str(possibilities))
        # print("last: " + str(last))

        # last = wayToGo
        for i in range(len(possibilities)):
            entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]),copy.copy(path)]
            queue.enqueue(entry)

    print("\tALERT: false")
    return -1,statesVisited + queue.size(), statesVisited,maxDepth, time.time()-startTime

def saveBfsAnswerInfo(fileName, length,visited, processed,maxDepth, time, permutaction):
    '''
1 linia (liczba całkowita): długość znalezionego rozwiązania - o takiej samej wartości jak w pliku z rozwiązaniem (przy czym gdy program nie znalazł rozwiązania, wartość ta to -1);
2 linia (liczba całkowita): liczbę stanów odwiedzonych;
3 linia (liczba całkowita): liczbę stanów przetworzonych;
4 linia (liczba całkowita): maksymalną osiągniętą głębokość rekursji;
5 linia (liczba rzeczywista z dokładnością do 3 miejsc po przecinku): czas trwania procesu obliczeniowego w milisekundach.
    '''

    with open("./puzzlesAnswers/" + fileName + "_bfs_" + str(permutaction) + "_sol_info" + ".txt", "w") as file:
        if length != -1:
            strings = [str(len(length)), str(visited),str(processed),str(maxDepth),str(time)]
        else:
            strings = ["-1", str(visited),str(processed),str(maxDepth),str(time)]

        file.writelines([s + "\n" for s in strings])
    return 0

def saveBfsAnswer(fileName, visited,permutaction):

    '''
    1 linia (liczba całkowita): długość roziwązania
    2 linia (permutacja roziwązania):
    '''

    with open("./puzzlesAnswers/" +fileName + "_bfs_" + str(permutaction) + "_sol" + ".txt", "w") as file:
        if visited != -1:
            strings = [str(len(visited)), str(visited)]
            file.writelines([s + "\n" for s in strings])
        else:
            file.writelines("-1")
    return 0

def doBfs(fileName,puzzlesAnswer,permutaction):
    length,visited,processed,maxDepth,time = bfs(loadPuzzles(fileName),puzzlesAnswer,permutaction)
    time = round(time, 3)
    saveBfsAnswer(fileName, length,permutaction)
    saveBfsAnswerInfo(fileName, length,visited,processed,maxDepth,time,permutaction)
    return 0