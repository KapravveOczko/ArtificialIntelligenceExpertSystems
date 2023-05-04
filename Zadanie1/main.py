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



# program:

puzzlesAnswer = puzzlesAnswer4x4
fileName = "4x4_07_00002"
# doDfs(fileName,puzzlesAnswer)
doBfs(fileName,puzzlesAnswer)
doFullAStar(fileName,puzzlesAnswer)