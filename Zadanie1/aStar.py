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

def aStar(puzzles, puzzlesAnswer):

    if checkPuzzles(puzzles, puzzlesAnswer):
        return True

    queueOpen = Queue()
    visited = []
    visited.append(copy.deepcopy(puzzles))
    cost = hamming(puzzles, puzzlesAnswer)
    pozX, pozY = setStart(puzzles)
    possibilities = checkpossibilities(puzzles, pozX, pozY)
    path = ""

    for i in range(len(possibilities)):
        entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]), copy.copy(path), copy.copy(cost), copy.copy(visited)]
        queueOpen.enqueue(entry)

    queueOpen.items.sort(key=lambda x: x[4])

    while queueOpen.isEmpty != True:

        entry = queueOpen.dequeue()
        puzzles = entry[0]
        wayToGo = entry[1]
        path = entry[2]
        #cost = entry[3]
        visited = entry[4]

        pozX, pozY = setStart(puzzles)

        print("------------------")
        print("wczytane wartości:")
        print(puzzles)
        print("ruch: " + str(wayToGo))

        puzzles = switchPositions(wayToGo, pozX, pozY, puzzles)
        if puzzles in visited:
            continue
        if checkPuzzles(puzzles, puzzlesAnswer):
            print("ścierzka: " + str(path))
            print("po zmianie: " + str(puzzles))
            return True

        path = str(path) + wayToGo
        cost = hamming(puzzles, puzzlesAnswer)
        pozX, pozY = setStart(puzzles)
        possibilities = checkpossibilities(puzzles, pozX, pozY)

        print("ścierzka: " + str(path))
        print("koszt: "+ str(cost))
        print("po zmianie: " + str(puzzles))
        print("możliwości: " + str(possibilities))


        for i in range(len(possibilities)):
            entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]), copy.copy(path),copy.copy(cost), copy.copy(visited)]
            queueOpen.enqueue(entry)
        queueOpen.items.sort(key=lambda x: x[4])


    return -1

# def aStarTest2(puzzles, puzzlesAnswer):
#
#     startTime = time.time()
#     last = None
#     queue = Queue()
#     pozX, pozY = setStart(puzzles)
#     possibilities = checkpossibilities(puzzles, pozX, pozY)
#     visited = ""
#     statesVisited = 1
#     hValue = hamming(puzzles, puzzlesAnswer)
#
#     if checkPuzzles(puzzles, puzzlesAnswer):
#         endTime = time.time()
#         return visited, statesVisited, endTime - startTime
#
#     queue.enqueue([copy.deepcopy(puzzles), "", copy.copy(visited), hValue])
#
#     while not queue.isEmpty():
#
#         entry = queue.dequeue()
#         puzzles = entry[0]
#         wayToGo = entry[1]
#         visited = entry[2]
#         fValue = len(visited) + entry[3]
#
#         statesVisited += 1
#         pozX, pozY = setStart(puzzles)
#
#         if checkPuzzles(puzzles, puzzlesAnswer):
#             endTime = time.time()
#             return visited, statesVisited, endTime - startTime
#
#         for i in range(len(possibilities)):
#             if last == checkOpposite(possibilities[i]):
#                 continue
#             #pozX, pozY = setStart(puzzles)
#             newPuzzles = copy.deepcopy(puzzles)
#             newVisited = copy.copy(visited)
#             newPuzzles = switchPositions(possibilities[i], pozX, pozY, newPuzzles)
#             newVisited += possibilities[i]
#             hValue = hamming(newPuzzles, puzzlesAnswer)
#             fValue = len(newVisited) + hValue
#             queue.enqueue([newPuzzles, possibilities[i], newVisited, hValue, fValue])
#
#         queue.items.sort(key=lambda x: x[4])
#
#     endTime = time.time()
#     return -1, statesVisited, endTime - startTime

def hamming(puzzles, puzzlesAnswer):
    cost = 0

    for i in range(len(puzzles)):
        for j in range(len(puzzles[0])):
            if puzzles[i][j] != puzzlesAnswer[i][j]:
                cost = cost+1

    return cost

def manhattan(puzzles, puzzlesAnswer):
    cost = 0
    puzzlesX,puzzlesY,puzzlesAnswerX,puzzlesAnswerY = 0,0,0,0

    for a in range(len(puzzles)* len(puzzles[0])):
        for i in range(len(puzzles)):
            for j in range(len(puzzles[0])):
                if puzzles[i][j] == str(a):
                    puzzlesX = j
                    puzzlesY = i
                if puzzlesAnswer[i][j] == str(a):
                    puzzlesAnswerX = j
                    puzzlesAnswerY = i
        cost = cost + abs(puzzlesX - puzzlesAnswerX) + abs(puzzlesY - puzzlesAnswerY)
        # print("a: " + str(a) + " cost: " + str(cost))

    return cost

# def checkOpposite(last):
#     if last == "U":
#         last = "D"
#     if last == "D":
#         last = "U"
#     if last == "L":
#         last = "R"
#     if last == "R":
#         last = "L"
#
#     return last