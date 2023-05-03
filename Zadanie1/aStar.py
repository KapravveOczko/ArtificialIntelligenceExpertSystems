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

def aStar(puzzles, puzzlesAnswer,metrics):

    if checkPuzzles(puzzles, puzzlesAnswer):
        return True

    queueOpen = Queue()
    visited = []
    visited.append(copy.deepcopy(puzzles))
    cost = metrics
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
        print("odwiedzone" + str(visited))

        puzzles = switchPositions(wayToGo, pozX, pozY, puzzles)
        if puzzles in visited:
            continue
        if checkPuzzles(puzzles, puzzlesAnswer):
            print("ścierzka: " + str(path))
            print("po zmianie: " + str(puzzles))
            return True

        path = str(path) + wayToGo
        cost = metrics
        pozX, pozY = setStart(puzzles)
        possibilities = checkpossibilities(puzzles, pozX, pozY)

        print("ścierzka: " + str(path))
        print("koszt: "+ str(cost))
        print("po zmianie: " + str(puzzles))
        print("możliwości: " + str(possibilities))

        # visited.append(copy.deepcopy(puzzles))
        #dodanie tej linijki wszystko psuje

        for i in range(len(possibilities)):
            entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]), copy.copy(path),copy.copy(cost), copy.copy(visited)]
            queueOpen.enqueue(entry)
        queueOpen.items.sort(key=lambda x: x[4])


    return -1

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
