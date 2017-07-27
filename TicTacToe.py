# TIC-TAC-TOE 2 player game

# empty board
board = [0, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# index 0 is player 1, #pieces[0] is player 1's marker/piece and so on
pieces = ['', '']
# positions of the board
availablePositions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_board(currentBoard):
    print('   |    |')
    print(' ' + currentBoard[7] + ' | ' + currentBoard[8] + '  | ' + currentBoard[9])
    print('   |    |')
    print('------------')
    print('   |    |')
    print(' ' + currentBoard[4] + ' | ' + currentBoard[5] + '  | ' + currentBoard[6])
    print('   |    |')
    print('------------')
    print('   |    |')
    print(' ' + currentBoard[1] + ' | ' + currentBoard[2] + '  | ' + currentBoard[3])
    print('   |    |')
    print('')

# describes the positioning of the board
def print_rules():
    print('This is the positioning. ')
    print(str(7) + ' ' + str(8) + ' ' + str(9))
    print(str(4) + ' ' + str(5) + ' ' + str(6))
    print(str(1) + ' ' + str(2) + ' ' + str(3))
    print('')

# prints the available positions
def print_available_positions(availablePositions):
    print('The available positions are:')
    print(availablePositions)
    print('')

# runs the game
def play_game():
    keepPlaying = True
    playerPieces = player_assignment()
    while keepPlaying:
        currentBoard = [0, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        possiblePositions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print_board(currentBoard)
        winner = round(currentBoard, possiblePositions, playerPieces)
        if winner == False:
            print("There was a tie!\n")
        elif winner == 1:
            print("Player 1 wins!\n")
        else:
            print("Player 2 wins!\n")
        # asks the user if they want to replay
        playAgain = raw_input("Another game? Press 'Y' to play again. ")
        if playAgain.upper() != 'Y':
            keepPlaying = False

# checks if there is a winner, after player chooses
def win_check(currentBoard, mark):
    # row check, col check, and diagonal check
    return currentBoard[7] == mark and currentBoard[8] == mark and currentBoard[9] == mark or \
           currentBoard[1] == mark and currentBoard[2] == mark and currentBoard[3] == mark or \
           currentBoard[4] == mark and currentBoard[5] == mark and currentBoard[6] == mark or \
           currentBoard[1] == mark and currentBoard[4] == mark and currentBoard[7] == mark or \
           currentBoard[2] == mark and currentBoard[5] == mark and currentBoard[8] == mark or \
           currentBoard[3] == mark and currentBoard[6] == mark and currentBoard[9] == mark or \
           currentBoard[1] == mark and currentBoard[5] == mark and currentBoard[9] == mark or \
           currentBoard[3] == mark and currentBoard[5] == mark and currentBoard[7] == mark

# gets the position from the user, through inputs
# param: the number of the player (1 or 2) & current board
def get_user_input(playerNumber, currentBoard, availablePositions):
    # position needs to be int, cannot be used up, has to be within range
    print_available_positions(availablePositions)
    while True:
        try:
            position = int(raw_input('Player ' + str(playerNumber + 1) + ' where would you like to place your marker? '))
        except ValueError:
            print('Please pick an available position. ')
            print_available_positions(availablePositions)
            continue
        else:
            if position < 1 or position > 9 or currentBoard[position] != ' ':
                print ('Please pick an available position. ')
                print_available_positions(availablePositions)
                continue
            break
    return position

# runs the round
# param: current board
def round(currentBoard, availablePositions, playerPieces):
    counter = 0
    # continue the game as long as there is not a tie
    while not check_full(availablePositions):
        if counter == 2:
            counter = 0
        position = get_user_input(counter, currentBoard, availablePositions)
        place_marker(currentBoard, counter, position, playerPieces)
        # remove the current position from the available
        availablePositions.remove(position)
        print_board(currentBoard)
        if win_check(currentBoard, playerPieces[counter]) or check_full(availablePositions):
            break
        else:
            counter = counter + 1
    # check if winner or tie
    if check_full(availablePositions):
        return False
    # there is a winner, return their player #
    return counter

# checks if the board is full
# param: current board
def check_full(availablePositions):
    return len(availablePositions) == 0

# assigns pieces to player 1 and 2
def player_assignment():
    choice1 = raw_input('Player 1, what piece do you want? ')
    while choice1 == ' ' or choice1 == '':
        choice1 = raw_input('Please pick a better, piece: ')
    choice2 = raw_input('Player 2, what piece do you want? ')
    while choice1 == ' ' or choice1 == '' or choice2 == choice1:
        choice2 = raw_input('Please pick a better, piece: ')
    return [choice1, choice2]

# edits the current board to contain the specific piece of the current player
# param: current board, player number, position to place marker
def place_marker(currentBoard, player, position, playerPieces):
    # pieces[player] gets the marker/piece
    currentBoard[position] = playerPieces[player]

print('Welcome to Tic-Tac-Toe!')
print_rules()
play_game()
