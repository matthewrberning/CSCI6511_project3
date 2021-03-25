from api import Api
import numpy as np
from random import randrange
import math
import json
import time
from minimax import minimax

class Board:
    def __init__(self, size, target) -> None:
        self.total_spaces = size**2
        self.dim = size
        self.target = target
        self.middle_point = math.floor(size / 2)
        self.board =  np.zeros( (size, size), dtype=np.int8 )
    
    def get_open_spaces(self):
        """Return the possible next moves""" 
        return np.argwhere(self.board == 0)

    def isFull(self):
        return True if np.count_nonzero(self.board) == self.total_spaces else False

    def isEmpty(self):
        return True if np.count_nonzero(self.board) == 0 else False

    def add_symbol(self, point, symbol):
        """point is a int tuple (x,y), symbol 1 or 0"""
        self.board[point[0]][point[1]] = symbol

    def remove_symbol(self, point):
        self.board[point[0]][point[1]] = 0

    # agent 1 will be represented by 1's, agent 2 will be -1's
    # @param coords: the coordinates of the most recently placed mark, represented as a 1x2 np arr
    def check_win_con(self, coords):
        """Check if the board at that point(most recent move) has won"""
        # 0 on agent 1 win, 1 on agent 2 win, 2 on tie, -1 on continuing
        # use the coords of the last turn to determine if we are looking for 1 or -1
        board = self.board
        target = self.target
        
        ans = 0
        if (board[coords[0], coords[1]] == 1):
            ans = 1
        elif (board[coords[0], coords[1]] == -1):
            ans = -1
        else:
            print("ERROR: Checking for win in unmarked square.")
            exit()

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
                    return True
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
                    return True
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
                    return True
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
                    return True
            start_space[0] -= 1
            start_space[1] += 1
        return False

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
                print("\n[interactive/debug mode - playing with ourselves]\n")
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
        # don't forget: the team that created the game always has the first move
        turn = 0
        # print(self.gameId)
        # print(self.our_agent.tid)
        # print(self.gameId)

        game_state = -1

        while game_state == -1:
        # while True:

            if self.debug:
                #show the board
                print("\n")
                print("---BOARD MAP---")
                self.display_board(self.our_agent, self.gameId)
                print("\n")
                print("---NUMPY BOARD---")
                print(self.board)

                if turn == 0:
                    #agents turn
                    # move = self.get_move_dummy_agent()
                    move = self.get_move_agent()
                    turn = not turn

                    self.board.add_symbol(move, 1)
                    game_state = self.get_game_state(0, move)
                    print("game_state: ", game_state)
                    

                else:
                    # user's turn
                    move = self.get_move_user()
                    turn = not turn

                    self.board.add_symbol(move, -1)
                    game_state = self.get_game_state(1, move)
                    print("game_state: ", game_state)
                    

            else:
                # if turn == 0:
                # if the check is true then the opponent has made a move, time for ours
                if self.check_for_opponent_moves():
                    print("current board")
                    self.display_board(self.our_agent, self.gameId)

                    #check for game state
                    # if game still open then play

                    # else report game state (loss/tie)

                    print("our agent is playing now...")
                    self.get_move_dummy_agent()

                    print("new board")
                    self.display_board(self.our_agent, self.gameId)

                else:
                    time.sleep(6) #sleep 2 seconds
                    continue

        print("GAME OVER! game_state: ", game_state)
        print("(0 on agent 1 win, 1 on agent 2 win, 2 on tie)")
        print("\n")
        print("---FINAL BOARD MAP---")
        self.display_board(self.our_agent, self.gameId)
                


        

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
        status = 0
        while status == 0:
            move = input("move? format: int,int\nmove: ")
            move = move.split(',')
            if len(move) == 1:
                print("please use format: int,int")
                continue
            elif len(move) > 2:
                print("please use format: int,int")
                continue
            else:
                try:
                    move = int(move[0]), int(move[1])
                except ValueError:
                    print("please use format: int,int")
                    continue
            d = dict(json.loads(self.opponent.make_move(self.gameId, move)))

            if d["code"] == "OK":
                status = 1
                return move
            else:
                continue

    def get_move_agent(self):

        status = 0
        while status == 0:
            move = minimax(self.board, 2, True)[1]
            print("minimax move: ", move)
            d = dict(json.loads(self.our_agent.make_move(self.gameId, move)))

            if d["code"] == "OK":
                status = 1
                return move
            else:
                continue


        return move

    def get_move_dummy_agent(self):
        # find list of the currently unocupied spaces, choose one at random 
        # send move to api
        d = dict(json.loads(self.our_agent.get_board_map(self.gameId)))
        # print(d)

        if not d['output']:
            #first move is not made so make it in middle of 3x3
            self.our_agent.make_move(self.gameId, (1,1))
            return (1,1)

        else:
            while True:
                move = (randrange(self.size), randrange(self.size))
                if f"{move[0]},{move[1]}" in d['output']:
                    continue
                else:
                    print("(dummy) agent's move: ", move)
                    self.our_agent.make_move(self.gameId, move)
                    return move
    


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



            
        

