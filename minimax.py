# from game import Board

c = 0
def minimax(board, depth, maximizer, point=None, alpha=float("-inf"), beta=float("inf")):
    """
    minimax algorithm to find most optimal move in a game of TTT.
    board- the game board you are playing on
    depth- depth limited recursion
    maximizer- if it is the maximizers turn
    point- should be none on initial call. the tentative point to add to the board
    """
    global c
    c+=1

    print("booooard:   ",board)

    if board.isEmpty() or board.board[board.middle_point][board.middle_point]:
        return float("inf"), (board.middle_point, board.middle_point)
    
    # add the tentative point to the board(currently just used to close off spaces)
    # but can be encorporated into a heuristic based on which agent has chosen a space
    if point: # on all other calls    
        board.add_symbol( (point[0], point[1]), 1 if maximizer else -1)
    else: # first call
        point = (0,0)
        
    # max depth reached, or the board is filled up
    if depth == 0 or board.isFull():
        return heuristic(board, point), point

    # find all possible moves
    children = board.get_open_spaces()

    # maximizer turn
    if maximizer:
        value = float("-inf")
        for child in children:
            value, point = my_max( value, minimax( board, depth - 1, not maximizer, (child[0], child[1]), alpha, beta )[0], point, tuple(child) )
            alpha = max(value, alpha)
            board.remove_symbol( (child[0], child[1]) )

            if beta <= alpha:
                break
        return value, point
    # minimizer turn
    else:
        value = float("inf")
        for child in children:
            value, point = my_min( value, minimax( board, depth - 1, not maximizer, (child[0], child[1]),alpha, beta )[0], point, tuple(child) )
            beta = min(value, beta)
            board.remove_symbol( (child[0], child[1]) )

            if beta <= alpha:
                break
        return value, point

# 0 on agent 1 win, 1 on agent 2 win, 2 on tie, -1 on continuing
# agent 1 will be represented by 1's, agent 2 will be -1's
# @param coords: the coordinates of the most recently placed mark, represented as a 1x2 np arr
def heuristic(board_obj, coords):
    # use the coords of the last turn to determine if we are looking for 1 or -1
    ans = 0
    target = board_obj.target
    board = board_obj.board

    if (board[coords[0], coords[1]] == 1):
        ans = 1
    elif (board[coords[0], coords[1]] == -1):
        ans = -1
    else:
        print("ERROR: Checking in unmarked square.")
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


def my_max(value1, value2, point1, point2):
    if value2 > value1:
        return value2, point2
    else:
        return value1, point1

def my_min(value1, value2, point1, point2):
    if value2 < value1:
        return value2, point2
    else:
        return value1, point1

# test code :)'
# n = 3
# b = Board(n,3)
# symbol = 1
# its = 0
# while 1:
#     its += 1
#     last_point = minimax(b, 2, True)[1]
#     b.add_symbol(last_point, 1 if symbol else -1)

#     if b.check_win_con(last_point):
#         print(b)

#         break

#     symbol = not symbol 
#     print(b)
# print(c, its)