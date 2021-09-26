#Battleship
#Author: Isaac Porter


#imports
import time
import random

#method that gives a simple greeting and takes user input to decide what game mode they want to play
def intro(gameType):
    while(gameType != '1' and gameType != '2' and gameType != '3'):
        print('Welcome to Battleship!\n')
        gameType = input('Who will be the players? (enter 1 or 2)\n1) Player v. Player\n2) Player v. Computer\n>> ')
        if(gameType != '1' and gameType != '2' and gameType != '3'):
            for x in range(0, 20): print()
            print('That is not a valid option, please enter 1 or 2.')
    return gameType

#method that runs the player versus player game
def pvpGame():
    p1p = 2
    p1c = 3
    p1s = 3
    p1d = 4
    p1a = 5
    p2p = 2
    p2c = 3
    p2s = 3
    p2d = 4
    p2a = 5
    p1sb = setupBoard()
    p1gb = setupBoard()
    p2sb = setupBoard()
    p2gb = setupBoard()
    turn = 0
    printSetupBoard(p1sb)
    shipSetup(p1sb, '1')
    for x in range(1, 20): print()
    printSetupBoard(p2sb)
    shipSetup(p2sb, '2')
    for x in range(1, 20): print()
    while((p1p > 0 or p1c > 0 or p1s > 0 or p1d > 0 or p1a > 0) and (p2p > 0 or p2c > 0 or p2s > 0 or p2d > 0 or p2a > 0)):
        if(turn % 2 + 1 == 1):
            for x in range(0, 20): print()
            printGameBoard(p1gb)
            print("Player 1's turn")
            spot = guess(p2sb, p1gb)
            if(spot == 'p'):
                p2p -= 1
            elif(spot == 'c'):
                p2c -= 1
            elif(spot == 's'):
                p2s -= 1
            elif(spot == 'd'):
                p2d -= 1
            elif(spot == 'a'):
                p2a -= 1
            print("Sinks:")
            if(p2p == 0):
                print("Patrol Boat")
            if(p2c == 0):
                print("Cruiser")
            if(p2s == 0):
                print("Submarine")
            if(p2d == 0):
                print("Destroyer")
            if(p2a == 0):
                print("Aircraft")
            printGameBoard(p1gb)
        else:
            for x in range(0, 20): print()
            printGameBoard(p2gb)
            print("Player 2's turn")
            spot = guess(p1sb, p2gb)
            if(spot == 'p'):
                p1p -= 1
            elif(spot == 'c'):
                p1c -= 1
            elif(spot == 's'):
                p1s -= 1
            elif(spot == 'd'):
                p1d -= 1
            elif(spot == 'a'):
                p1a -= 1
            print("Sinks:")
            if(p1p == 0):
                print("Patrol Boat")
            if(p1c == 0):
                print("Cruiser")
            if(p1s == 0):
                print("Submarine")
            if(p1d == 0):
                print("Destroyer")
            if(p1a == 0):
                print("Aircraft Carrier")
            printGameBoard(p2gb)
        turn += 1
        time.sleep(3)
    if(p1p > 0 or p1c > 0 or p1s > 0 or p1d > 0 or p1a > 0):
        for x in range(0, 20): print()
        printGameBoard(p1gb)
        print("\nPlayer 1 wins!")
    else:
        for x in range(0, 20): print()
        printGameBoard(p2gb)
        print("\nPlayer 2 wins!")

#method handling ship placement phase for players
def shipSetup(board, a):
    count = 1
    print("Player " + a + "'s turn to place ships (ships cannot overlap).")
    shipList()
    while(count < 6):
        st = str(count)
        e = 1
        while(e > 0):
            x = input("What row would you like the ship to start in? (choose 1 - 10)\n>> ")
            y = input("What column would you like the ship to start in? (choose 1 - 10)\n>> ")
            d = input("Which direction should the ship point? (choose 1 - 4):\n1 - up\t\t2 - right\n3 - down\t4 - left\n>> ")
            if((x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '10') and (y == '1' or y == '2' or y == '3' or y == '4' or y == '5' or y == '6' or y == '7' or y == '8' or y == '9' or y == '10') and (d == '1' or d == '2' or d == '3' or d == '4')):
                e = shipLegality(board, st, x, y, d)
            if(e > 0):
                printSetupBoard(board)
                print("\nThat is not valid input, please try again.")
            else:
                print("Ship has been placed.")
        placeShip(board, st, x, y, d)
        printSetupBoard(board)
        count += 1

#method handling user input to decide which level of cpu the user wants to play against
def pvcGameOptions(computerLevel):
    while(computerLevel != '1' and computerLevel != '2' and computerLevel != '3'):
        computerLevel = input('Computer difficulty (enter 1, 2, or 3):\n1) easy\n2) medium\n3) hard\n>> ')
        if(computerLevel != '1' and computerLevel != '2' and computerLevel != '3'):
            print('\nThat is not a valid option.')
    return computerLevel

#method that runs a game between a player and an easy level cpu
def easyMode():
    p1p = 2
    p1c = 3
    p1s = 3
    p1d = 4
    p1a = 5
    p2p = 2
    p2c = 3
    p2s = 3
    p2d = 4
    p2a = 5
    p1sb = setupBoard()
    p1gb = setupBoard()
    p2sb = setupBoard()
    turn = 0
    printSetupBoard(p1sb)
    shipSetup(p1sb, '1')
    compSetup(p2sb)
    for x in range(1, 20):print()
    while((p1p > 0 or p1c > 0 or p1s > 0 or p1d > 0 or p1a > 0) and (p2p > 0 or p2c > 0 or p2s > 0 or p2d > 0 or p2a > 0)):
        if(turn % 2 + 1 == 1):
            for x in range(0, 20): print()
            printGameBoard(p1gb)
            print("Player 1's turn")
            spot = guess(p2sb, p1gb)
            if(spot == 'p'):
                p2p -= 1
            elif(spot == 'c'):
                p2c -= 1
            elif(spot == 's'):
                p2s -= 1
            elif(spot == 'd'):
                p2d -= 1
            elif(spot == 'a'):
                p2a -= 1
            print("Sinks:")
            if(p2p == 0):
                print("Patrol Boat")
            if(p2c == 0):
                print("Cruiser")
            if(p2s == 0):
                print("Submarine")
            if(p2d == 0):
                print("Destroyer")
            if(p2a == 0):
                print("Aircraft Carrier")
            printGameBoard(p1gb)
        else:
            print("\nComputer's turn...")
            time.sleep(2)
            for x in range(0, 20): print()
            if((turn + 1) % 30 == 0 and turn != 1):
                spot = autoHit(p1sb)
            else:
                spot = cpuGuess(p1sb, p1sb)
            if(spot == 'p'):
                p1p -= 1
            elif(spot == 'c'):
                p1c -= 1
            elif(spot == 's'):
                p1s -= 1
            elif(spot == 'd'):
                p1d -= 1
            elif(spot == 'a'):
                p1a -= 1
            print("Sinks:")
            if(p1p == 0):
                print("Patrol Boat")
            if(p1c == 0):
                print("Cruiser")
            if(p1s == 0):
                print("Submarine")
            if(p1d == 0):
                print("Destroyer")
            if(p1a == 0):
                print("Aircraft Carrier")
            printSetupBoardAlt(p1sb)
        turn += 1
        time.sleep(3)
    if(p1p > 0 or p1c > 0 or p1s > 0 or p1d > 0 or p1a > 0):
        for x in range(0, 20): print()
        printGameBoard(p1gb)
        print("\nPlayer 1 wins!")
    else:
        for x in range(0, 20): print()
        printSetupBoardAlt(p1sb)
        print("\nThe computer wins!")

#method that runs a game between a player and a medium level cpu
def mediumMode():
    p1p = 2
    p1c = 3
    p1s = 3
    p1d = 4
    p1a = 5
    p2p = 2
    p2c = 3
    p2s = 3
    p2d = 4
    p2a = 5
    p1sb = setupBoard()
    p1gb = setupBoard()
    p2sb = setupBoard()
    turn = 0
    printSetupBoard(p1sb)
    shipSetup(p1sb, '1')
    compSetup(p2sb)
    for x in range(1, 20): print()
    while((p1p > 0 or p1c > 0 or p1s > 0 or p1d > 0 or p1a > 0) and (p2p > 0 or p2c > 0 or p2s > 0 or p2d > 0 or p2a > 0)):
        if(turn % 2 + 1 == 1):
            for x in range(0, 20): print()
            printGameBoard(p1gb)
            print("Player 1's turn")
            spot = guess(p2sb, p1gb)
            if(spot == 'p'):
                p2p -= 1
            elif(spot == 'c'):
                p2c -= 1
            elif(spot == 's'):
                p2s -= 1
            elif(spot == 'd'):
                p2d -= 1
            elif(spot == 'a'):
                p2a -= 1
            print("Sinks:")
            if(p2p == 0):
                print("Patrol Boat")
            if(p2c == 0):
                print("Cruiser")
            if(p2s == 0):
                print("Submarine")
            if(p2d == 0):
                print("Destroyer")
            if(p2a == 0):
                print("Aircraft Carrier")
            printGameBoard(p1gb)
        else:
            print("\nComputer's turn...")
            time.sleep(2)
            for x in range(0, 20): print()
            if((turn + 1) % 20 == 0 and turn != 1):
                spot = autoHit(p1sb)
            else:
                spot = cpuGuess(p1sb, p1sb)
            if(spot == 'p'):
                p1p -= 1
            elif(spot == 'c'):
                p1c -= 1
            elif(spot == 's'):
                p1s -= 1
            elif(spot == 'd'):
                p1d -= 1
            elif(spot == 'a'):
                p1a -= 1
            print("Sinks:")
            if(p1p == 0):
                print("Patrol Boat")
            if(p1c == 0):
                print("Cruiser")
            if(p1s == 0):
                print("Submarine")
            if(p1d == 0):
                print("Destroyer")
            if(p1a == 0):
                print("Aircraft Carrier")
            printSetupBoardAlt(p1sb)
        turn += 1
        time.sleep(3)
    if(p1p > 0 or p1c > 0 or p1s > 0 or p1d > 0 or p1a > 0):
        for x in range(0, 20): print()
        printGameBoard(p1gb)
        print("\nPlayer 1 wins!")
    else:
        for x in range(0, 20): print()
        printSetupBoardAlt(p1sb)
        print("\nThe computer wins!")

#method that runs a game between a player and a hard level cpu
def hardMode():
    p1p = 2
    p1c = 3
    p1s = 3
    p1d = 4
    p1a = 5
    p2p = 2
    p2c = 3
    p2s = 3
    p2d = 4
    p2a = 5
    p1sb = setupBoard()
    p1gb = setupBoard()
    p2sb = setupBoard()
    turn = 0
    printSetupBoard(p1sb)
    shipSetup(p1sb, '1')
    compSetup(p2sb)
    for x in range(1, 20): print()
    while((p1p > 0 or p1c > 0 or p1s > 0 or p1d > 0 or p1a > 0) and (p2p > 0 or p2c > 0 or p2s > 0 or p2d > 0 or p2a > 0)):
        if(turn % 2 + 1 == 1):
            for x in range(0, 20): print()
            printGameBoard(p1gb)
            print("Player 1's turn")
            spot = guess(p2sb, p1gb)
            if(spot == 'p'):
                p2p -= 1
            elif(spot == 'c'):
                p2c -= 1
            elif(spot == 's'):
                p2s -= 1
            elif(spot == 'd'):
                p2d -= 1
            elif(spot == 'a'):
                p2a -= 1
            print("Sinks:")
            if(p2p == 0):
                print("Patrol Boat")
            if(p2c == 0):
                print("Cruiser")
            if(p2s == 0):
                print("Submarine")
            if(p2d == 0):
                print("Destroyer")
            if(p2a == 0):
                print("Aircraft Carrier")
            printGameBoard(p1gb)
        else:
            print("\nComputer's turn...")
            time.sleep(2)
            for x in range(0, 20): print()
            if((turn + 1) % 10 == 0 and turn != 1):
                spot = autoHit(p1sb)
            else:
                spot = cpuGuess(p1sb, p1sb)
            if(spot == 'p'):
                p1p -= 1
            elif(spot == 'c'):
                p1c -= 1
            elif(spot == 's'):
                p1s -= 1
            elif(spot == 'd'):
                p1d -= 1
            elif(spot == 'a'):
                p1a -= 1
            print("Sinks:")
            if(p1p == 0):
                print("Patrol Boat")
            if(p1c == 0):
                print("Cruiser")
            if(p1s == 0):
                print("Submarine")
            if(p1d == 0):
                print("Destroyer")
            if(p1a == 0):
                print("Aircraft Carrier")
            printSetupBoardAlt(p1sb)
        turn += 1
        time.sleep(3)
    if(p1p > 0 or p1c > 0 or p1s > 0 or p1d > 0 or p1a > 0):
        for x in range(0, 20): print()
        printGameBoard(p1gb)
        print("\nPlayer 1 wins!")
    else:
        for x in range(0, 20): print()
        printSetupBoardAlt(p1sb)
        print("\nThe computer wins!")

#method that runs a demo game between 2 cpu opponents
def demoGame():
    p1p = 2
    p1c = 3
    p1s = 3
    p1d = 4
    p1a = 5
    p2p = 2
    p2c = 3
    p2s = 3
    p2d = 4
    p2a = 5
    p1sb = setupBoard()
    p2sb = setupBoard()
    turn = 0
    compSetup(p1sb)
    printSetupBoard(p1sb)
    compSetup(p2sb)
    printSetupBoard(p2sb)
    while((p1p > 0 or p1c > 0 or p1s > 0 or p1d > 0 or p1a > 0) and (p2p > 0 or p2c > 0 or p2s > 0 or p2d > 0 or p2a > 0)):
        if(turn % 2 + 1 == 1):
            for x in range(0, 20): print()
            print("Computer's turn...")
            time.sleep(5)
            if((turn + 1) % 10 == 0 and turn != 1):
                spot = autoHit(p2sb)
            else:
                spot = cpuGuess(p2sb, p2sb)
            if(spot == 'p'):
                p2p -= 1
            elif(spot == 'c'):
                p2c -= 1
            elif(spot == 's'):
                p2s -= 1
            elif(spot == 'd'):
                p2d -= 1
            elif(spot == 'a'):
                p2a -= 1
            print("Sinks:")
            if(p2p == 0):
                print("Patrol Boat")
            if(p2c == 0):
                print("Cruiser")
            if(p2s == 0):
                print("Submarine")
            if(p2d == 0):
                print("Destroyer")
            if(p2a == 0):
                print("Aircraft Carrier")
            printGameBoard(p2sb)
        else:
            for x in range(0, 20): print()
            print("\nComputer's turn...")
            time.sleep(5)
            for x in range(0, 20): print()
            if((turn + 1) % 10 == 0 and turn != 1):
                spot = autoHit(p1sb)
            else:
                spot = cpuGuess(p1sb, p1sb)
            if(spot == 'p'):
                p1p -= 1
            elif(spot == 'c'):
                p1c -= 1
            elif(spot == 's'):
                p1s -= 1
            elif(spot == 'd'):
                p1d -= 1
            elif(spot == 'a'):
                p1a -= 1
            print("Sinks:")
            if(p1p == 0):
                print("Patrol Boat")
            if(p1c == 0):
                print("Cruiser")
            if(p1s == 0):
                print("Submarine")
            if(p1d == 0):
                print("Destroyer")
            if(p1a == 0):
                print("Aircraft Carrier")
            printSetupBoardAlt(p1sb)
        turn += 1
        time.sleep(5)
    if(p1p > 0 or p1c > 0 or p1s > 0 or p1d > 0 or p1a > 0):
        for x in range(0, 20): print()
        printGameBoard(p1gb)
        print("\nComputer wins!")
    else:
        for x in range(0, 20): print()
        printSetupBoardAlt(p1sb)
        print("\nComputer wins!")

#autohit function used in the incrementing of cpu difficulty
def autoHit(board):
    for x in range(1, 10):
        for y in range(1, 10):
            if(board[x][y] != '-' and board[x][y] != 'h' and board[x][y] != 'm'):
                hitSpot = board[x][y]
                board[x][y] = 'h'
                print("That's a hit!")
                return hitSpot

#method starting computer placement phase
def compSetup(board):
    count = 1
    print("\nComputer's turn to place ships.")
    while(count < 6):
        st = str(count)
        e = 1
        while(e > 0):
            x = str(random.randint(1, 10))
            y = str(random.randint(1, 10))
            d = str(random.randint(1, 4))
            e = shipLegality(board, st, x, y, d)
        placeShip(board, st, x, y, d)
        count += 1
    time.sleep(2)
    print("Computer has finished placing ships.")
    time.sleep(2)

#sets up the base board for battleship before players place ships
def setupBoard():
    board = [['-' for i in range(0, 11)] for i in range(0, 11)]
    for x in range(0, 11):
        board[0][x] = str(x)
    for x in range(1, 10):
        board[x][0] = str(x) + ' '
    board[10][0] = 10
    board[0][0] += ' '
    return board

#prints the setup board that ships are placed on
def printSetupBoard(board):
    print('\n      Battleship')
    for x in range(0, 11):
        for y in range(0, 11):
            print(board[x][y], end=' ')
        print()
    print("Legend:\n'p' - patrol boat\t'c' - cruiser\n's' - submarine\t\t'd' - destroyer\n'a' - aircraft carrier\n'-' - open space\n")

#prints the alternate setup board which is a combo of the game board and setup board
def printSetupBoardAlt(board):
    print('\n      Battleship')
    for x in range(0, 11):
        for y in range(0, 11):
            print(board[x][y], end=' ')
        print()
    print("Legend:\n'p' - patrol boat\t'c' - cruiser\t's' - submarine\n'd' - destroyer\t\t'a' - aircraft carrier\n'-' - open space\t'h' - hit\t'm' - miss\n")

#prints the game board (board players see and guess on after setup)
def printGameBoard(board):
    print('\n      Battleship')
    for x in range(0, 11):
        for y in range(0, 11):
            print(board[x][y], end=' ')
        print()
    print("Legend:\n'-' - open space\n'h' - hit\t'm' - miss\n")

#method taking a guess from the user at which spot they think an opponent ship is
def guess(b1, b2):
    i = 1
    while(i == 1):
        x = input("In which row would you like guess? (choose 1 - 10)\n>> ")
        y = input("In which column would you like to guess? (choose 1 - 10)\n>> ")
        if((x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '10') and (y == '1' or y == '2' or y == '3' or y == '4' or y == '5' or y == '6' or y == '7' or y == '8' or y == '9' or y == '10')):
            if(b2[int(x)][int(y)] != 'm' and b2[int(x)][int(y)] != 'h'):
                return check(b1, b2, x, y)
            else:
                print('You have already guessed that spot.')
        else:
            print('That is an invalid placement.')

#random guess method for cpu opponent
def cpuGuess(b1, b2):
    i = 1
    while(i == 1):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        if(b1[x][y] != 'h' and b1[x][y] != 'm'):
            return check(b1, b2, x, y)

#checks if location guessed is a hit or miss
def check(b1, b2, x, y):
    a, b = int(x), int(y)
    if(b1[a][b] == '-'):
        for x in range(0, 20): print()
        print('A swing and a miss!')
        z = b1[a][b]
        b2[a][b] = 'm'
    else:
        for x in range(0, 20): print()
        print("That's a hit!")
        z = b1[a][b]
        b2[a][b] = 'h'
    return z

#simple list of ships in the game
def shipList():
    print('Here are your ships to place:')
    print(f'1) Patrol boat: {"pp":<15}')
    print(f'2) Cruiser: {"ccc":<15}')
    print(f'3) Submarine: {"sss":<15}')
    print(f'4) Destroyer: {"dddd":<15}')
    print(f'5) Aircraft Carrier: {"aaaaa":<15}')
    print("(you will place the ships in the order they appear)")
    print()

#checks the legality of the placement of a ship before it is place on the board
def shipLegality(board, shipType, a, b, c):
    x, y, d = a, b, c
    i = 1
    if(d == '1'):
        if(shipType == '1'):
            if(int(x) - 1 >= 1):
                c = 2
                for r in range(0, 2):
                    if(board[int(x) - r][int(y)] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '2'):
            if(int(x) - 2 >= 1):
                c = 3
                for r in range(0, 3):
                    if(board[int(x) - r][int(y)] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '3'):
            if(int(x) - 2 >= 1):
                c = 3
                for r in range(0, 3):
                    if(board[int(x) - r][int(y)] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '4'):
            if(int(x) - 3 >= 1):
                c = 4
                for r in range(0, 4):
                    if(board[int(x) - r][int(y)] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '5'):
            if(int(x) - 4 >= 1):
                c = 5
                for r in range(0, 5):
                    if(board[int(x) - r][int(y)] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
    elif(d == '2'):
        if(shipType == '1'):
            if(int(y) + 1 <= 10):
                c = 2
                for r in range(0, 2):
                    if(board[int(x)][int(y) + r] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '2'):
            if(int(y) + 2 <= 10):
                c = 3
                for r in range(0, 3):
                    if(board[int(x)][int(y) + r] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '3'):
            if(int(y) + 2 <= 10):
                c = 3
                for r in range(0, 3):
                    if(board[int(x)][int(y) + r] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '4'):
            if(int(y) + 3 <= 10):
                c = 4
                for r in range(0, 4):
                    if(board[int(x)][int(y) + r] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '5'):
            if(int(y) + 4 <= 10):
                c = 5
                for r in range(0, 5):
                    if(board[int(x)][int(y) + r] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
    elif(d == '3'):
        if(shipType == '1'):
            if(int(x) + 1 <= 10):
                c = 2
                for r in range(0, 2):
                    if(board[int(x) + r][int(y)] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '2'):
            if(int(x) + 2 <= 10):
                c = 3
                for r in range(0, 3):
                    if(board[int(x) + r][int(y)] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '3'):
            if(int(x) + 2 <= 10):
                c = 3
                for r in range(0, 3):
                    if(board[int(x) + r][int(y)] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '4'):
            if(int(x) + 3 <= 10):
                c = 4
                for r in range(0, 4):
                    if(board[int(x) + r][int(y)] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '5'):
            if(int(x) + 4 <= 10):
                c = 5
                for r in range(0, 5):
                    if(board[int(x) + r][int(y)] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
    elif(d == '4'):
        if(shipType == '1'):
            if(int(y) - 1 >= 1):
                c = 2
                for r in range(0, 2):
                    if(board[int(x)][int(y) - r] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '2'):
            if(int(y) - 2 >= 1):
                c = 3
                for r in range(0, 3):
                    if(board[int(x)][int(y) - r] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '3'):
            if(int(y) - 2 >= 1):
                c = 3
                for r in range(0, 3):
                    if(board[int(x)][int(y) - r] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '4'):
            if(int(y) - 3 >= 1):
                c = 4
                for r in range(0, 4):
                    if(board[int(x)][int(y) - r] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
        elif(shipType == '5'):
            if(int(y) - 4 >= 1):
                c = 5
                for r in range(0, 5):
                    if(board[int(x)][int(y) - r] == '-'):
                        c -= 1
                if(c == 0):
                    i -= 1
    return i

#method that places ships of a certain ship type on a board starting at location board[a][b] and going in a certain direction
def placeShip(board, st, a, b, direction):
    x, y = int(a), int(b)
    if(st == '1'):
        if(direction == '1'):
            for i in range(0, 2):
                board[x - i][y] = 'p'
        elif(direction == '2'):
            for i in range(0, 2):
                board[x][y + i] = 'p'
        elif(direction == '3'):
            for i in range(0, 2):
                board[x + i][y] = 'p'
        else:
            for i in range(0, 2):
                board[x][y - i] = 'p'
    elif(st == '2'):
        if(direction == '1'):
            for i in range(0, 3):
                board[x - i][y] = 'c'
        elif(direction == '2'):
            for i in range(0, 3):
                board[x][y + i] = 'c'
        elif(direction == '3'):
            for i in range(0, 3):
                board[x + i][y] = 'c'
        else:
            for i in range(0, 3):
                board[x][y - i] = 'c'
    elif(st == '3'):
        if(direction == '1'):
            for i in range(0, 3):
                board[x - i][y] = 's'
        elif(direction == '2'):
            for i in range(0, 3):
                board[x][y + i] = 's'
        elif(direction == '3'):
            for i in range(0, 3):
                board[x + i][y] = 's'
        else:
            for i in range(0, 3):
                board[x][y - i] = 's'
    elif(st == '4'):
        if(direction == '1'):
            for i in range(0, 4):
                board[x - i][y] = 'd'
        elif(direction == '2'):
            for i in range(0, 4):
                board[x][y + i] = 'd'
        elif(direction == '3'):
            for i in range(0, 4):
                board[x + i][y] = 'd'
        else:
            for i in range(0, 4):
                board[x][y - i] = 'd'
    else:
        if(direction == '1'):
            for i in range(0, 5):
                board[x - i][y] = 'a'
        elif(direction == '2'):
            for i in range(0, 5):
                board[x][y + i] = 'a'
        elif(direction == '3'):
            for i in range(0, 5):
                board[x + i][y] = 'a'
        else:
            for i in range(0, 5):
                board[x][y - i] = 'a'

#starts the domino of methods and launches Battleship
gt = 0
gt = intro(gt)
if(gt == '1'):
    pvpGame()
elif(gt == '3'):
    demoGame()
else:
    level = 0
    level = pvcGameOptions(level)
    if(level == '1'):
        easyMode()
    elif(level == '2'):
        mediumMode()
    else:
        hardMode()