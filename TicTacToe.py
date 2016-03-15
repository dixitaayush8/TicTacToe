def board(bList): #prints the board
    print "\n\t", bList[0], "|", bList[1], "|", bList[2]
    print "\t", "---------"
    print "\t", bList[3], "|", bList[4], "|", bList[5]
    print "\t", "---------"
    print "\t", bList[6], "|", bList[7], "|", bList[8], "\n"

def makePlayerTwoMove(bList,move,letter): #function for making player 2 move
    bList[move] = letter

def inputLetters(): #inputs letters that player 1 and 2 choose. 
    t = ''
    p = str(raw_input('Player 1, Choose a letter (X or Y): '))
    if p == 'X':
        t = 'Y'
    elif p == 'Y':
        t = 'X'
    else:
        while (p != 'X' or p != 'Y') and (t != 'X' or t != 'Y'):
            t = ''
            p = str(raw_input('Player 1, Choose a letter (X or Y): '))
            if p == 'X':
                t = 'Y'
                print 'Player 2, you are ' + t
                return p, t
            elif p == 'Y':
                t = 'X'
                print 'Player 2, you are ' + t
                return p, t
    print 'Player 2, you are ' + t
    return p, t

def playerOneMove(bList, letter): #Player 1 chooses a move
    num = int(raw_input('Player 1, make a move (0-8): ' ))
    while num < 0 or num > 8 or (bList[num] == letter):
        num = int(raw_input('Try again: '))
    return num

def win(bList, letter): #function to determine if player won
    if (bList[0] == bList[1] == bList[2] == letter) or (bList[3] == bList[4] == bList[5] == letter) or (bList[6] == bList[7] == bList[8] == letter) or (bList[0] == bList[3] == bList[6] == letter) or (bList[1] == bList[4] == bList[7] == letter) or (bList[2] == bList[5] == bList[8] == letter) or (bList[0] == bList[4] == bList[8] == letter) or (bList[2] == bList[4] == bList[6] == letter):
        return True

def tie(bList): #function to check if there is a tie in the game 
    i = 0
    for i in range(len(bList)):
        j = str(i)
        if(bList[i] != j):
            i = i + 1
        else:
            return False
    print 'It\'s a tie!'
    return True

def playerTwoMove(bList, letter): #Player 2 chooses a move
    numTwo = int(raw_input('Player 2, make a move (0-8): '))
    while numTwo < 0 or numTwo > 8 or (bList[numTwo] == letter):
        numTwo = int(raw_input('Try again: '))
    return numTwo

def makePlayerOneMove(bList, move, letter): #function that takes input from player 1 and assigns it to the respective index on the board
    bList[move] = letter

def playGame(): #function that executes the game
    bList = ['0','1','2','3','4','5','6','7','8']
    letterOne, letterTwo = inputLetters()
    while True:
        board(bList)
        move = playerOneMove(bList,letterTwo)
        makePlayerOneMove(bList,move,letterOne)
        if ((win(bList,letterOne)) or (win(bList,letterTwo))):
            board(bList)
            bList = ['0','1','2','3','4','5','6','7','8']
            print 'You won!'
            return False
        elif(tie(bList)):
            board(bList)
            bList = ['0','1','2','3','4','5','6','7','8']
            return False
        board(bList)
        moveTwo = playerTwoMove(bList,letterOne)
        makePlayerTwoMove(bList,moveTwo,letterTwo)
        if ((win(bList,letterOne)) or (win(bList,letterTwo))):
            board(bList)
            bList = ['0','1','2','3','4','5','6','7','8'] #resets the board
            print 'You won!'
            return False
        elif(tie(bList)):
            board(bList)
            bList = ['0','1','2','3','4','5','6','7','8']
            return False

playGame() 
