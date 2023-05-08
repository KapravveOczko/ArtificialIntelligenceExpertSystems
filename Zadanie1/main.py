from functions import *
from bfs import *
from dfs import *
from aStar import *

print("hello world")

puzzlesAnswer2x2 = [['1','2'],['3','0']]
puzzlesAnswer3x3 = [['1','2','3'],['4','5','6'],['7','8','0']]
puzzlesAnswer4x4 = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]

puzzlesAnswer = puzzlesAnswer4x4
fileName = "4x4_07_00208"
permutaction = ["RDUL","RDLU","DRUL","DRLU","LUDR","LURD","ULDR","ULRD"]

for i in range(len(permutaction)):
#     print("===============================")
#     print("\t\t+------+")
#     print( "\t\t| " + str(permutaction[i]) + " |")
#     print("\t\t+------+")
#     print()
#     print("BFS:")
#     doBfs(fileName,puzzlesAnswer,permutaction[i])
    print()
    print(""
          "DFS:")
    doDfs(fileName, puzzlesAnswer,permutaction[i])

# print("\t\t+------+")
# print( "\t\t| " + "ASTR" + " |")
# print("\t\t+------+")
# print()
# print("HAMM:")
# doAStar(fileName, puzzlesAnswer, "hamm")
# print()
# print("MANH:")
# doAStar(fileName, puzzlesAnswer, "manh")

# doDfs(fileName, puzzlesAnswer, "RLUD")
# program:

# puzzlesAnswer = puzzlesAnswer4x4
# fileName = "4x4_07_00107"
# permutaction = "ULRD"
# doDfs(fileName,puzzlesAnswer)
# doBfs(fileName,puzzlesAnswer)
# doFullAStar(fileName,puzzlesAnswer)