from functions import *
from stack import *
import copy
import time

'''
kolejka stanów odwiedzonych

    sprawdzamy stan
    sprawdzamy możliwości poruszenia się z aktualnego stanu
    dodajemy te stany do stosu (kolejka lifo)
    dodajemy do nich tablice odwiedzonych stanów
    
'''

def dfs(puzzles, puzzlesAnswer):

    """
    inicjujemy potrzebne wartości:
    startTime: czas rozpoczęcia działania programu
    stack: inicjalizacja kolejki lifo
    pozX,pozY: pozycja 0
    possibilities: możliwe przesunięcia
    visited: lista odwiedzonych stanów
    dodajemy do listy visited stan początkowy
    path: wykonane ruchy
    statesVisited: zlicza ile stanów odiwedziliśmy
    maxDepth: maksymalna przeszukana głębokość
    """

    startTime = time.time()
    stack = Stack()
    pozX, pozY = setStart(puzzles)
    possibilities = checkpossibilities(puzzles, pozX, pozY)
    visited = set()
    visited.add(str(puzzles))
    path = ''
    statesVisited = 0
    maxDepth = 0 #trzeba dodać 1 na końcu bo stan początkowy

    """
    sprawdzamy czy stan początkowy to stan poszukiwany
    wypełniamy stos możliwymi ruchami
    entry: aktualny stan łamigłówki, ruch do wykonania, liesta stanów odwiedzonych,lista wykonanych już ruchów
    """

    if checkPuzzles(puzzles, puzzlesAnswer):
        return path, statesVisited, maxDepth + 1, time.time() - startTime
    for i in range(len(possibilities)):
        entry = [copy.deepcopy(puzzles), copy.copy(possibilities[i]), copy.deepcopy(visited), copy.copy(path)]
        stack.push(entry)

    """
       rozpoczyna się pętla wykonywana tak długo jak stos nie jest pusty

       pop'ujemy stos wpełniając zmienne
       iterujemy ilość odwiedzonych stanów
       ustanawiamy nowe pozycje x,y
       dodajemy wykonany ruch do listy wykonaych ruchów
       sprawdzamy osiągniętą głębokość
       wykonujemy ruch 
       sprawdzamy czy nowy stan był już osiągnięty oraz czy jest rozwiązaniem
           jeśli tak tu konczy się funkcja, jej czas trwania jest pobierany przez zmienną endTime
       ustanawiamy nowe pozycje x,y
       dodajemy do stan do kolejki odwiedzonej
       wypełniamy stos możliwymi ruchami

       """

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
        if str(puzzles) in visited:
            continue
        if checkPuzzles(puzzles, puzzlesAnswer):
            return path, statesVisited,  maxDepth + 1, time.time() - startTime

        pozX, pozY = setStart(puzzles)
        visited.add(str(puzzles))
        possibilities = checkpossibilities(puzzles, pozX, pozY)
        if len(visited) == 20:
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