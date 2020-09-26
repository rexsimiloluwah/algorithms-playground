import numpy as np 
import math
import sys

def generate_random_grid(x = 9, y = 9):
    """
        DESC : This function returns a square grid of dimensions (x, y) i.e. x-rows and y-columns
    """

    assert x == y, "x must be equal to y for a square grid !"
    assert x > 0 and y > 0, "x and y must be greater than 0 !"

    grid = np.zeros((x,y))
    param_space = list(range(1,10))
    for i in range(9):
        num = param_space[np.random.randint(low = 0, high = len(param_space))]
        param_space.pop(param_space.index(num))
        grid[i, i] = num
        
    return grid


def check_constraints(row,col, n):
    """
        DESC : This helper function checks all the constraints for the sudoku puzzle i.e. 
        all numbers between [1,9] must be in each row, column and square of the puzzle unrepeated.

        x (int) -> x-position of the cell in the puzzle
        y (int) -> y-position of the cell in the puzzle
        n (int) -> Number to be checked
    """
    global grid

    for i in range(9):
        # Checks the constraint for the row
        if (grid[row, i] == n) and (col != i):
            return False

    for i in range(9):
        # Checks the constraint for the column
        if (grid[i, col] == n) and (row != i):
            return False

    # Checking the constraint for the square

    row0 = (row // 3) * 3
    col0 = (col // 3) * 3

    for i in range(row0, row0 + 3):
        for j in range(col0, col0 + 3):
            if (grid[i, j] == n) and ( (row,col) != (i,j)):
                return False


    return True

def find_empty_cell():
    global grid

    for row in range(9):
        for col in range(9):
            if grid[row, col] == 0:
                return row, col
    return None

    
def solve(grid):

    """
        DESC : This function basically solves the sudoku puzzle using all the constraints and a back-tracking algorithm (CREDITS :- ComputerPhile, TechWithTim)
    """

    empty = find_empty_cell()
    if not empty:
        return True
    else:
        (row, col) = empty

    for i in range(1,10):
        if check_constraints(row, col, i):
            grid[row, col] = i
            
            if solve(grid):
                return True
                
            grid[row][col] = 0

    return False

# grid = generate_random_grid(9,9)

def print_puzzle(grid):
    """
        DESC : This function prints out the sudoku puzzle
    """
    for i in range(len(grid)):
        print("-"*34)
        for j in range(len(grid)):
            if j < 8:
                print(grid[i,j], end = " | ")

            if j == 8:
                print(grid[i,j], end= "\n")
    print("-"*34)
            
    


if __name__ == "__main__":
    grid = np.array([
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    
    ])
    
    print_puzzle(grid)
    # # print(check_constraints(2,2,8))
    print(solve(grid))
    print_puzzle(grid)

