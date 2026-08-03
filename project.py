import numpy as np
import random



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


valid_sudoku = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 4, 2, 1, 7, 6, 6],
    [2, 7, 6, 8, 5, 3, 1, 5, 4],
    [9, 1, 4, 7, 6, 5, 2, 0, 3],
    [4, 2, 3, 7, 8, 9, 6, 5, 1],
    [7, 1, 9, 2, 3, 4, 8, 3, 5],
    [3, 6, 5, 4, 1, 9, 7, 2, 8]
])

solved_board = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],

    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],

    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
], dtype=int)


hardest_sudoku = np.array([
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
], dtype=int)


# print(heuristic_function(hardest_sudoku))
print(generate_board('Luis'))
