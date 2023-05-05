from functions import *
from bfs import *
from dfs import *
from aStar import *

print("hello world")

puzzlesAnswer2x2 = [['1','2'],['3','0']]
puzzlesAnswer3x3 = [['1','2','3'],['4','5','6'],['7','8','0']]
puzzlesAnswer4x4 = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]
# print(bfs(puzzles,puzzlesAnswer))

#test dla bfs

# fileName = "4x4_07_00071"
# puzzles = loadPuzzles2(fileName)
# puzzlesAnswer = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]
# print(len(puzzles))
# print(len(puzzles[0]))
# x,y = setStart(puzzles)
#
# print(x)
# print(y)
# visited,iter,time = bfs(puzzles,puzzlesAnswer)
# time = round(time, 3)
# saveAnswer(fileName,visited)
# saveAnswerInfo(fileName,visited,iter,time)

#test dla dfs

# puzzles = loadPuzzles(fileName)
# puzzlesAnswer = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]
# print(len(puzzles))
# print(len(puzzles[0]))
# x,y = setStart(puzzles)
#
# print(x)
# print(y)
#
# print(dfs(puzzles,puzzlesAnswer))

#test aStar

# fileName = "4x4_07_00001"
# puzzlesAnswer = puzzlesAnswer4x4
# puzzles = loadPuzzles(fileName)
# print("hamming: " + str(hamming(puzzles,puzzlesAnswer)))
# print("manhattan: " + str(manhattan(puzzles,puzzlesAnswer)))
# print("==================================")
# print(puzzles)
# print(aStar(puzzles,puzzlesAnswer,manhattan(puzzles, puzzlesAnswer)))

#test

# puzzlesAnswer = puzzlesAnswer4x4
# fileName = "4x4_07_00006"
# puzzles = loadPuzzles(fileName)
# x,y = setStart(puzzles)
# print(checkpossibilities(puzzles,x,y,"L"))

#test sort permutaction

puzzlesAnswer = puzzlesAnswer4x4
fileName = "4x4_07_00197"
permutaction = ["RDUL","RDLU","DRUL","DRLU","LUDR","LURD","ULDR","ULRD"]

for i in range(len(permutaction)):
    print("===============================")
    print("\t\t+------+")
    print( "\t\t| " + str(permutaction[i]) + " |")
    print("\t\t+------+")
    print()
    print("BFS:")
    doBfs(fileName,puzzlesAnswer,permutaction[i])
    print()
    print("DFS:")
    doDfs(fileName, puzzlesAnswer,permutaction[i])

print("\t\t+------+")
print( "\t\t| " + "ASTR" + " |")
print("\t\t+------+")
print()
print("HAMM:")
doAStar(fileName, puzzlesAnswer, "hamm")
print()
print("MANH:")
doAStar(fileName, puzzlesAnswer, "manh")


# program:

# puzzlesAnswer = puzzlesAnswer4x4
# fileName = "4x4_07_00107"
# permutaction = "ULRD"
# doDfs(fileName,puzzlesAnswer)
# doBfs(fileName,puzzlesAnswer)
# doFullAStar(fileName,puzzlesAnswer)