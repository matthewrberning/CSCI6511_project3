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
    #print("checking for vertical")
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
                return True
                #found = True
                #print("found at", start_space)
                #break
        start_space[0] += 1

    # check for horizontal win
    #print("checking for horizontal")
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
                return True
                #found = True
                #print("found at", start_space)
                #break
        start_space[1] += 1
    
    # check for diagonal win, negative slope
    #print("checking for diagonal, negative slope")
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
                return True
                #found = True
                #print("found at", start_space)
                #break
        start_space[0] += 1
        start_space[1] += 1

    # check for diagonal win, positive slope
    # print("checking for diagonal, positive slope")
    start_space = [coords[0]+(target-1), coords[1]-(target-1)]
    for i in range(target):
        #print("start space:", start_space)
        if start_space[0] < len(board) and start_space[0] >= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp_found = True
            #print("reach:", start_space[0]-(target-1), ",", start_space[1]+(target-1))
            if (start_space[0]-(target-1) >= 0 and start_space[1]+(target-1) < len(board)):
                #print("Entered")
                for j in range(target):
                    #print("curr space = ", start_space[0]-j, ",", start_space[1]+j)
                    if board[start_space[0]-j, start_space[1]+j] != ans:
                        temp_found = False
            else: 
                temp_found = False
            if (temp_found):
                return True
        start_space[0] -= 1
        start_space[1] += 1
    return False


# MAIN SCRIPT
# Test 1: 1x1 board, game won
board = np.zeros((1, 1))
board[0, 0] = 1
if (get_game_state(board, 1, [0, 0]) == True):
    print("Test 1: PASSED")
else:
    print("Test 1: FAILED")
# Test 2: 5x5 board, small target, game won, horizontal on top edge
board = np.zeros((5, 5))
board[1, 0] = 1
board[2, 0] = 1
board[3, 0] = 1
if (get_game_state(board, 3, [1, 0]) == True):
    print("Test 2: PASSED")
else:
    print("Test 2: FAILED")
# Test 3: 5x5 board, small target, game won, horizontal on bottom edge
board = np.zeros((5, 5))
board[1, 4] = 1
board[2, 4] = 1
board[3, 4] = 1
if (get_game_state(board, 3, [1, 4]) == True):
    print("Test 3: PASSED")
else:
    print("Test 3: FAILED")
# Test 4: 5x5 board, small target, game won, horizontal in center
board = np.zeros((5, 5))
board[1, 2] = 1
board[2, 2] = 1
board[3, 2] = 1
if (get_game_state(board, 3, [1, 2]) == True):
    print("Test 4: PASSED")
else:
    print("Test 4: FAILED")
# Test 5: 5x5 board, small target, game won, vertical on left edge
board = np.zeros((5, 5))
board[0, 1] = 1
board[0, 2] = 1
board[0, 3] = 1
if (get_game_state(board, 3, [0, 2]) == True):
    print("Test 5: PASSED")
else:
    print("Test 5: FAILED")
# Test 6: 5x5 board, small target, game won, vertical on right edge
board = np.zeros((5, 5))
board[4, 1] = 1
board[4, 2] = 1
board[4, 3] = 1
if (get_game_state(board, 3, [4, 2]) == True):
    print("Test 6: PASSED")
else:
    print("Test 6: FAILED")    
# Test 7: 5x5 board, small target, game won, vertical in center
board = np.zeros((5, 5))
board[2, 1] = 1
board[2, 2] = 1
board[2, 3] = 1
if (get_game_state(board, 3, [2, 2]) == True):
    print("Test 7: PASSED")
else:
    print("Test 7: FAILED")
# Test 8: 5x5 board, small target, game won, diagonal, negative slope
board = np.zeros((5, 5))
board[1, 1] = 1
board[2, 2] = 1
board[3, 3] = 1
if (get_game_state(board, 3, [2, 2]) == True):
    print("Test 8: PASSED")
else:
    print("Test 8: FAILED")
# Test 9: 5x5 board, small target, game won, diagonal, positive slope
board = np.zeros((5, 5))
board[3, 1] = 1
board[2, 2] = 1
board[1, 3] = 1
if (get_game_state(board, 3, [2, 2]) == True):
    print("Test 9: PASSED")
else:
    print("Test 9: FAILED")
# Test 10: 5x5 board, small target, game ALMOST won, horizontal on top edge
board = np.zeros((5, 5))
board[1, 0] = 1
board[3, 0] = 1
if (get_game_state(board, 3, [1, 0]) == False):
    print("Test 10: PASSED")
else:
    print("Test 10: FAILED")
# Test 11: 5x5 board, small target, game ALMOST won, horizontal on bottom edge
board = np.zeros((5, 5))
board[1, 4] = 1
board[2, 4] = 1
if (get_game_state(board, 3, [1, 4]) == False):
    print("Test 11: PASSED")
else:
    print("Test 11: FAILED")
# Test 12: 5x5 board, small target, game ALMOST won, horizontal in center
board = np.zeros((5, 5))
board[2, 2] = 1
board[3, 2] = 1
if (get_game_state(board, 3, [2, 2]) == False):
    print("Test 12: PASSED")
else:
    print("Test 12: FAILED")
# Test 13: 5x5 board, small target, game ALMOST won, vertical on left edge
board = np.zeros((5, 5))
board[0, 2] = 1
board[0, 3] = 1
if (get_game_state(board, 3, [0, 2]) == False):
    print("Test 13: PASSED")
else:
    print("Test 13: FAILED")
# Test 14: 5x5 board, small target, game ALMOST won, vertical on right edge
board = np.zeros((5, 5))
board[4, 1] = 1
board[4, 2] = 1
if (get_game_state(board, 3, [4, 2]) == False):
    print("Test 14: PASSED")
else:
    print("Test 14: FAILED")
# Test 15: 5x5 board, small target, game ALMOST won, vertical in center
board = np.zeros((5, 5))
board[2, 1] = 1
board[2, 3] = 1
if (get_game_state(board, 3, [2, 3]) == False):
    print("Test 15: PASSED")
else:
    print("Test 15: FAILED")
# Test 16: 5x5 board, small target, game ALMOST won, diagonal, negative slope
board = np.zeros((5, 5))
board[1, 1] = 1
board[3, 3] = 1
if (get_game_state(board, 3, [1, 1]) == False):
    print("Test 16: PASSED")
else:
    print("Test 16: FAILED")
# Test 17: 5x5 board, small target, game ALMOST won, diagonal, positive slope
board = np.zeros((5, 5))
board[3, 1] = 1
board[1, 3] = 1
if (get_game_state(board, 3, [3, 1]) == False):
    print("Test 17: PASSED")
else:
    print("Test 17: FAILED")
# Test 18: 5x5 board, full target, game won, horizontal on top edge
board = np.zeros((5, 5))
board[0, 0] = 1
board[1, 0] = 1
board[2, 0] = 1
board[3, 0] = 1
board[4, 0] = 1
if (get_game_state(board, 5, [1, 0]) == True):
    print("Test 18: PASSED")
else:
    print("Test 18: FAILED")
# Test 19: 5x5 board, full target, game won, horizontal on bottom edge
board = np.zeros((5, 5))
board[0, 4] = 1
board[1, 4] = 1
board[2, 4] = 1
board[3, 4] = 1
board[4, 4] = 1
if (get_game_state(board, 5, [4, 4]) == True):
    print("Test 19: PASSED")
else:
    print("Test 19: FAILED")
# Test 20: 5x5 board, full target, game won, horizontal in center
board = np.zeros((5, 5))
board[0, 2] = 1
board[1, 2] = 1
board[2, 2] = 1
board[3, 2] = 1
board[4, 2] = 1
if (get_game_state(board, 5, [2, 2]) == True):
    print("Test 20: PASSED")
else:
    print("Test 20: FAILED")
# Test 21: 5x5 board, full target, game won, vertical on left edge
board = np.zeros((5, 5))
board[0, 0] = 1
board[0, 1] = 1
board[0, 2] = 1
board[0, 3] = 1
board[0, 4] = 1
if (get_game_state(board, 5, [0, 2]) == True):
    print("Test 21: PASSED")
else:
    print("Test 21: FAILED")
# Test 22: 5x5 board, full target, game won, vertical on right edge
board = np.zeros((5, 5))
board[4, 0] = 1
board[4, 1] = 1
board[4, 2] = 1
board[4, 3] = 1
board[4, 4] = 1
if (get_game_state(board, 5, [4, 2]) == True):
    print("Test 22: PASSED")
else:
    print("Test 22: FAILED")
# Test 23: 5x5 board, full target, game won, vertical in center
board = np.zeros((5, 5))
board[2, 0] = 1
board[2, 1] = 1
board[2, 2] = 1
board[2, 3] = 1
board[2, 4] = 1
if (get_game_state(board, 5, [2, 2]) == True):
    print("Test 21: PASSED")
else:
    print("Test 21: FAILED")
# Test 24: 5x5 board, full target, game won, diagonal, negative slope
board = np.zeros((5, 5))
board[0, 0] = 1
board[1, 1] = 1
board[2, 2] = 1
board[3, 3] = 1
board[4, 4] = 1
if (get_game_state(board, 5, [2, 2]) == True):
    print("Test 24: PASSED")
else:
    print("Test 24: FAILED")
# Test 25: 5x5 board, full target, game won, diagonal, positive slope
board = np.zeros((5, 5))
board[4, 0] = 1
board[3, 1] = 1
board[2, 2] = 1
board[1, 3] = 1
board[0, 4] = 1
if (get_game_state(board, 5, [2, 2]) == True):
    print("Test 25: PASSED")
else:
    print("Test 25: FAILED")
# Test 26: 5x5 board, full target, game ALMOST won, horizontal on top edge
board = np.zeros((5, 5))
board[0, 0] = 1
board[1, 0] = 1
board[2, 0] = 1
board[3, 0] = 1
board[4, 0] = 1
if (get_game_state(board, 5, [0, 0]) == True):
    print("Test 26: PASSED")
else:
    print("Test 26: FAILED")
# Test 27: 5x5 board, full target, game ALMOST won, horizontal on bottom edge
board = np.zeros((5, 5))
board[1, 4] = 1
board[2, 4] = 1
board[3, 4] = 1
board[4, 4] = 1
if (get_game_state(board, 5, [4, 4]) == False):
    print("Test 27: PASSED")
else:
    print("Test 27: FAILED")
# Test 28: 5x5 board, full target, game ALMOST won, horizontal in center
board = np.zeros((5, 5))
board[0, 2] = 1
board[2, 2] = 1
board[3, 2] = 1
board[4, 2] = 1
if (get_game_state(board, 5, [2, 2]) == False):
    print("Test 28: PASSED")
else:
    print("Test 28: FAILED")
# Test 29: 5x5 board, full target, game ALMOST won, vertical on left edge
board = np.zeros((5, 5))
board[0, 0] = 1
board[0, 2] = 1
board[0, 3] = 1
board[0, 4] = 1
if (get_game_state(board, 5, [0, 2]) == False):
    print("Test 29: PASSED")
else:
    print("Test 29: FAILED")
# Test 30: 5x5 board, full target, game ALMOST won, vertical on right edge
board = np.zeros((5, 5))
board[4, 0] = 1
board[4, 1] = 1
board[4, 2] = 1
board[4, 4] = 1
if (get_game_state(board, 5, [4, 4]) == False):
    print("Test 22: PASSED")
else:
    print("Test 22: FAILED")
# Test 31: 5x5 board, full target, game ALMOST won, vertical in center
board = np.zeros((5, 5))
board[2, 1] = 1
board[2, 2] = 1
board[2, 3] = 1
board[2, 4] = 1
if (get_game_state(board, 5, [2, 2]) == False):
    print("Test 31: PASSED")
else:
    print("Test 31: FAILED")
# Test 32: 5x5 board, full target, game ALMOST won, diagonal, negative slope
board = np.zeros((5, 5))
board[0, 0] = 1
board[1, 1] = 1
board[3, 3] = 1
board[4, 4] = 1
if (get_game_state(board, 5, [1, 1]) == False):
    print("Test 32: PASSED")
else:
    print("Test 32: FAILED")
# Test 33: 5x5 board, full target, game ALMOST won, diagonal, positive slope
board = np.zeros((5, 5))
board[4, 0] = 1
board[3, 1] = 1
board[2, 2] = 1
board[0, 4] = 1
if (get_game_state(board, 5, [2, 2]) == False):
    print("Test 33: PASSED")
else:
    print("Test 33: FAILED")

# board = np.zeros((5, 5))
# print(len(board))
# board[4, 4] = 1
# board[3, 1] = 1
# board[1, 3] = 1
# board[2, 2] = 1
# print(board)

# #checking for vertical wins
# print(get_game_state(board, 3, [2, 2]))