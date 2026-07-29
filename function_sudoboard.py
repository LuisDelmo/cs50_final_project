import numpy as np
from collections import deque
from Node import Node
import math




#check if this: [row, collumn or flatten_quadrant] is valid
def check_this(unit):
        set_unit = set()
        for cell in unit:
            if cell != 0 and cell in set_unit:
                return False
            set_unit.add(cell)
        return True

#check if this cell is valid using the check_this function
def check_cell_board(coords,board):
        y,x = coords
        row = board[y,:]
        column = board[:,x]
        #quadrant giga elegant logic
        qindexy = (y // 3) * 3
        qindexx = (x // 3) * 3
        quadrant = board[qindexy:qindexy+3,qindexx:qindexx+3].flatten()

        if not all([check_this(row),check_this(column),check_this(quadrant)]):
                return False
        return True


#function to return possible nums in this cell TODO remember to give set possible num to it
possiblenum = set(range(1,10))
def check_possiblenums(coords,board,possiblenum):
        value_num = board[coords]
        possible = []

        for num in set(range(1,10)):
            if num != value_num:
                board[coords] = num
                if check_cell_board(board=board,coords=(coords)):
                    possible.append(num)
                board[coords] = value_num
        if possible:
            return possible
        return None

#function to find best cell to try and solve
def heuristic_function(board):
    #3 cases possible hueristic
    # no num in board
    # invalid board




easy_puzzle = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])
