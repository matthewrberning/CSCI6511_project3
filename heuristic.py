import numpy as np
from game import Board

# 0 on agent 1 win, 1 on agent 2 win, 2 on tie, -1 on continuing
# agent 1 will be represented by 1's, agent 2 will be -1's
# @param board: numpy array representing board, represented asa square np arr
# @param target: the length of the winning line
# @param coords: the coordinates of the most recently placed mark, represented as a 1x2 np arr
def get_game_state(board, target, coords):
    # use the coords of the last turn to determine if we are looking for 1 or -1
    ans = 0
    if (board[coords[0], coords[1]] == 1):
        ans = 1
    elif (board[coords[0], coords[1]] == -1):
        ans = -1
    else:
        print("ERROR: Checking for win in unmarked square.")
        exit()

    max_util = 0
    # check for vertical win
    start_space = [coords[0]-(target-1), coords[1]]
    for i in range(target):
        if start_space[0] >= 0 and start_space[0] <= coords[0]:
            temp = 0
            if (start_space[0]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0]+j, start_space[1]] == ans:
                        temp += 1
            if (temp > max_util):
                max_util = temp
        start_space[0] += 1

    # check for horizontal win
    start_space = [coords[0], coords[1]-(target-1)]
    for i in range(target):
        if start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp = 0
            if (start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0], start_space[1]+j] == ans:
                        temp += 1
            if (temp > max_util):
                max_util = temp
        start_space[1] += 1
    
    # check for diagonal win, negative slope
    start_space = [coords[0]-(target-1), coords[1]-(target-1)]
    for i in range(target):
        if start_space[0] >= 0 and start_space[0] <= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp = 0
            if (start_space[0]+(target-1) < len(board) and start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0]+j, start_space[1]+j] == ans:
                        temp += 1
            if (temp > max_util):
                max_util = temp
        start_space[0] += 1
        start_space[1] += 1

    # check for diagonal win, positive slope
    start_space = [coords[0]+(target-1), coords[1]-(target-1)]
    for i in range(target):
        if start_space[0] < len(board) and start_space[0] >= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp = 0
            if (start_space[0]-(target-1) >= 0 and start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0]-j, start_space[1]+j] == ans:
                        temp += 1
            if (temp > max_util):
                max_util = temp
        start_space[0] -= 1
        start_space[1] += 1
    return max_util

board = np.zeros((5, 5))
print(len(board))
board[4, 4] = 1
board[3, 1] = 1
board[1, 3] = 1
board[2, 2] = 1
board[0, 4] = 1
board[4, 0] = 1
print(board)

#checking for vertical wins
print(get_game_state(board, 5, [2, 2]))