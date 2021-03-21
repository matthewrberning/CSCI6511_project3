from game import Board

c = 0
def minimax(board, depth, maximizer, point=None, alpha=float("-inf"), beta=float("inf")):
    """
    minimax algorithm to find most optimal move in a game of TTT.
    board- the game board you are playing on
    depth- depth limited recursion
    maximizer- if it is the maximizers turn
    point- should be none on initial call
    """
    global c
    c+=1

    # max depth reached, or the board is filled up
    if depth == 0 or board.isFull():
        return heuristic(board, point), point

    # add the tentative point to the board(currently just used to close off spaces)
    # but can be encorporated into a heuristic based on which agent has chosen a space
    if point: # on all other calls    
        board.add_symbol( (point[0], point[1]), 1 if maximizer else -1)
    else: # first call
        point = (0,0)

    # find all possible moves
    children = board.get_open_spaces()

    # maximizer turn
    if maximizer:
        value = float("-inf")
        for child in children:
            # value = int( max( value, minimax( board, depth - 1, not maximizer, (child[0], child[1]) ) ) )
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
            # value = int( min( value, minimax( board, depth - 1, not maximizer, (child[0], child[1]) ) ) )
            value, point = my_min( value, minimax( board, depth - 1, not maximizer, (child[0], child[1]),alpha, beta )[0], point, tuple(child) )
            beta = min(value, beta)
            board.remove_symbol( (child[0], child[1]) )

            if beta <= alpha:
                break
        return value, point


def heuristic(board: Board, point: tuple):
    return point[0] + point[1]


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
n = 10
b = Board(n,n)
symbol = 1
while not b.isFull():
    b.add_symbol(minimax(b, 2, True)[1], 1 if symbol else -1)
    symbol = not symbol 
    print(b)
print(c)