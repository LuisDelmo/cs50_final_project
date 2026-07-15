import numpy as np
from SudoBoard import SudoBoard
import time

#TODO 3 func outside the class to satisfy check50
def initialize_sudoku(name,level):
    pass


sudoku = SudoBoard('Luis')

def beacnkmark_time(board):
    for i in range(50):
        start_time = time.perf_counter()
        _ = sudoku.solve(board)
        end_time = time.perf_counter()

        this_time = end_time - start_time
        times.append(this_time)
        print(i)


    # 4. Calculate the difference


    avg_time = sum(times) / len(times)
    best_time = min(times)
    worst_time = max(times)
    time_eplapsed = sum(times)

    print("\n--- Teste sudoku 50 resoluções ---")
    print(f"Media de tempo: {avg_time:.6f} seconds")
    print(f"Resolucao mais rapida:  {best_time:.6f} seconds")
    print(f"Resolucao mais lenta:  {worst_time:.6f} seconds")
    print(f"tempo total  :  {time_eplapsed:.6f} seconds")

valid_sudoku = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 4, 2, 1, 7, 3, 6],
    [2, 7, 6, 8, 5, 3, 1, 0, 4],
    [9, 1, 4, 7, 6, 5, 2, 8, 3],
    [4, 2, 3, 7, 8, 9, 6, 5, 1],
    [7, 1, 9, 2, 3, 4, 8, 3, 5],
    [3, 6, 5, 4, 1, 9, 7, 2, 8]
])

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



broken_test_board = np.array([
    [5, 3, 0,  0, 7, 0,  0, 0, 0],
    [6, 0, 0,  1, 9, 5,  0, 0, 0],
    [0, 9, 8,  0, 0, 0,  0, 6, 0],

    [8, 0, 0,  0, 6, 0,  0, 0, 3], # <-- Primeiro 6 aqui
    [4, 0, 0,  8, 0, 3,  0, 0, 1],
    [7, 0, 0,  0, 2, 6,  0, 0, 6], # <-- Segundo 6 aqui (Invalida o quadrante!)

    [0, 6, 0,  0, 0, 0,  2, 8, 0],
    [0, 0, 0,  4, 1, 9,  0, 0, 5],
    [0, 0, 0,  0, 8, 0,  8, 7, 9]
])

sparse_board = np.array([
    [1, 0, 0, 0, 0, 7, 0, 9, 0],
    [0, 3, 0, 0, 2, 0, 0, 0, 8],
    [0, 0, 9, 6, 0, 0, 5, 0, 0],
    [0, 0, 5, 3, 0, 0, 9, 0, 0],
    [0, 1, 0, 0, 8, 0, 0, 0, 2],
    [6, 0, 0, 0, 0, 4, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 7, 0, 0, 0, 3, 0, 0]
])


test_board = np.array([
    [5, 3, 4, 9, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])



medium_puzzle = np.array([
    [0, 0, 0, 6, 0, 0, 4, 0, 0],
    [7, 0, 0, 0, 0, 3, 6, 0, 0],
    [0, 0, 0, 0, 9, 1, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 1, 8, 0, 0, 0, 3],
    [0, 0, 0, 3, 0, 6, 0, 4, 5],
    [0, 4, 0, 2, 0, 0, 0, 6, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 1, 0, 0]
])


sudoku_board = np.array([
    [0, 0, 0,  7, 8, 9,  0, 0, 0], # Row 0 provides: {7, 8, 9} to the empty cells
    [1, 2, 3,  0, 0, 0,  0, 0, 0], # Box 0 provides: {1, 2, 3}
    [4, 5, 6,  0, 0, 0,  0, 0, 0], # Box 0 provides: {4, 5, 6}

    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],

    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0]
])

sudoku.board = sparse_board
# print(sudoku.board)



# print(sudoku.heuristic_function(valid_sudoku))
# print(sudoku.check_possiblenums(4,4,easy_puzzle))
# print(sudoku.heuristic_function(sudoku_board))
print(sudoku.new_solve(board=sparse_board))



# print(sudoku.heuristic_function(easy_puzzle))


# print(sudoku.check_cell_board(board=broken_test_board,coords=(3,4)))

