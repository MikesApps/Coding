"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    turn = 0 

    for row in board:
        for cell in row:
            if cell == 'X':
                turn += 1
            elif cell == 'O':
                turn -= 1
    if turn == 1:
        return 'O'
    else:
        return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allactions = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                allactions.add((row,col))
    return allactions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    r, c = action
    print(r, c, 'R AND C ARE')
    if board[r][c] is not None:
        raise Exception('Illegal', 'Move')
    newboard = copy.deepcopy(board)
    newboard[r][c] = player(board)
    return newboard
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
   
    for i in range(0,3):
         # Check Rows
        if (board[i][0] == board[i][1] == board [i][2]) and board[i][0] is not None:
            return board[i][0]

         # Check Cols
        if (board[0][i] == board[1][i] == board [2][i]) and board[0][i] is not None:
            return board[0][i]
        
        #diags
        if( board[0][0] == board[1][1] == board[2][2]) and board[0][0] is not None:
            return board[0][0]
        if (board[0][2] == board[1][1] == board [2][0]) and board [1][1] is not None:
            return board[1][1]
    return None

def winnerEval(board):
    """
    Returns the winner of the game, if there is one.
    """
    play = player(board)
    win = None
    for i in range(0,3):
         # Check Rows
        if (board[i][0] == board[i][1] == board [i][2]) and board[i][0] is not None:
            win =  board[i][0]

         # Check Cols
        if (board[0][i] == board[1][i] == board [2][i]) and board[0][i] is not None:
            win = board[0][i]
        
        #diags
        if( board[0][0] == board[1][1] == board[2][2]) and board[0][0] is not None:
            win =  board[0][0]
        if (board[0][2] == board[1][1] == board [2][0]) and board [1][1] is not None:
            win = board[1][1]
    if win == None:
        return 0
    elif win == 'X':
        return 1
    else:
        return -1





def terminal(board):
    """
    Returns True if game is over, False otherwise. 
    """
    return winner(board) is not None or len(actions(board)) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0








def minimax(board, depth, playa = 32):
    play = player(board)
    if play == 'X':
        best = [-1, -1, -2]
    else:
        best = [-1, -1, 2]

    if terminal(board):
        score = winnerEval(board)
        return [-1, -1, score]

    for cell in actions(board):
        x, y = cell
        board[x][y] = play
        score = minimax(board, depth - 1, -playa)
        board[x][y] = None
        score[0], score[1] = x, y

        if play == 'X':
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best



boards =    [[None, None, None],
            ['X', 'X', 'X'],
            ['O', 'O', 'O']]
print(minimax(boards, 0, 32))


#print(winner(boards))

#print(player(boards))