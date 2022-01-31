"""
Author: TRAORE Souleman

Date: 24.01.2022

Contains Saving and uploading the game grid.

"""

SAVE_FILE = r'./src/'

test_grid = [['.', '.', '.', '.'],
             ['X', 'X', '.', 'O'], 
             ['X', '.', 'O', '.'],
             ['X', 'O', '.', 'O']]

def saveFile(gridArray, gridSize):
    with open("src/save.txt", 'w') as f:
        for i in range(gridSize):
            for j in range(gridSize):
                f.write(gridArray[i][j]+',')
            f.write('\n')

#saveFile(test_grid, 4)

def uploadFile(filename):
    with open(filename,'r') as f:
        result_grid = []
        for i in f: 
            row = i.split(',')
            result_grid.append(row[0:-1])
        return result_grid

#print(uploadFile("src/save.txt"))