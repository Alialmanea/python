import random

board=[' ' for x in range(10)]


def insertLetter(letter,pos):
    board[pos]=letter

def isPositionFree(pos):
    return board[pos] == ' '


def printBoard():
    print('')
    print('   |   |')
    print('' + board[1] + '  |' + board[2] + '  | ' + board[3])
    print('   |   |')
    print('------------')
    print('   |   |')
    print('' + board[4] + '  |' + board[5] + '  | ' + board[6])
    print('   |   |')
    print('-------------')
    print('   |   |')
    print('' + board[7] + '  |' + board[8] + '  | ' + board[9])
    print('   |   |')


def isWinner(board,letter):
    return (board[7] == letter and board[8] == letter and board[9] == letter) or \
           (board[4] == letter and board[5] == letter and board[6] == letter) or \
           (board[1] == letter and board[2] == letter and board[3] == letter) or \
           (board[1] == letter and board[4] == letter and board[7] == letter) or \
           (board[2] == letter and board[5] == letter and board[8] == letter) or \
           (board[3] == letter and board[6] == letter and board[9] == letter) or \
           (board[1] == letter and board[5] == letter and board[9] == letter) or \
           (board[3] == letter and board[5] == letter and board[7] == letter)

def isBoardFull():
    for i in range(1,10):
        if board[i] == ' ':
            return False
    return True


def playMove():
    while True:
        pos =input('please Select a position to place an X  (1 - 9) : ')
        try:
            pos = int (pos)
            if pos > 0 and pos < 10:
                if isPositionFree(pos):
                    insertLetter('X',pos)
                    break
                else:
                    print('Oops ! This {} Position is Occupied '.format(pos))
            else:
                print("please Select a Position within the rang !")

        except:
            print('please Select a position to place an X  (1 - 9)')

def compMove():
    PossibleMove =[x for x,letter in enumerate(board) if letter ==' ' and x !=0]
    move = 0
    for let in ['O', 'X']:
        for i in PossibleMove:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []

    for i in PossibleMove:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = cornersOpen[random.randrange(0,len(cornersOpen))]
        return move

    if 5 in PossibleMove:
        move = 5
        return move

    edgesOpen = []

    for i in PossibleMove:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = cornersOpen[random.randrange(0, len(edgesOpen))]




    return move


def main():
    print('  Tic Tac Toe  ')
    printBoard()

    while not (isBoardFull()):
        if not (isWinner(board, 'O')):
            playMove()
            printBoard()
        else:
            print('The Winner is O !')
            break
        if not (isWinner(board, 'X')):
            mov = compMove()
            if mov == 0:
                print(" Tie Game ")
            else:
                insertLetter('O', mov)
                print("The computer placed O in position {} ".format(mov))
                printBoard()
        else:
            print('The Winner is X ! Great Job !')
            break

    if isBoardFull():
        print('  Tie Game  ')




if __name__ == '__main__':
    main()
