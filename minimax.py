from board import Board
import numpy as np
import math

def get_best_move(board, depth, maximizer):
    children = sorted(board.get_open_spaces(), key=lambda x: space_sort(board, x, maximizer), reverse=True)

    best_move = None
    best_value = float("-inf")

    if (board.board[board.middle][board.middle] == 0): 
        return board.middle,board.middle
        
    for idx, child in enumerate(children):
        board.add_symbol(child, 1 if maximizer else -1)

        
        minimax_result = minimax(board, depth, False)

        board.remove_symbol(child)

        if minimax_result > best_value:
            best_value = minimax_result
            best_move = child
    return best_move

def minimax(board, depth, maximizer, alpha=float("-inf"), beta=float("inf"), point=None):
    """
    minimax algorithm to find most optimal move in a game of TTT.
    board- the game board you are playing on
    depth- depth limited recursion
    maximizer- if it is the maximizers turn
    point- should be none on initial call. the tentative point to add to the board
    """
    # if board.isFull():
    #     return -1, point 
    

    # if depth == 0 or board.isFull():
    #     # return heuristic(board, maximizer, depth), point
    #     return abs(heuristic(board, point, maximizer)), point
    h = heuristic(board)
    if abs(h) == board.total_spaces or depth==0:
        return h

    if board.isFull():
        return 0

    # next possible moves, sorting by how we greedily evaluate the move
    children = sorted(board.get_open_spaces(), key=lambda x: space_sort(board, x, maximizer), reverse=True)


    # maximizer turn
    if maximizer:
        value = float("-inf")
        for child in children:
            board.add_symbol(child, 1)
            value = max(minimax( board, depth - 1, not maximizer, alpha, beta, point=child), value)
            board.remove_symbol(child)
            
            alpha = max(value, alpha)

            if beta <= alpha:
                break
        return value
    # minimizer turn
    else:
        value = float("inf")
        for child in children:
            board.add_symbol(child, -1)
            value = min(minimax( board, depth - 1, not maximizer, alpha, beta, point=child), value)
            board.remove_symbol(child)

            beta = min(value, beta)

            if beta <= alpha:
                break
            
        return value

def heuristic(board_obj):
    n = board_obj.dim; t = board_obj.target
    board = board_obj.board
    for i in range(n):
        row = board[i]
        col = board[:, i]
        if np.count_nonzero(row == 1) == t-1 : 
            return board_obj.total_spaces
        elif np.count_nonzero(row == -1) == t-1:
            return -board_obj.total_spaces
        if np.count_nonzero(col == 1) == t-1 : 
            return board_obj.total_spaces
        elif np.count_nonzero(col == -1) == t-1:
            return -board_obj.total_spaces
    #Todo diagonals
    return 0
        
# 0 on agent 1 win, 1 on agent 2 win, 2 on tie, -1 on continuing
# agent 1 will be represented by 1's, agent 2 will be -1's
# @param coords: the coordinates of the most recently placed mark, represented as a 1x2 np arr
def space_sort(board_obj, coords, maximizer):
    target = board_obj.target
    board = board_obj.board
    # use the coords of the last turn to determine if we are looking for 1 or -1
    turn = 0
    if (board[coords[0], coords[1]] == 1):
        turn = 1
        #print("its 1 turn")
    elif (board[coords[0], coords[1]] == -1):
        turn = -1
        #print("it's -1 turn")
    else:
        board_obj.add_symbol(coords, 1 if maximizer else -1)
        turn = 1 if maximizer else -1

        # print("ERROR: Checking for win in unmarked square.")
        # exit()
    
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
                board_obj.remove_symbol(coords)
                return temp
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
                board_obj.remove_symbol(coords)
                return temp
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
                board_obj.remove_symbol(coords)
                return temp
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
                board_obj.remove_symbol(coords)
                return temp
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
                board_obj.remove_symbol(coords)
                return temp
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
                board_obj.remove_symbol(coords)
                return temp
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
                board_obj.remove_symbol(coords)
                return temp
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
                board_obj.remove_symbol(coords)
                return temp
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):   
                multiplier += 1
        start_space[0] -= 1
        start_space[1] += 1
    #print("h =", max_util+(multiplier/10))
    board_obj.remove_symbol(coords)
    return max_util+(multiplier/(multiplier+1))
