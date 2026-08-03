import numpy as np

from project import check_this, check_cell_board, solve


def test_check_this():
    valid_unit = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    invalid_unit = np.array([1, 2, 3, 4, 5, 5, 7, 8, 9])
    incomplete_unit = np.array([1, 2, 0, 4, 0, 6, 7, 8, 9])

    assert check_this(valid_unit) is True
    assert check_this(invalid_unit) is False
    assert check_this(incomplete_unit) is True


def test_check_cell_board():
    board = np.array([
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

    assert check_cell_board((0, 0), board) is True

    board[0, 2] = 5

    assert check_cell_board((0, 2), board) is False


def test_solve():
    board = np.array([
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

    solved_board = solve(board, fastest=True)

    assert isinstance(solved_board, np.ndarray)
    assert np.all(solved_board != 0)
    assert all(
        check_cell_board((y, x), solved_board)
        for y in range(9)
        for x in range(9)
    )
