from functions import *
from bfs import *

print("hello world")

puzzles = loadToArray(loadPuzzles("2x2_01_00001"))
x,y = setStart(puzzles)
print("x: ", str(x))
print("y: ", str(y))
checkpossibilities(puzzles,x,y)