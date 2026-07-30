from itertools import cycle
import numpy as np
from collections import deque
from Node import Node
import math



class SudoBoard:
    def __init__(self,name,level=1):
        self.size = (9,9)
        self.board = np.zeros((9,9),dtype=np.int64)
        self.name = name
        self.level = level
        self.possiblenum = set(range(1,10))

    # before was 3 diff methods to check row,column and qdrant. changed to only one
    def check_this(self,unit):
        set_unit = set()
        for cell in unit:
            if cell != 0 and cell in set_unit:
                return False
            set_unit.add(cell)
        return True

    def check_cell_board(self,coords,board):
        y,x = coords
        row = board[y,:]
        column = board[:,x]
        #quadrant giga elegant logic
        qindexy = (y // 3) * 3
        qindexx = (x // 3) * 3
        quadrant = board[qindexy:qindexy+3,qindexx:qindexx+3].flatten()

        if not all([self.check_this(row),self.check_this(column),self.check_this(quadrant)]):
                return False
        return True

    def check_possiblenums(self,y,x,board):
        value_num = board[y,x]
        possible = []

        for num in self.possiblenum:
            if num != value_num:
                board[y,x] = num
                if self.check_cell_board(board=board,coords=(y,x)):
                    possible.append(num)
                board[y,x] = value_num
        if possible:
            return possible
        return None


    def heuristic_function(self,board):
        #func to return in order for now the coords with least possible nums
        size = len(board)

        min_size_possible = math.inf
        zero_inboard = False
        best_coord = None
        possibilities = None

        for y in range(size):
            for x in range(size):
                if board[y,x] == 0:
                    if not zero_inboard:
                        zero_inboard = True
                    possible_for_this = self.check_possiblenums(y,x,board)

                    if possible_for_this is None:
                        continue

                    possible_size = len(possible_for_this)

                    if possible_size < min_size_possible:
                        min_size_possible = possible_size
                        best_coord = (y,x)
                        possibilities = possible_for_this

                    if min_size_possible == 1:
                        return best_coord, possibilities
        if not zero_inboard:
            return zero_inboard, possibilities
        return best_coord, possibilities

    def new_heuristic(self):
        #3 cases possible hueristic
        # no num in board
        #



    #DEPRECATED first solve function i did, was too slow, tried to finetune with the heuristic but still slow
    def solve(self,board):
        # GET size of board


        # empty_cells = [(y,x) for y in range(n_y) for x in range(n_x) if board[y,x] == 0]
        empty_cells = self.heuristic_function(board)
        f_y,f_x = empty_cells.pop(0)
        #initialize deque to queue and append first node
        queue = deque()
        first_node = Node(coords=(f_y,f_x))
        queue.append(first_node)
        new_board = np.array(board)

        solutions = []
        #start node queue loop
        while queue:

            #get node from queue and get its init value from self
            node = queue.pop()
            # node.nums = []
            node_num = node.nums[node.index]
            ny,nx = node.coords

            # check real possible nums for this board and coords in place
            possible_nums_fornode = self.check_possiblenums(y=ny,x=nx,board=new_board)

            # check if the possible_nums is empty or the num choosen by the node is invalid
            if not possible_nums_fornode or node_num not in possible_nums_fornode:

                # checks if node in the last num of init possibilities
                if node.index < 8:
                    #GOTO next num
                    node.index += 1
                    queue.append(node)
                else:
                    #IF in last num from init start back tracking
                    #TODO LATER add a check backtrack and append this solution to know if board have more than 1 solution
                    if node.parent != None:
                        new_board[ny,nx] = 0
                        empty_cells.insert(0,(ny,nx))
                        node = node.parent
                        node.index += 1 if node.index < 8 else 0
                        queue.append(node)
                    else:
                        #put here the append and a checker for values that the node still have
                        return len(solutions),solutions
                #append again for new value or parent


            #IF the value of node is valid and possible append this value to the board
            else:
                new_board[ny,nx] = node_num
                #search for next empty cell TODO: make a search logic for the nodes in queue so the method doesnt have to linear search every time

                if not empty_cells:
                    solutions.append(new_board)

                    return solutions
                else:
                    child_y,child_x = empty_cells.pop(0)
                    #IF found empty create child node to make that logic of values again
                    new_node = Node(coords=(child_y,child_x),parent=node)
                    queue.append(new_node)

            #printing board just for vizualization
            print('\n',new_board)


        #if not queue all solution found etc return board TODO
        print('Solved')
        return new_board


    def new_solve(self,solutions=None,fastest=False):
        #add a None check valid later
        if solutions is None:
            solutions = []
        print(self.board)
        coords,possible = self.heuristic_function(self.board)

        if coords == False:
            if fastest:
                return np.copy(self.board)
            solutions.append(np.copy(board))
            return

        while possible:
            to_check = possible.pop()
            self.board[coords] = to_check

            board_s = self.new_solve(solutions,fastest=fastest)
            if fastest and isinstance(board_s,np.ndarray):
                return board_s

            self.board[coords] = 0

        return solutions






