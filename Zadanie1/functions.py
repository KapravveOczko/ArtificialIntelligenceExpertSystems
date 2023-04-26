import numpy as np


def loadPuzzles(fileName):
    fileName = "./puzzles/" + fileName + ".txt"

    with open(fileName, 'r') as file:
        content = file.read()
        content = content.replace(" ","")
        content = content.replace("\n", "")

    return content

def loadToArray(content):
    w = int(content[0])  # Konwersja na liczbę całkowitą
    k = int(content[1])  # Konwersja na liczbę całkowitą
    content = content[2:]

    content = np.array(list(content))  # Konwersja na listę znaków, a następnie na tablicę NumPy

    puzzle = content.reshape((w, k))  # Poprawienie kodu na podstawie wczytanych w i k

    return puzzle

def printPuzzles(puzzle):
    print(puzzle)
    return 0

def checkPuzzles(A, B):
    result = True
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != B[i][j]:
                result = False
                break

    print(result)
    return result