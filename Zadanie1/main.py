from functions import *
from bfs import *
from dfs import *
from aStar import *

print("hello world")


puzzlesAnswer2x2 = [['1','2'],['3','0']]
puzzlesAnswer3x3 = [['1','2','3'],['4','5','6'],['7','8','0']]
puzzlesAnswer4x4 = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]
puzzlesAnswer = puzzlesAnswer4x4

positionDict = {}
for i in range(len(puzzlesAnswer)):
    for j in range(len(puzzlesAnswer[0])):
        positionDict[int(puzzlesAnswer[i][j])] = (i, j)


""""""

# algorytm + głębokość + wartośćmierzona + permutacja/metryka



""""""

fileNameStart = "4x4_0"
fileNameDepth = 0
fileNameNumber = 1
numberOfPuzzles = [2,4,10,24,54,107,212]
buffer = ""


for i in range(7):
    fileNameDepth = fileNameDepth + 1
    for j in range(numberOfPuzzles[i]):
        fileNameNumber = j+1

        if fileNameNumber < 10:
            buffer = "0"
        elif fileNameNumber < 100:
            buffer = ""
        else:
            buffer = ""

        fileName = fileNameStart + str(fileNameDepth) + "_000" + buffer + str(fileNameNumber)
        print(fileName)

        permutaction = ["RDUL","RDLU","DRUL","DRLU","LUDR","LURD","ULDR","ULRD"]

        for c in range(len(permutaction)):
            print("===============================")
            print("\t\t+------+")
            print( "\t\t| " + str(permutaction[i]) + " |")
            print("\t\t+------+")
            print()
            print("BFS:")
            lengthBFS,visitedBFS,processedBFS,maxDepthBFS,timeBFS = bfs(loadPuzzles(fileName),puzzlesAnswer,permutaction[c])
            print()
            print("DFS:")
            lengthDFS,visitedDFS,processedDFS,maxDepthDFS,timeDFS = dfs(loadPuzzles(fileName),puzzlesAnswer,permutaction[c])

        print("\t\t+------+")
        print( "\t\t| " + "ASTR" + " |")
        print("\t\t+------+")
        print()
        print("HAMM:")
        lengthHAMM,visitedHAMM,processedHAMM,maxDepthHAMM,timeHAMM = aStar(loadPuzzles(fileName), puzzlesAnswer,"hamm",positionDict)
        print()
        print("MANH:")
        lengthMANH,visitedMANH,processedMANH,maxDepthMANH,timeMANH = aStar(loadPuzzles(fileName), puzzlesAnswer,"manh",positionDict)


# fileName = "4x4_01_00001"
# permutaction = ["RDUL","RDLU","DRUL","DRLU","LUDR","LURD","ULDR","ULRD"]
#
# for i in range(len(permutaction)):
#     print("===============================")
#     print("\t\t+------+")
#     print( "\t\t| " + str(permutaction[i]) + " |")
#     print("\t\t+------+")
#     print()
#     print("BFS:")
#     doBfs(fileName,puzzlesAnswer,permutaction[i])
#     print()
#     print("DFS:")
#     doDfs(fileName, puzzlesAnswer,permutaction[i])
#
# print("\t\t+------+")
# print( "\t\t| " + "ASTR" + " |")
# print("\t\t+------+")
# print()
# print("HAMM:")
# doAStar(fileName, puzzlesAnswer, "hamm")
# print()
# print("MANH:")
# doAStar(fileName, puzzlesAnswer, "manh")

# program:

# puzzlesAnswer = puzzlesAnswer4x4
# fileName = "4x4_07_00107"
# permutaction = "ULRD"
# doDfs(fileName,puzzlesAnswer)
# doBfs(fileName,puzzlesAnswer)
# doFullAStar(fileName,puzzlesAnswer)

