# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 11:23:46 2020

@author: NVSD
"""


#to find empty value in the sudokugrid
def unassignedValue(sudokuarray):
    for row in range(9):
        for col in range(9):
            if sudokuarray[row][col] == 0:
                return row,col
    return -1,-1


def isSafe(num,row,col):
    if num in sudokuGrid[row]:#checking row
        return False
    for row_i in range(9):
        if num == sudokuGrid[row_i][col]:#checking in column
            return False
    #checking in 3X3 grid
    gridRow = row%3
    gridCol = col%3
    baseGridRow = row-gridRow
    baseGridCol = col-gridCol
    subgrid = []
    for i in range(3):
        for j in range(3):
            subgrid.append(sudokuGrid[baseGridRow+i][baseGridCol+j])
    if num in subgrid:
        return False
    return True

#main solving function using backtrack algorithm
def sudokusolver(sudokuGrid):
    r,c = unassignedValue(sudokuGrid)
    if r == -1 and c == -1:
        return True
    
    for i in range(1,10):
        if (isSafe(i,r,c)):
            sudokuGrid[r][c] = i
            if sudokusolver(sudokuGrid):
                return True
            sudokuGrid[r][c] = 0
    return False

if __name__ == "__main__":
    #input sudoku grid here
    sudokuGrid = [[0,0,0,0,0,0,2,0,0],
                  [0,8,0,0,0,7,0,9,0],
                  [6,0,2,0,0,0,5,0,0],
                  [0,7,0,0,6,0,0,0,0],
                  [0,0,0,9,0,1,0,0,0],
                  [0,0,0,0,2,0,0,4,0],
                  [0,0,5,0,0,0,6,0,3],
                  [0,9,0,4,0,0,0,7,0],
                  [0,0,6,0,0,0,0,0,0]]
    if (sudokusolver(sudokuGrid)):
        for i in sudokuGrid:
            print(i)
    else:
        print("The given sudoku is not solvable")
        
        
    
    
    
    
    