from api import Api 

class Game:
    # keep track of game state, test win cons, board full etc
    # Game.run 
    # debug "what move? then print out board", otherwise, just play two agents
    # agent 1 is always us?

    #NOTE: create function to check if its our turn! We can keep a list of activate games and loop
    # through the active ones
    def __init__(self, agent1, agent2, first_move=True, gameId=None) -> None:
        self.agent1 = agent1
        self.agent2 = agent2

        # 0 agent 1 moves, 1 agent 2 moves
        if first_move:
            self.to_move = 0
        else:
            self.to_move = 1
        
        # game has not been created
        if gameId == None:
            # this can be either way, no difference
            self.gameId = agent1.create_game(agent2.tid)
            print("Current game id: {}".format(self.gameId))
        # need to 
        else:
            self.gameId = gameId
    
    def play_game(self):
        # while game not done (-1):
        #   alternate moves of agents
        # check get_game_state after each move - report win etc.

        # main game loop
        while self.get_game_state() == -1:
            pass
        
        
        # while move is not made
            # collect current board state compare to previous state
            # if the same then sleep 30 seconds and stay in while
            # if different break while loop - pass to agent
     
        
        pass
    
    def get_game_state(self):
        """0 on agent 1 win, 1 on agent 2 win, 2 on tie, -1 on continuing"""
        # request board state
        # use opposite player !self.to_move...

        pass 

    # TODO: get turn
    def my_turn(self):
        pass
