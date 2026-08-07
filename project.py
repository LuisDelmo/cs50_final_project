import numpy as np
import random
from game import game_loop


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


#function to return possible nums in this cell
def check_possiblenums(coords,board):
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
        return []

#function to find best cell to try and solve
def heuristic_function(board):

    empty_cells = np.argwhere(board == 0)
    if empty_cells.size <= 0:
        is_valid = all(check_cell_board((y,x),board) for y in range(len(board)) for x in range(len(board[y])))
        if is_valid:
            return True, (True,True)
        return False, (False,False)

    min_possible = 100
    possible = None
    coords = None


    for (y,x) in empty_cells:

        possible_this = check_possiblenums((y,x),board)

        if possible_this is not None:
            size_possible = len(possible_this)

            if size_possible == 0:
                #invalid
                return False, (False,False)

            if size_possible < min_possible:
                min_possible = size_possible
                possible = possible_this
                coords = (y,x)

    return possible, coords

def solve(board,solutions=None,fastest=False,calls=None):
        #add a None check valid later
        if solutions is None:
            solutions = []
        possible, coords = heuristic_function(board)

        if len(solutions) >= 2:
            return

        if possible is True:
            c_board = np.copy(board)
            if fastest:
                return c_board
            solutions.append(c_board)
            return
        if possible is False:
            return

        while possible:
            to_check = possible.pop()
            board[coords] = to_check

            board_s = solve(board,solutions,fastest=fastest)
            if fastest and isinstance(board_s,np.ndarray):
                return board_s

            board[coords] = 0

        
        return len(solutions), solutions

def generate_board(name,level=1):
    board = np.zeros((9,9))
    seed_name = random.randint(1,9)
    for char in name:
        seed_name *= ord(char)
    random.seed(seed_name)

    random_coords = (random.randint(0,8),random.randint(0,8))
    random_num = random.randint(1,9)
    board[random_coords] = random_num

    board = solve(board,fastest=True)

    levels_range_map = {1: (32,45),
                        2: (22,30),
                        3: (17,17)}
    a,b = levels_range_map[level]
    n_clues = random.randint(a,b)
    to_hide = 81 - n_clues
    random.seed(seed_name+n_clues-random_num)
    coords = [(x, y) for x in range(9) for y in range(9)]

    hidden = 0
    while True:
        
        if hidden >= to_hide:
            return board
        random.shuffle(coords)
        coords_hide = coords.pop()

        prev_num = board[coords_hide]
        board[coords_hide] = 0
        num_solutions, _ = solve(board)

        if num_solutions > 1:
            board[coords_hide] = prev_num
            continue
        hidden += 1



def main():
    name = input('What is your name?')
    game_loop(name,generate_board,solve)



if __name__ == '__main__':
    main()
