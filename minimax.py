def minimax(board, depth, maximizer, point=None):
    """
    minimax algorithm to find most optimal move in a game of TTT.
    board- the game board you are playing on
    depth- depth limited recursion
    maximizer- if it is the maximizers turn
    point- should be none on initial call
    """

    # max depth reached, or the board is filled up
    if depth == 0 or board.isFull():
        return heuristic(point), point

    # add the tentative point to the board(currently just used to close off spaces)
    # but can be encorporated into a heuristic based on which agent has chosen a space
    if point: # on all other calls
        board.add_symbol( (point[0], point[1]), 1 if maximizer else -1 )
    else: # first call
        point = (0,0)

    # find all possible moves
    children = board.get_open_spaces()

    # maximizer turn
    if maximizer:
        value = float("-inf")
        for child in children:
            # value = int( max( value, minimax( board, depth - 1, not maximizer, (child[0], child[1]) ) ) )
            value, point = my_max( value, minimax( board, depth - 1, not maximizer, (child[0], child[1]) )[0], point, tuple(child) )
            board.remove_symbol( (child[0], child[1]) )
        return value, point
    # minimizer turn
    else:
        value = float("inf")
        for child in children:
            # value = int( min( value, minimax( board, depth - 1, not maximizer, (child[0], child[1]) ) ) )
            value, point = my_min( value, minimax( board, depth - 1, not maximizer, (child[0], child[1]) )[0], point, tuple(child) )
            board.remove_symbol( (child[0], child[1]) )
        return value, point


def heuristic(point: tuple):
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

# test code :)
# b = Board(10,10)
# symbol = 1
# c = 0
# while not b.isFull():
#     b.add_symbol(minimax(b, 2, True)[1], 1 if symbol else -1)
#     symbol = not symbol
#     c+=1
#     print(b)
# print(c)