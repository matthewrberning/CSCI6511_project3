import numpy as np

# 0 on agent 1 win, 1 on agent 2 win, 2 on tie, -1 on continuing
# agent 1 will be represented by 1's, agent 2 will be -1's
# @param board: numpy array representing board, represented asa square np arr
# @param target: the length of the winning line
# @param coords: the coordinates of the most recently placed mark, represented as a 1x2 np arr
def get_game_state(board, target, coords):
    # check for vertical win
    print("checking for vertical")
    found = False
    start_space = [coords[0]-(target-1), coords[1]]
    for i in range(target):
        if start_space[0] >= 0 and start_space[0] <= coords[0]:
            temp_found = True
            if (start_space[0]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0]+j, start_space[1]] != 1:
                        temp_found = False
            else:
                temp_found = False
            if (temp_found):
                found = True
                print("found at", start_space)
        start_space[0] += 1

    # check for horizontal win
    print("checking for horizontal")
    start_space = [coords[0], coords[1]-(target-1)]
    for i in range(target):
        print("start space:", start_space)
        if start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp_found = True
            if (start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    print(j)
                    if board[start_space[0], start_space[1]+j] != 1:
                        temp_found = False
            else: 
                temp_found = False
            if (temp_found):
                found = True
                print("found at", start_space)
                break
        start_space[1] += 1
    
    # check for diagonal win

    print(found)

board = np.zeros((5, 5))
print(len(board))
board[4, 0] = 1
board[4, 2] = 1
board[4, 1] = 1
board[4, 4] = 1
print(board)

# checking for vertical wins
get_game_state(board, 3, [4, 2])