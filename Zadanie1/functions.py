import numpy as np

def  loadPuzzles2(fileName):
    fileName = "./puzzles/" + fileName + ".txt"
    with open(fileName, 'r') as file:
        content = file.read()
        content = content.replace("\n", " ")
        print (content)

        w = int(content[0])  # Konwersja na liczbę całkowitą
        k = int(content[2])  # Konwersja na liczbę całkowitą
        content = content[4:]

        print(content)

        array = []
        for i in content.split():
            array.append(int(i))
        puzzle = [array[i:i + w] for i in range(0, len(array), k)]

        for i in range(w):
            for j in range(k):
                puzzle[i][j] = str(puzzle[i][j])
                puzzle[i][j] = puzzle[i][j].replace(" ","")

        print(puzzle)

    return puzzle
'''
:return True if puzzles are equal
:return False if puzzles not equal
'''
def checkPuzzles(A, B):
    result = True
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != B[i][j]:
                result = False
                break

    #print(result)
    return result