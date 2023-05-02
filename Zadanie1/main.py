from functions import *
from bfs import *
from dfs import *

print("hello world")

# # puzzlesAnswer = [['1','2'],['3','0']]
# puzzlesAnswer = [['1','2','3'],['4','5','6'],['7','8','0']]
# # puzzlesAnswer = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]
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
# time = time * -1
# time = round(time, 3)
# saveAnswer(fileName,visited)
# saveAnswerInfo(fileName,visited,iter,time)

#test dla dfs


fileName = "2x2_02_00002"
puzzles = loadPuzzles(fileName)
puzzlesAnswer = [['1','2'],['3','0']]
print(len(puzzles))
print(len(puzzles[0]))
x,y = setStart(puzzles)

print(x)
print(y)

print(dfs(puzzles,puzzlesAnswer))