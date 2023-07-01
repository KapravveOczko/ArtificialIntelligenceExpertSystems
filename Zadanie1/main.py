from functions import *
from bfs import *
from dfs import *
from aStar import *

print("hello world")


puzzlesAnswer2x2 = [['1','2'],['3','0']]
puzzlesAnswer3x3 = [['1','2','3'],['4','5','6'],['7','8','0']]
puzzlesAnswer4x4 = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]
puzzlesAnswer = puzzlesAnswer4x4
#
#
# import csv
# import copy
#
# positionDict = {}
# for i in range(len(puzzlesAnswer)):
#     for j in range(len(puzzlesAnswer[0])):
#         positionDict[int(puzzlesAnswer[i][j])] = (i, j)
#
#
# """"""
#
# # permutacja/metryka + głębokość + wartośćmierzona
# answersBFS = []
# answersDFS = []
# answersAHAMM = []
# answersAMANH = []
# permutation = ["RDUL","RDLU","DRUL","DRLU","LUDR","LURD","ULDR","ULRD"]
#
# for j in range(7):
#     depth = j + 1
#     entry = ["hamm",depth, 0, 0, 0, 0, 0]
#     answersAHAMM.append(copy.copy(entry))
#     entry = ["manh",depth, 0, 0, 0, 0, 0]
#     answersAMANH.append(copy.copy(entry))
#     for i in range(len(permutation)):
#         entry = [permutation[i], depth, 0, 0, 0, 0, 0]
#         answersBFS.append(copy.copy(entry))
#         answersDFS.append(copy.copy(entry))
#
# print(len(answersBFS))
# print(answersDFS)
# print(answersAHAMM)
# print(answersAMANH)
#
# """"""
#
# fileNameStart = "4x4_0"
# fileNameDepth = 0
# fileNameNumber = 1
# numberOfPuzzles = [2,4,10,24,54,107,212]
# buffer = ""
# x = 0
#
# for i in range(7):
#     fileNameDepth = fileNameDepth + 1
#     for j in range(numberOfPuzzles[i]):
#         fileNameNumber = j+1
#
#
#         if fileNameNumber < 10:
#             buffer = "00"
#         elif fileNameNumber < 100:
#             buffer = "0"
#         else:
#             buffer = ""
#
#         fileName = fileNameStart + str(fileNameDepth) + "_00" + buffer + str(fileNameNumber)
#         if i ==0:
#             x = 0
#         else:
#             x = i * 7 + i
#
#         permutaction = ["RDUL","RDLU","DRUL","DRLU","LUDR","LURD","ULDR","ULRD"]
#
#         for c in range(len(permutaction)):
#             print("===============================")
#             print("\t\t+------+")
#             print( "\t\t| " + str(permutaction[i]) + " |")
#             print("\t\t+------+")
#             print()
#             print("BFS:")
#             print(x)
#             lengthBFS,visitedBFS,processedBFS,maxDepthBFS,timeBFS = bfs(loadPuzzles(fileName),puzzlesAnswer,permutaction[c])
#             answersBFS[x][2] = answersBFS[x][2] + len(lengthBFS)
#             answersBFS[x][3] = answersBFS[x][3] + visitedBFS
#             answersBFS[x][4] = answersBFS[x][4] + processedBFS
#             answersBFS[x][5] = answersBFS[x][5] + maxDepthBFS
#             answersBFS[x][6] = answersBFS[x][6] + timeBFS
#             print()
#             print("DFS:")
#             lengthDFS,visitedDFS,processedDFS,maxDepthDFS,timeDFS = dfs(loadPuzzles(fileName),puzzlesAnswer,permutaction[c])
#             answersDFS[x][2] = answersDFS[x][2] + len(lengthDFS)
#             answersDFS[x][3] = answersDFS[x][3] + visitedDFS
#             answersDFS[x][4] = answersDFS[x][4] + processedDFS
#             answersDFS[x][5] = answersDFS[x][5] + maxDepthDFS
#             answersDFS[x][6] = answersDFS[x][6] + timeDFS
#
#             x = x + 1
#
#         print("\t\t+------+")
#         print( "\t\t| " + "ASTR" + " |")
#         print("\t\t+------+")
#         print()
#         print("HAMM:")
#         lengthHAMM,visitedHAMM,processedHAMM,maxDepthHAMM,timeHAMM = aStar(loadPuzzles(fileName), puzzlesAnswer,"hamm",positionDict)
#         answersAHAMM[i][2] = answersAHAMM[i][2] + len(lengthHAMM)
#         answersAHAMM[i][3] = answersAHAMM[i][3] + visitedHAMM
#         answersAHAMM[i][4] = answersAHAMM[i][4] + processedHAMM
#         answersAHAMM[i][5] = answersAHAMM[i][5] + maxDepthHAMM
#         answersAHAMM[i][6] = answersAHAMM[i][6] + timeHAMM
#         print()
#         print("MANH:")
#         lengthMANH,visitedMANH,processedMANH,maxDepthMANH,timeMANH = aStar(loadPuzzles(fileName), puzzlesAnswer,"manh",positionDict)
#         answersAMANH[i][2] = answersAMANH[i][2] + len(lengthMANH)
#         answersAMANH[i][3] = answersAMANH[i][3] + visitedMANH
#         answersAMANH[i][4] = answersAMANH[i][4] + processedMANH
#         answersAMANH[i][5] = answersAMANH[i][5] + maxDepthMANH
#         answersAMANH[i][6] = answersAMANH[i][6] + timeMANH
#
#
# print(answersBFS)
# print(answersDFS)
# print(answersAHAMM)
# print(answersAMANH)
#
# with open('./answers/answers.csv', mode='w', newline='') as file:
#     writerBfs = csv.writer(file, delimiter=';')
#     writerBfs.writerow(['tablica', 'algorytm', 'głębokość', 'długość', 'odwiedzone', 'przetworzone', 'maksymalna głębokość', 'czas (s)'])
#
#     for entry in answersBFS:
#         writerBfs.writerow(['answersBFS', entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]])
#
#     writerDfs = csv.writer(file, delimiter=';')
#     writerDfs.writerow(['tablica', 'algorytm', 'głębokość', 'długość', 'odwiedzone', 'przetworzone', 'maksymalna głębokość', 'czas (s)'])
#
#     for entry in answersDFS:
#         writerDfs.writerow(['answersDFS', entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]])
#
#     writerAhamm = csv.writer(file, delimiter=';')
#     writerAhamm.writerow(['tablica', 'algorytm', 'głębokość', 'długość', 'odwiedzone', 'przetworzone', 'maksymalna głębokość', 'czas (s)'])
#
#     for entry in answersAHAMM:
#         writerAhamm.writerow(['answersAHAMM', entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]])
#
#     writerAmanh = csv.writer(file, delimiter=';')
#     writerAmanh.writerow(['tablica', 'algorytm', 'głębokość', 'długość', 'odwiedzone', 'przetworzone', 'maksymalna głębokość', 'czas (s)'])
#
#     for entry in answersAMANH:
#         writerAmanh.writerow(['answersAMANH', entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]])
#
#
#








#================================================================

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

