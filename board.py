import numpy as np

class Board:
    def __init__(self, size, target) -> None:
        self.total_spaces = size**2
        self.dim = size
        self.target = target
        self.board =  np.zeros( (size, size), dtype=np.int8 )
    
    def get_open_spaces(self):
        """Return the possible next moves""" 
        return np.argwhere(self.board == 0)

    def isFull(self):
        return True if np.count_nonzero(self.board) == self.total_spaces else False

    def add_symbol(self, point, symbol):
        """point is a int tuple (x,y), symbol 1 or 0"""
        self.board[point[0]][point[1]] = symbol

    def remove_symbol(self, point):
        self.board[point[0]][point[1]] = 0

    def check_win_con(self, target, coords):
        board = self.board
        target = self.target
        # use the coords of the last turn to determine if we are looking for 1 or -1
        ans = 0
        if (board[coords[0], coords[1]] == 1):
            ans = 1
        elif (board[coords[0], coords[1]] == -1):
            ans = -1
        else:
            print("ERROR: Checking for win in unmarked square.")
            exit()
        winner = 0
        if ans == 1:
            winner = 0
        else: 
            winner = 1
        # check for vertical win
        start_space = [coords[0]-(target-1), coords[1]]
        for i in range(target):
            if start_space[0] >= 0 and start_space[0] <= coords[0]:
                temp_found = True
                if (start_space[0]+(target-1) < len(board)):
                    for j in range(target):
                        if board[start_space[0]+j, start_space[1]] != ans:
                            temp_found = False
                else:
                    temp_found = False
                if (temp_found):
                    return True, winner
            start_space[0] += 1

        # check for horizontal win
        start_space = [coords[0], coords[1]-(target-1)]
        for i in range(target):
            if start_space[1] >= 0 and start_space[1] <= coords[1]:
                temp_found = True
                if (start_space[1]+(target-1) < len(board)):
                    for j in range(target):
                        if board[start_space[0], start_space[1]+j] != ans:
                            temp_found = False
                else: 
                    temp_found = False
                if (temp_found):
                    return True, winner
            start_space[1] += 1
        
        # check for diagonal win, negative slope
        start_space = [coords[0]-(target-1), coords[1]-(target-1)]
        for i in range(target):
            if start_space[0] >= 0 and start_space[0] <= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[1]:
                temp_found = True
                if (start_space[0]+(target-1) < len(board) and start_space[1]+(target-1) < len(board)):
                    for j in range(target):
                        if board[start_space[0]+j, start_space[1]+j] != ans:
                            temp_found = False
                else: 
                    temp_found = False
                if (temp_found):
                    return True, winner
            start_space[0] += 1
            start_space[1] += 1

        # check for diagonal win, positive slope
        start_space = [coords[0]+(target-1), coords[1]-(target-1)]
        for i in range(target):
            if start_space[0] < len(board) and start_space[0] >= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[1]:
                temp_found = True
                if (start_space[0]-(target-1) >= 0 and start_space[1]+(target-1) < len(board)):
                    for j in range(target):
                        if board[start_space[0]-j, start_space[1]+j] != ans:
                            temp_found = False
                else: 
                    temp_found = False
                if (temp_found):
                    return True, winner
            start_space[0] -= 1
            start_space[1] += 1
        if self.isFull():
            return False, 2
        return False, -1

    def __str__(self) -> str:
        return str(self.board)