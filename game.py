from api import Api
import numpy as np
from random import randrange
import json
import time
from minimax import minimax
from board import Board


class Game:
    def __init__(self, our_agent, opponent, size=3, target=3, first_move=True, gameId=None) -> None:
        self.our_agent = our_agent #our agent GME teamId: 1265
        self.opponent = opponent #either an instance of Api class (mellon) or an int(teamId) for opponent team

        self.first_move = first_move #do dwe need this? the first move always goes to the starting team


        # game not created
        if not gameId:

            if isinstance(opponent, Api):
                #creating a new game with interactive play
                print("\n[interactive/debug mode - playing with ourselves]\n")
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
        
        
        
    def play_game(self, who_starts="us"):
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
                    # game_state = get_game_state(self.board, self.target, move)
                    game_state = self.board.check_win_con(self.target, move)[1]
                    print("----game_state: ", game_state)
                    

                else:
                    # user's turn
                    move = self.get_move_user()
                    # move = self.get_move_agent2()
                    turn = not turn

                    self.board.add_symbol(move, -1)
                    # game_state = get_game_state(self.board, self.target, move)
                    game_state = self.board.check_win_con(self.target, move)[1]
                    print("----game_state: ", game_state)
                    

            else:
                # if turn == 0:
                # if the check is true then the opponent has made a move, time for ours
                if self.check_for_opponent_moves(who_starts=who_starts):
                    # update board happens in check_for_opponent_moves
                    
                    print("\n")
                    print("---CURRENT BOARD MAP---")
                    self.display_board(self.our_agent, self.gameId)
                    print("\n")
                    print("---NUMPY BOARD---")
                    print(self.board)

                    #check the board after their move for win conditions

                    d = dict(json.loads(self.our_agent.get_moves(self.gameId, 1)))
                    move=(int(d["moves"][0]["move"].split(',')[0]), int(d["moves"][0]["move"].split(',')[1]))

                    game_state = self.board.check_win_con(self.target, move)[1]
                    print("----game_state after opponent's move: ", game_state)
                    
                    #if they win/tie on that turn exit the while loop
                    if game_state != -1:
                        break

                    # otherwise continue playing our turn
                    print("\nour agent is playing now...")
                    move = self.get_move_agent()
                    self.board.add_symbol(move, 1)

                    game_state = self.board.check_win_con(self.target, move)[1]
                    print("----game_state: ", game_state)

                    print("\n")
                    print("---CURRENT BOARD MAP---")
                    self.display_board(self.our_agent, self.gameId)
                    print("\n")
                    print("---NUMPY BOARD---")
                    print(self.board)


                    # else report game state (loss/tie)

                    # print("our agent is playing now...")
                    # self.get_move_dummy_agent()

                    # print("new board")
                    # self.display_board(self.our_agent, self.gameId)


                else:
                    time.sleep(10) #sleep 2 seconds
                    continue

        print("GAME OVER! game_state: ", game_state)
        print("(0 on agent 1 win,\n1 on agent 2 win,\n2 on tie)")
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

        print(self.board)
        
        if self.board.check_win_con(point):
            return last_to_move
        elif self.board.isFull():
            return 2
        return -1



    def display_board(self, agent, gameId):
        '''
        display the board
        '''

        for line in agent.get_board_string(gameId)["output"].split("\n"):
            if line != '':
                line_map = "|"

                for char in line:
                    line_map = line_map+f"{char}|"
                print('--'*len(line))
                print(line_map)
            else:
                continue

    def get_move_user(self):    
        #ask user for input, send to api
        status = 0
        while status == 0:
            move = input("\nmove? format: int,int\nmove: ")
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
            move = minimax(self.board, 1, True)[1]
            # print("-------minimax move DEPTH 3, A-B pruning: ", move)
            d = dict(json.loads(self.our_agent.make_move(self.gameId, move)))

            if d["code"] == "OK":
                status = 1
                return move
            else:
                continue


        return move



    # def get_move_agent2(self):

    #     status = 0
    #     while status == 0:
    #         move = minimax(self.board, 1, True)[1]
    #         print("-------minimax move HEURISTIC ONLY: ", move)
    #         d = dict(json.loads(self.opponent.make_move(self.gameId, move)))

    #         if d["code"] == "OK":
    #             status = 1
    #             return move
    #         else:
    #             continue


    #     return move


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
    


    def check_for_opponent_moves(self, who_starts):
        d = dict(json.loads(self.our_agent.get_moves(self.gameId, 1)))

        if d["code"] == "FAIL":
            if d["message"] == "No moves" and who_starts=="us":
                #we need to make the first move
                return True
            elif d["message"] == "No moves" and who_starts=="them":
                #we need to wait for them to move
                return False
            else:
                print("something else happened...")
                print(d)
        elif d["moves"][0]["teamId"] == self.our_agent.tid:
            return False 
        else:
            move=(int(d["moves"][0]["move"].split(',')[0]), int(d["moves"][0]["move"].split(',')[1]))
            #update the board
            self.board.add_symbol(move, -1)
            return True






            
        

