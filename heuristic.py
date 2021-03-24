import numpy as np
from game import Board

# 0 on agent 1 win, 1 on agent 2 win, 2 on tie, -1 on continuing
# agent 1 will be represented by 1's, agent 2 will be -1's
# @param board: numpy array representing board, represented asa square np arr
# @param target: the length of the winning line
# @param coords: the coordinates of the most recently placed mark, represented as a 1x2 np arr
def heuristic(board, target, coords):
    # use the coords of the last turn to determine if we are looking for 1 or -1
    turn = 0
    if (board[coords[0], coords[1]] == 1):
        turn = 1
        print("its 1 turn")
    elif (board[coords[0], coords[1]] == -1):
        turn = -1
        print("it's -1 turn")
    else:
        print("ERROR: Checking for win in unmarked square.")
        exit()

    max_util = 0
    multiplier = 0
    ans = 1
    # check vert, 1
    start_space = [coords[0]-(target-1), coords[1]]
    for i in range(target):
        if start_space[0] >= 0 and start_space[0] <= coords[0]:
            temp = 0
            if (start_space[0]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0]+j, start_space[1]] == ans:
                        temp += 1
            if (temp == target):
                return float('inf')
            if (ans == turn):
                temp = 0
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):   
                multiplier += 1
        start_space[0] += 1

    # check horiz, 1
    start_space = [coords[0], coords[1]-(target-1)]
    for i in range(target):
        if start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp = 0
            if (start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0], start_space[1]+j] == ans:
                        temp += 1
            if (temp == target):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):   
                multiplier += 1
        start_space[1] += 1
    
    # check diag, negative slope, 1
    start_space = [coords[0]-(target-1), coords[1]-(target-1)]
    for i in range(target):
        if start_space[0] >= 0 and start_space[0] <= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp = 0
            if (start_space[0]+(target-1) < len(board) and start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0]+j, start_space[1]+j] == ans:
                        temp += 1
            if (temp == target):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):   
                multiplier += 1
        start_space[0] += 1
        start_space[1] += 1

    # check diag, positive slope, 1
    start_space = [coords[0]+(target-1), coords[1]-(target-1)]
    for i in range(target):
        if start_space[0] < len(board) and start_space[0] >= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp = 0
            if (start_space[0]-(target-1) >= 0 and start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0]-j, start_space[1]+j] == ans:
                        temp += 1
            if (temp == target):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):   
                multiplier += 1
        start_space[0] -= 1
        start_space[1] += 1

    ans = -1
    # check vert, -1
    start_space = [coords[0]-(target-1), coords[1]]
    for i in range(target):
        if start_space[0] >= 0 and start_space[0] <= coords[0]:
            temp = 0
            if (start_space[0]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0]+j, start_space[1]] == ans:
                        temp += 1
            if (temp == target):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):   
                multiplier += 1
        start_space[0] += 1

    # check horiz, -1
    start_space = [coords[0], coords[1]-(target-1)]
    for i in range(target):
        if start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp = 0
            if (start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0], start_space[1]+j] == ans:
                        temp += 1
            if (temp == target):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):   
                multiplier += 1
        start_space[1] += 1
    
    # check diag, negative slope, -1
    start_space = [coords[0]-(target-1), coords[1]-(target-1)]
    for i in range(target):
        if start_space[0] >= 0 and start_space[0] <= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp = 0
            if (start_space[0]+(target-1) < len(board) and start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0]+j, start_space[1]+j] == ans:
                        temp += 1
            if (temp == target):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):   
                multiplier += 1
        start_space[0] += 1
        start_space[1] += 1

    # check diag, positive slope, -1
    start_space = [coords[0]+(target-1), coords[1]-(target-1)]
    for i in range(target):
        if start_space[0] < len(board) and start_space[0] >= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp = 0
            if (start_space[0]-(target-1) >= 0 and start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0]-j, start_space[1]+j] == ans:
                        temp += 1
            if (temp == target):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):   
                multiplier += 1
        start_space[0] -= 1
        start_space[1] += 1


    return max_util+(multiplier/(multiplier+1))

# board = np.zeros((3, 3))
# print(len(board))
# board[0, 0] = -1
# board[0, 1] = 1
# board[1, 1] = 1
# board[2, 1] = -1
# print(board)

# #checking for vertical wins
# print(heuristic(board, 3, [2, 1]))

# board = np.zeros((4, 4))
# board[3, 2] = 1
# board[0, 2] = -1
# board[1, 1] = -1
# board[1, 2] = 1
# board[2, 0] = 1
# board[2, 1] = -1
# board[2, 2] = 1
# print(board)

# #checking for vertical wins
# print(heuristic(board, 3, [3, 2]))