from game import Board
def minimax(board, depth, maximizer, point=None):
    if depth == 0 or board.isFull():
        return heuristic(point), point

    if point:
        board.add_symbol( (point[0], point[1]), 1 if maximizer else -1 )
    else:
        point = (0,0)

    children = board.get_open_spaces()

    if maximizer:
        value = float("-inf")
        for child in children:
            # value = int( max( value, minimax( board, depth - 1, not maximizer, (child[0], child[1]) ) ) )
            value, point = my_max( value, minimax( board, depth - 1, not maximizer, (child[0], child[1]) )[0], point, tuple(child) )
            board.remove_symbol( (child[0], child[1]) )
        return value, point
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
#     print(b.board)
