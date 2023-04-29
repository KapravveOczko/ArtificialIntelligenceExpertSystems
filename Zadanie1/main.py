from functions import *
from bfs import *

print("hello world")

# # puzzlesAnswer = [['1','2'],['3','0']]
# puzzlesAnswer = [['1','2','3'],['4','5','6'],['7','8','0']]
# # puzzlesAnswer = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]
# print(bfs(puzzles,puzzlesAnswer))

puzzles = loadPuzzles2("4x4_06_00007")
puzzlesAnswer = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]
print(len(puzzles))
print(len(puzzles[0]))
x,y = setStart(puzzles)

print(x)
print(y)
print(bfs(puzzles,puzzlesAnswer))

