# Sudoku Generator & Solver
#### Video Demo:  <URL HERE>
#### Description:

Simple recursion backtracking algorithm for solving and generate a Sudoku board/game, also make a very simple
pygame vizualization for better understanding.

## Features
- Generate Sudoku boards
- Different difficulty levels
- Solve Sudoku boards
- Check whether a puzzle has a unique solution
- heuristic function for optimization
- Recursive backtracking
- Pygame interface

## How It Works
### 1. Board Representation
  First we make the board as an 2d numpy array for faster, and better manipulation,
    representing empty cells as 0.

### 2. Sudoku Validation

- check_this(unit) : First we pass a row,col or flatten 3x3 grid, so the
  function can iterate over all the values, and add to a set, if a value is in the set, return False.

- check_cell_board(coords,board) : Using the coords of the cell chosen to be validated, the function extracts the row, col and 3x3 quadrant of cell,
  using the full board passed as the argument. After that checks if any of the check_this() function of row, col and quadrant, returns as False.

### 3. Candidate Generation

- check_possiblenums(coords,board) : Using the cell chosen and board, it iterates in the range of 1 to 9 inclusive, and use check_cell_board() function
  to check if the numbers is valid, if returns True append the number to the possible numbers list and in the end returns it.

### 4. Heuristic

- heuristic_function(board) : works as a optimization function to the solver, first it checks if there are empty cells in board, if there isn´t checks if the board
  is valid, and then returns False or True. If the board have empty cells it iterates and call the check_possiblenums(), and count how many numbers are possible,
  if the count is less than the previous minimum, it stores the numbers and the count. At the end returns the possible numbers and the cell coordinates with the least amount of possibilities.

### 5. Solver

- solve(board,solutions=None,fastest=False) : Receives board, initialize solutions with None value and fastest as False.
  First the function checks is solution is None and initializes it as a list, then call heuristic_function to find the most optimal path,
  **Base Case:** checks if it have more than 1 solution for the recursion, and checks if the board is solved, if so it checks the fastest value, value is True = return the solutions,
    else it appends the solution to the solutions list and backtrack.

  **Recursion Loop:** After that is where the recursion starts, begin looping while there is possible numbers and pop it, place the popped number in board and call solve again to go deeper, when a number doesn't pass the base case it goes back to the
    while loop, change back this cell, checks another number and go deeper again.

  If the function finds a solution it falls on the base case and append the solution to the list and search for more, or if fastest is active it return the solved board.

### 6. Generator

- **__generate_board(name, level=1)__**: Receives your name and a level to be played.
  First it initializes the board as empty, and a random value in range of 1 to 9, iterates each char of the num, gets its decimal value and multiply by the random value, and set the seed like this to make it more random,
    and then it generates a random coordinate in board and a random number to be placed, place it in board and calls solve() with fastest = True.

  After that it creates a random range of clues based on the level chosen by the player, initialize a counter for the hidden numbers and starts looping.
    **Base case:** If the hidden count is equal or more than the numbers to hide it returns the board
    **Hiding Logic:** Selects a random coordinates and change to 0, call solve() in this new state and checks how many solutions the board have now
    **If solutions > 1:** Changes back the number and go to the next iteration


## Project Structure
Show folders/files.

## Installation
pip install -r requirements.txt

## Usage
python project.py

## Testing
pytest test_project.py

## Author
Luis Fernando Faria Delmondes
