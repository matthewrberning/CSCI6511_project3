from game import Board
import numpy as np


# agent 1 will be represented by 1's, agent 2 will be -1's
# @param coords: the coordinates of the most recently placed mark, represented as a 1x2 np arr
def check_win_con(coords, board, target):
    """Check if the board at that point(most recent move) has won"""
    # 0 on agent 1 win, 1 on agent 2 win, 2 on tie, -1 on continuing
    # use the coords of the last turn to determine if we are looking for 1 or -1
    
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

##################################
##################################
##################################
##################################


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
        #print("its 1 turn")
    elif (board[coords[0], coords[1]] == -1):
        turn = -1
        #print("it's -1 turn")
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

    #################################
    #################################
    #################################

size = 4
t = 3
b = Board(size, t)
while 1:
    print(b.board)
    # human turn
    entry = input("User turn:")
    u_x = int(entry[0])
    u_y = int(entry[1])
    b.board[u_x][u_y] = -1
    if (check_win_con([u_x, u_y], b.board, t)):
        break
    print(b.board)
    # machine turn
    print("Machine turn:")
    best = [0, 0]
    curr_max = float('-inf')
    for i in range(size):
        for j in range(size):
            if b.board[i][j] == 0:
                b.board[i][j] = 1
                v = heuristic(b.board, t, [i, j])
                if(v > curr_max):
                    best = [i, j]
                    curr_max = v
                b.board[i][j] = 0
    b.board[best[0], best[1]] = 1
    if (check_win_con(best, b.board, t)):
        break
print(b.board)
