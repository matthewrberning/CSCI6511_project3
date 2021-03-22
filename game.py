from api import Api
import numpy as np
from random import randrange
import json
import time

class Board:
    def __init__(self, size, target) -> None:
        self.total_spaces = size**2

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
    def __init__(self, our_agent, opponent, size=3, target=3, first_move=True, gameId=None) -> None:
        self.our_agent = our_agent #our agent GME teamId: 1265
        self.opponent = opponent #either an instance of Api class (mellon) or an int(teamId) for opponent team

        self.first_move = first_move #do we need this? the first move always goes to the starting team


        # game not created
        if not gameId:

            if isinstance(opponent, Api):
                #creating a new game with interactive play
                print("interactive/debug")
                self.debug = True
                self.gameId = our_agent.create_game(opponent.tid, size, target)
            else:
                #creating a new game with an outside team (opponent is an int)
                self.debug = False
                self.gameId = our_agent.create_game(opponent, size, target)

            
            self.size, self.target = size, target

        # game created
        else:

            if isinstance(opponent, Api):
                print("interactive/debug")
                self.debug = True

            else:
                self.debug = False

            self.size, self.target = self.get_game_params(gameId)
            self.gameId = gameId
        
        self.board = Board(self.size, self.target)
        
        
        
    def play_game(self):
        # while game not done (-1):
        # alternate moves of agents
        # check get_game_state after each move - report win etc.

        # main game loop
        # the team that created the game always has the first move
        turn = 0
        # print(self.gameId)
        # print(self.our_agent.tid)
        # print(self.gameId)

        # while self.get_game_state() == -1:
        while True:

            if self.debug:
                #show the board
                self.display_board(self.our_agent, self.gameId)

                if turn == 0:
                    #agents turn
                    self.get_move_dummy_agent()
                    turn = not turn

                else:
                    # user's turn
                    self.get_move_user()

                    turn = not turn

            else:
                # if turn == 0:
                # if the check is true then the opponent has made a move, time for ours
                if self.check_for_opponent_moves():
                    print("current board")
                    self.display_board(self.our_agent, self.gameId)

                    print("our agent is playing now...")
                    self.get_move_dummy_agent()

                    print("new board")
                    self.display_board(self.our_agent, self.gameId)

                else:
                    time.sleep(6) #sleep 2 seconds
                    continue


            # while move is not made
                # collect current board state compare to previous state
                # if the same then sleep 30 seconds and stay in while
                # if different break while loop - pass to agent
            # pass
        

    def get_game_params(self, gameId):
        b = self.our_agent.get_board_string(gameId)

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



    def display_board(self, agent, gameId):

        for line in agent.get_board_string(gameId)["output"].split("\n"):
            if line != '':
                line_map = "|"

                for char in line:
                    line_map = line_map+f"{char}|"
                print('--'*len(line))
                print(line_map)
            else:
                continue
        # show the board
        # list who is who (X or O)
        # list total number of moves made, list total empty spaces
        pass

    def get_move_user(self):
        #ask user for input, send to api
        move = input("move? format: (int, int)\nmove: ")
        self.opponent.make_move(self.gameId, move)

    def get_move_dummy_agent(self):
        # find list of the currently unocupied spaces, choose one at random 
        # send move to api
        d = dict(json.loads(self.our_agent.get_board_map(self.gameId)))
        # print(d)

        if not d['output']:
            self.our_agent.make_move(self.gameId, (1,1))

        else:
            while True:
                move = (randrange(self.size), randrange(self.size))
                if f"{move[0]},{move[1]}" in d['output']:
                    continue
                else:
                    print("(dummy) agent's move: ", move)
                    self.our_agent.make_move(self.gameId, move)
                    break

    def check_for_opponent_moves(self):
        d = dict(json.loads(self.our_agent.get_moves(self.gameId, 1)))

        if d["code"] == "FAIL":
            if d["message"] == "No moves":
                #we need to make the first move
                return True
            else:
                print("something else happened...")
                print(d)
        elif d["moves"][0]["teamId"] == self.our_agent.tid:
            return False
        else:
            return True



            
        

