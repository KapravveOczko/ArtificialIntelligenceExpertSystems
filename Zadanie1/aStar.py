from functions import *
import time
import copy
from queue import *

'''
hamming:
polega na oszacowaniu kosztu pozostałego do celu jako liczby płytek, które nie są już na swoim miejscu.

manhattan:
polega na oszacowaniu kosztu pozostałego do celu jako sumy odległości Manhattana każdej płytki od jej pozycji w celu

Inicjalizacja
1.1. Ustal stan początkowy planszy i stan docelowy (np. ułożoną planszę).
1.2. Utwórz węzeł początkowy zawierający stan początkowy, koszt g równy 0 oraz wartość heurystyki h 
    wyznaczoną na podstawie metryki Manhattan lub Hamminga.
1.3. Utwórz listę otwartych węzłów oraz listę zamkniętych węzłów.
1.4. Ustal wartość f_max jako wartość docelową algorytmu. [?]

2.1. Dodaj węzeł początkowy do otwartej listy węzłów.

Dla każdego węzła na otwartej liście węzłów, wykonaj poniższe czynności:
3.1. Sprawdź, czy wartość f węzła jest mniejsza niż f_max.  [?]
3.2. Jeśli wartość f jest większa lub równa f_max, przerwij działanie algorytmu. [?]
3.3. Jeśli stan węzła jest równy stanowi docelowemu, zwróć znalezioną ścieżkę.
3.4. Usuń węzeł z otwartej listy węzłów i dodaj go do zamkniętej listy węzłów.
3.5. Dla każdej możliwej operacji ruchu (przesunięcie pustego pola na planszy):
3.5.1. Utwórz nowy stan planszy na podstawie wykonanej operacji ruchu.
3.5.2. Jeśli nowy stan planszy już występuje na liście zamkniętych węzłów, pomiń operację ruchu.
3.5.3. Oblicz koszt g dla nowego stanu planszy jako koszt g węzła aktualnego plus 1.
3.5.4. Oblicz wartość heurystyki h dla nowego stanu planszy na podstawie metryki Manhattan lub Hamminga.
3.5.5. Utwórz nowy węzeł zawierający nowy stan planszy, koszt g oraz wartość heurystyki h.
3.5.6. Ustaw węzeł poprzedzający dla nowego węzła na aktualny węzeł.
3.5.7. Oblicz wartość f dla nowego węzła i dodaj go do otwartej listy węzłów.

Jeśli otwarta lista węzłów jest pusta, zwróć brak ścieżki.

Powtórz kroki 3-4 aż do znalezienia celu lub osiągnięcia maksymalnej wartości f_max.
'''


def aStar(puzzles, puzzlesAnswer, metrics, positionDict):
    startTime = time.time()
    statesVisited = 0
    maxDepth = 0
    queue = Queue()
    visited = set()
    visited.add(str(puzzles))

    statesVisited = statesVisited + 1
    #brzydko, ale brak lepszego pomysłu przy zachowanym DRY

    if metrics == "manh":
        cost = manhattan(puzzles,positionDict)
    else:
        cost = hamming(puzzles,puzzlesAnswer)

    pozX, pozY = setStart(puzzles)
    possibilities = checkpossibilities(puzzles, pozX, pozY)
    path = ""

    if checkPuzzles(puzzles, puzzlesAnswer):
        print("\ttime: " + str(path))
        print("\tlength: " + str(len(path)))
        print("\ttime: " + str(time.time() - startTime))
        return path, statesVisited + queue.size(),statesVisited, maxDepth + 1, time.time() - startTime

    for i in range(len(possibilities)):
        entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]), copy.copy(path), copy.copy(cost)]
        queue.enqueue(entry)

    queue.items.sort(key=lambda x: x[3])

    while queue.isEmpty() != True:

        queue.items.sort(key=lambda x: x[3])
        entry = queue.dequeue()
        puzzles = entry[0]
        wayToGo = entry[1]
        path = entry[2]
        cost = entry[3]

        pozX, pozY = setStart(puzzles)

        # print("------------------")
        # print("wczytane wartości:")
        # print(puzzles)
        # print("ruch: " + str(wayToGo))
        # print("odwiedzone" + str(visited))

        puzzles = switchPositions(wayToGo, pozX, pozY, puzzles)

        if str(puzzles) in visited:
            continue
        path = str(path) + wayToGo

        if checkPuzzles(puzzles, puzzlesAnswer):
            print("\ttime: " + str(path))
            print("\tlength: " + str(len(path)))
            print("\ttime: " + str(time.time() - startTime))
            statesVisited = len(visited)
            #przetworzone = visited + dlugosc kolejki
            return path, statesVisited + queue.size(),statesVisited, maxDepth + 1, time.time() - startTime

        if metrics == "manh":
            cost = manhattan(puzzles, positionDict)
        else:
            cost = hamming(puzzles, puzzlesAnswer)

        pozX, pozY = setStart(puzzles)
        possibilities = checkpossibilities(puzzles, pozX, pozY)

        if len(path) > maxDepth:
            maxDepth = len(path)

        # print("ścieżka: " + str(path))
        # print("koszt: " + str(cost))
        # print("po zmianie: " + str(puzzles))
        # print("możliwości: " + str(possibilities))

        visited.add(str(puzzles))

        for i in range(len(possibilities)):
            entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]), copy.copy(path), copy.copy(cost)]
            queue.enqueue(entry)
        # queue.items.sort(key=lambda x: x[3])

    return -1, statesVisited + queue.size(),statesVisited, maxDepth + 1, time.time() - startTime

def hamming(puzzles, puzzlesAnswer):
    cost = 0

    for i in range(len(puzzles)):
        for j in range(len(puzzles[0])):
            if puzzles[i][j] != puzzlesAnswer[i][j]:
                cost = cost+1

    return cost

def manhattan(puzzles, positionDict):
    cost = 0

    for i in range(len(puzzles)):
        for j in range(len(puzzles[0])):
            value = int(puzzles[i][j])
            if value != 0:
                correct_x, correct_y = positionDict[value]
                cost += abs(i - correct_x) + abs(j - correct_y)

    return cost

def saveAStarAnswerInfo(fileName, path, statesVisited,statesProcessed,maxDepth, time, metrics):
    '''
1 linia (liczba całkowita): długość znalezionego rozwiązania - o takiej samej wartości jak w pliku z rozwiązaniem (przy czym gdy program nie znalazł rozwiązania, wartość ta to -1);
2 linia (liczba całkowita): liczbę stanów odwiedzonych;
3 linia (liczba całkowita): liczbę stanów przetworzonych;
4 linia (liczba całkowita): maksymalną osiągniętą głębokość rekursji;
5 linia (liczba rzeczywista z dokładnością do 3 miejsc po przecinku): czas trwania procesu obliczeniowego w milisekundach.
    '''

    with open("./puzzlesAnswers/" + fileName + "_a" + metrics + "_sol_info" + ".txt", "w") as file:
        if path != -1:
            strings = [str(len(path)), str(statesVisited), str(statesProcessed), str(maxDepth), str(time)]
        else:
            strings = ["-1", str(statesVisited), str(statesProcessed), str(maxDepth), str(time)]

        file.writelines([s + "\n" for s in strings])
    return 0

def saveAStarAnswer(fileName, path , metrics):

    '''
    1 linia (liczba całkowita): długość roziwązania
    2 linia (permutacja roziwązania):
    '''

    with open("./puzzlesAnswers/" +fileName + "_a" + metrics + "_sol" + ".txt", "w") as file:
        if path != -1:
            strings = [str(len(path)), str(path)]
            file.writelines([s + "\n" for s in strings])
        else:
            file.writelines("-1")
    return 0

def doAStar(fileName,puzzlesAnswer,metrics):

    positionDict = {}
    for i in range(len(puzzlesAnswer)):
        for j in range(len(puzzlesAnswer[0])):
            positionDict[int(puzzlesAnswer[i][j])] = (i, j)

    path, statesVisited,statesProcessed, maxDepth, time = aStar(loadPuzzles(fileName), puzzlesAnswer,metrics,positionDict)
    time = round(time, 3)
    saveAStarAnswer(fileName, path,metrics)
    saveAStarAnswerInfo(fileName, path, statesVisited,statesProcessed, maxDepth, time,metrics)

    return 0

def doFullAStar(fileName,puzzlesAnswer):
    doAStar(fileName,puzzlesAnswer,"hamm")
    doAStar(fileName,puzzlesAnswer,"manh")
    return 0