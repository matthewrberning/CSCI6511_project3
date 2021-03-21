import numpy as np

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

    # check for vertical win
    print("checking for vertical")
    found = False
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
                found = True
                print("found at", start_space)
                break
        start_space[0] += 1

    # check for horizontal win
    print("checking for horizontal")
    start_space = [coords[0], coords[1]-(target-1)]
    for i in range(target):
        #print("start space:", start_space)
        if start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp_found = True
            if (start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0], start_space[1]+j] != ans:
                        temp_found = False
            else: 
                temp_found = False
            if (temp_found):
                found = True
                print("found at", start_space)
                break
        start_space[1] += 1
    
    # check for diagonal win, negative slope
    print("checking for diagonal, negative slope")
    start_space = [coords[0]-(target-1), coords[1]-(target-1)]
    for i in range(target):
        #print("start space:", start_space)
        if start_space[0] >= 0 and start_space[0] <= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp_found = True
            if (start_space[0]+(target-1) < len(board) and start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    if board[start_space[0]+j, start_space[1]+j] != ans:
                        temp_found = False
            else: 
                temp_found = False
            if (temp_found):
                found = True
                print("found at", start_space)
                break
        start_space[0] += 1
        start_space[1] += 1

    # check for diagonal win, positive slope
    print("checking for diagonal, positive slope")
    start_space = [coords[0]+(target-1), coords[1]-(target-1)]
    for i in range(target):
        print("start space:", start_space)
        if start_space[0] >= 0 and start_space[0] >= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp_found = True
            if (start_space[0]-(target-1) >= 0 and start_space[1]+(target-1) < len(board)):
                for j in range(target):
                    #print(" now at:", start_space[0]-j, ",", start_space[1]+j)
                    if board[start_space[0]-j, start_space[1]+j] != ans:
                        temp_found = False
            else: 
                temp_found = False
            if (temp_found):
                found = True
                print("found at", start_space)
                break
        start_space[0] -= 1
        start_space[1] += 1
    print(found)
    return False


# MAIN SCRIPT
# Test 1: 1x1 board, game won
board = np.zeros((1, 1))
board[0, 0] = 1
get_game_state(board, 1, [0, 0])
# Test 2: 5x5 board, small target, game won, horizontal on top edge
board = np.zeros((5, 5))
# Test 3: 5x5 board, small target, game won, horizontal on bottom edge
board = np.zeros((5, 5))
# Test 4: 5x5 board, small target, game won, horizontal in center
board = np.zeros((5, 5))
# Test 5: 5x5 board, small target, game won, vertical on left edge
board = np.zeros((5, 5))
# Test 6: 5x5 board, small target, game won, vertical on right edge
board = np.zeros((5, 5))
# Test 7: 5x5 board, small target, game won, vertical in center
board = np.zeros((5, 5))
# Test 8: 5x5 board, small target, game won, diagonal, negative slope
board = np.zeros((5, 5))
# Test 9: 5x5 board, small target, game won, diagonal, positive slope
board = np.zeros((5, 5))
# Test 10: 5x5 board, small target, game ALMOST won, horizontal on top edge
board = np.zeros((5, 5))
# Test 11: 5x5 board, small target, game ALMOST won, horizontal on bottom edge
board = np.zeros((5, 5))
# Test 12: 5x5 board, small target, game ALMOST won, horizontal in center
board = np.zeros((5, 5))
# Test 13: 5x5 board, small target, game ALMOST won, vertical on left edge
board = np.zeros((5, 5))
# Test 14: 5x5 board, small target, game ALMOST won, vertical on right edge
board = np.zeros((5, 5))
# Test 15: 5x5 board, small target, game ALMOST won, vertical in center
board = np.zeros((5, 5))
# Test 16: 5x5 board, small target, game ALMOST won, diagonal, negative slope
board = np.zeros((5, 5))
# Test 17: 5x5 board, small target, game ALMOST won, diagonal, positive slope
board = np.zeros((5, 5))




# Test 18: 5x5 board, full target, game won, horizontal on top edge
# Test 19: 5x5 board, full target, game won, horizontal on bottom edge
# Test 20: 5x5 board, full target, game won, horizontal in center
# Test 21: 5x5 board, full target, game won, vertical on left edge
# Test 22: 5x5 board, full target, game won, vertical on right edge
# Test 23: 5x5 board, full target, game won, vertical in center
# Test 24: 5x5 board, full target, game won, diagonal, negative slope
# Test 25: 5x5 board, full target, game won, diagonal, positive slope
# Test 26: 5x5 board, full target, game ALMOST won, horizontal on top edge
# Test 27: 5x5 board, full target, game ALMOST won, horizontal on bottom edge
# Test 28: 5x5 board, full target, game ALMOST won, horizontal in center
# Test 29: 5x5 board, full target, game ALMOST won, vertical on left edge
# Test 30: 5x5 board, full target, game ALMOST won, vertical on right edge
# Test 31: 5x5 board, full target, game ALMOST won, vertical in center
# Test 32: 5x5 board, full target, game ALMOST won, diagonal, negative slope
# Test 33: 5x5 board, full target, game ALMOST won, diagonal, positive slope

board = np.zeros((5, 5))
print(len(board))
board[4, 4] = 1
board[3, 1] = 1
board[1, 3] = 1
board[2, 2] = 1
print(board)

# checking for vertical wins
get_game_state(board, 3, [2, 2])