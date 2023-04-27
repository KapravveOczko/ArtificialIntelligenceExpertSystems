from functions import *
from bfs import *

print("hello world")

# puzzles = loadToArray(loadPuzzles("2x2_01_00002"))
# pozX, pozY = setStart(puzzles)
# print("x " + str(pozX))
# print("y " + str(pozY))
# # print(checkpossibilities(puzzles,pozX,pozY))
# printPuzzles(puzzles)
# puzzles[pozY][pozX] = 5
# printPuzzles(puzzles)


#sprawdzamy jak działa kolejka
# puzzles = loadToArray(loadPuzzles("2x2_01_00001"))
# from queue import *
# queue = Queue()
#
# entry = [puzzles, "L"]
# print(entry)
# queue.enqueue(entry)
#
# entry = [puzzles,"D"]
# print(entry)
# queue.enqueue(entry)
#
# entry = queue.dequeue()
# print(entry)
#
# entry = queue.dequeue()
# print(entry)


puzzles = loadToArray(loadPuzzles("2x2_01_00002"))
puzzlesAnswer = [['1','2'],['3','0']]
print(bfs(puzzles,puzzlesAnswer))