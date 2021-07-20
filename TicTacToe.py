board = {0: " ", 1: " ", 2: " ",
         3: " ", 4: " ", 5: " ",
         6: " ", 7: " ", 8: " "}
choice = {0: "0", 1: "1", 2: "2",
          3: "3", 4: "4", 5: "5",
          6: "6", 7: "7", 8: "8"}

def printGameBoard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print('-+-+-')
    print(board[3] + "|" + board[4] + "|" + board[5])
    print('-+-+-')
    print(board[6] + "|" + board[7] + "|" + board[8])

def printChoice():
    print(choice[0] + "|" + choice[1] + "|" + choice[2])
    print('-+-+-')
    print(choice[3] + "|" + choice[4] + "|" + choice[5])
    print('-+-+-')
    print(choice[6] + "|" + choice[7] + "|" + choice[8])

def check_win(move):
    # check horizontals
    if (board[0] == move and board[1] == move and board[2] == move):
        return True
    elif (board[3] == move and board[4] == move and board[5] == move):
        return True
    elif (board[6] == move and board[7] == move and board[8] == move): 
        return True
    # check verticals
    elif (board[0] == move and board[3] == move and board[6] == move): 
        return True
    elif (board[1] == move and board[4] == move and board[7] == move): 
        return True
    elif (board[2] == move and board[5] == move and board[8] == move): 
        return True
    # check diagonals
    elif (board[0] == move and board[4] == move and board[8] == move): 
        return True
    elif (board[2] == move and board[4] == move and board[6] == move): 
        return True
    return False

def game():
    turn = "X"
    counter = 0 # to check who's move it is
    for i in range(10):
        if counter == 9:
            print("Game over, its a tie!")
            break
        if counter % 2 == 0:
            turn = "X"
        else:
            turn = "O"
        move = int(input("It's your turn " + turn + ", please make your move: "))
        if board[move] == "X" or board[move] == "O": # check for wrong input
            print("That box has already been taken.")
            continue
        else:
            board[move] = turn
            counter += 1
            printGameBoard()
            print("=====")
            printChoice()
            if check_win("X"):
                print("*** X won! ***")
                break
            elif check_win("O"):
                print("*** O won! ***")
                break
print("Welcome to tic tac toe!\n" + "To play this game, please enter a number for the box you would like to choose.")
printChoice()
print("=====")
game()
        