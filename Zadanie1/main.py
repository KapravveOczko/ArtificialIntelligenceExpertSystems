from functions import *
from bfs import *

print("hello world")

# # puzzlesAnswer = [['1','2'],['3','0']]
# puzzlesAnswer = [['1','2','3'],['4','5','6'],['7','8','0']]
# # puzzlesAnswer = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]
# print(bfs(puzzles,puzzlesAnswer))

fileName = "4x4_06_00007"
puzzles = loadPuzzles2(fileName)
puzzlesAnswer = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]
print(len(puzzles))
print(len(puzzles[0]))
x,y = setStart(puzzles)

print(x)
print(y)
visited,iter,time = bfs(puzzles,puzzlesAnswer)
time = time * -1
time = round(time, 3)
saveAnswer(fileName,visited)
saveAnswerInfo(fileName,visited,iter,time)

