from api import Api
import numpy as np

class Board:
    def __init__(self, size, target) -> None:
        self.total_spaces = size**2
        self.dim = size
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

    def check_win_con(self, point):
        """Check if the board at that point(most recent move) has won"""
        pass

    def __str__(self) -> str:
        return str(self.board)

class Game:
    def __init__(self, us, opp_tid, size=3, target=3,first_move=True, gameId=None) -> None:
        self.us = us


        # game not created
        if not gameId:
            self.gameId = us.create_game(opp_tid, size, target)
            self.size, self.target = size, target
        # game created
        else:
            self.size, self.target = self.get_game_params(gameId)
        
        self.board = Board(self.size, self.target)
        
        
        
    def play_game(self):
        # while game not done (-1):
        #   alternate moves of agents
        # check get_game_state after each move - report win etc.

        # main game loop
        while self.get_game_state() == -1:
            # while move is not made
                # collect current board state compare to previous state
                # if the same then sleep 30 seconds and stay in while
                # if different break while loop - pass to agent
            pass
        

    def get_game_params(self, gameId):
        b = self.us.get_board_string(gameId)

        one_row = b['output'].split("\n")
        t = int(b['target'])
        return len(one_row[0]), t


    
    def get_game_state(self, last_to_move, point):
        """
        0 on agent 1 win, 1 on agent 2 win, 2 on tie, -1 on continuing. Only have to check the last move!
        last_to_move is the agent that last played, using the enumeration above. So, on a win, return the agent 
        identifier, otherwise check for a tie, or keep playing
        """
        # request board state
        # use opposite player !self.to_move...
        
        if self.board.check_win_con(point):
            return last_to_move
        elif self.board.isFull():
            return 2
        return -1
    
    

