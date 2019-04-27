import random
class Board:
    letters = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
    lettersList = ['A','B','C','D','E','F','G','H','I','J']
    numbersSet = set([1,2,3,4,5,6,7,8,9,0])

    def __init__(self, name):
        self.name = name
        self.homeBoard = [['~' for x in range(10)] for y in range(10)]
        self.enemyBoard = [['~' for x in range(10)] for y in range(10)]

    def printBoard(self):
        print(self.name)
        print('                    HOME BOARD                                                  ENEMY BOARD')
        for index in range(10):
            print(self.lettersList[index], self.homeBoard[index], '      ', self.lettersList[index], self.enemyBoard[index])
        print('    0    1    2    3    4    5    6    7    8    9              0    1    2    3    4    5    6    7    8    9   ')

    def placeMark(self, letter, number, mark, player):
        if player == 'home':
            board = self.homeBoard
        elif player == 'enemy':
            board = self.enemyBoard
        else:
            print('Incorrect Player Specified')
            raise(ValueError)
        board[self.letters[letter]][int(number)] = mark


class Game:
    letters = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
    lettersList = ['A','B','C','D','E','F','G','H','I','J']
    numbersSet = set(['1','2','3','4','5','6','7','8','9','0'])
    playerMoves = set()
    cpuMoves = set()

    def __init__(self, dev = False):
        self.player1 = Board('Player 1')
        self.player2 = Board('Player 2')
        self.devMode = dev
        self.gameInitialization()

    def takeInput(self):
        while True:
            inputStr = input('Select a gridpoint: ')
            if len(inputStr) != 2:
                print('Please enter a valid point')
                continue
            letter, number = list(inputStr.upper())
            if letter not in self.letters:
                print('Please enter a valid letter')
                continue
            elif number not in self.numbersSet:
                print('Please enter a valid number')
                continue
            return [letter, str(number)]

    def manualPlacement(self, player):
        self.placeShip(4, player)
        self.placeShip(3, player)
        self.placeShip(2, player)

    def randomPlacement(self, player):
        self.randomPlacementHelper(4, player)
        self.randomPlacementHelper(3, player)
        self.randomPlacementHelper(2, player)

    def randomPlacementHelper(self, dist, player):
        while True:
            row = random.choice(self.lettersList)
            column = random.choice(list(self.numbersSet))
            startCoord = [row, column]
            if self.isColliding([startCoord], player) == False:
                potentialEnd = self.distFromPoint(startCoord, dist - 1)
                endCoord = random.choice(potentialEnd)
                shipPoints = self.pointsBetween(startCoord, endCoord)
                if self.isColliding(shipPoints, player) == False:
                    self.placeShip(dist, player,startCoord,endCoord)
                    break
            else:
                continue


    def distFromPoint(self, point, dist):
        row = self.letters[point[0]]
        column = int(point[1])
        output = []
        if row - dist >= 0:
            output.append([self.lettersList[row - dist],point[1]])
        if row + dist <= 9:
            output.append([self.lettersList[row + dist],point[1]])
        if column + dist <= 9:
            output.append([point[0], str(column + dist)])
        if column - dist >= 0:
            output.append([point[0], str(column - dist)])
        return output

    def pointsBetween(self, startCoord, endCoord):
        points = []
        if startCoord[0] == endCoord[0]:
            givenDist = abs(int(startCoord[1]) - int(endCoord[1]))
            lowerStart = min( [int(startCoord[1]),int(endCoord[1])] )
            for idx in range(givenDist+1):
                points.append([startCoord[0], str(lowerStart + idx)])

        elif startCoord[1] == endCoord[1]:
            givenDist = abs(self.letters[startCoord[0]] - self.letters[endCoord[0]])
            letter1Idx = self.lettersList.index(startCoord[0])
            letter2Idx = self.lettersList.index(endCoord[0])
            minLetterIdx = min([letter1Idx, letter2Idx])
            for idx in range(givenDist+1):
                points.append( [self.lettersList[minLetterIdx + idx] , str(startCoord[1])] )

        return points

    def isColliding(self, points, player):
        if player == 1:
            playerBoard = self.player1
        elif player == 2:
            playerBoard = self.player2
        checkCollision = False
        for index in points:
            if playerBoard.homeBoard[self.letters[index[0]]][int(index[1])] != '~':
                checkCollision = True
        return checkCollision


    def placeShip(self, distance, player, start = None, end = None):
        while True:
            if player == 1:
                playerBoard = self.player1
            elif player == 2:
                playerBoard = self.player2
            if start == None or end == None:
                playerBoard.printBoard()
                print('Placing a ship of distance ' + str(distance))
                print('Starting Coordinate:')
                startCoord = self.takeInput()
                print('Ending Coordinate: ')
                endCoord = self.takeInput()
            else:
                startCoord = start
                endCoord = end
            points = []
            if startCoord[0] != endCoord[0] and startCoord[1] != endCoord[1]:
                print('Invalid Placement: Try again')
                input('OK')
                continue
            else:
                points = self.pointsBetween(startCoord,endCoord)

                if len(points) != distance:
                    print('Invalid Placement, wrong distance, try again')
                    input('OK')
                    continue

            collision = self.isColliding(points, player)

            if collision == True:
                print('Placement Collision Detected, try again')
                input('OK')
                continue

            for index in points:
                playerBoard.placeMark(index[0],index[1],'@','home')
            break

    def playerMove(self):
        while True:
            self.player1.printBoard()
            print('Where should we attack?')
            move = self.takeInput()
            row, column = move
            if str(move) not in self.playerMoves:
                self.playerMoves.add(str(move))
            else:
                print("We've attacked there before!")
                continue
            if self.player2.homeBoard[self.letters[row]][int(column)] == '@':
                mark = 'X'
                print('HIT!')
            else:
                mark = 'O'
                print('MISS...')

            self.player1.placeMark(row, column, mark,'enemy')
            self.player2.placeMark(row, column, mark, 'home')
            break

    def cpuMove(self):
        while True:
            row = random.choice(self.lettersList)
            column = random.choice(list(self.numbersSet))
            move = [row, column]
            if str(move) not in self.cpuMoves:
                self.cpuMoves.add(str(move))
            else:
                continue
            print('Computer Tries: ' + row + column)
            if self.player1.homeBoard[self.letters[row]][int(column)] == '@':
                mark = 'X'
                print('HIT!')
            else:
                mark = 'O'
                print('MISS...')

            self.player2.placeMark(row, column, mark,'enemy')
            self.player1.placeMark(row, column, mark, 'home')
            break

    def isVictorious(self, player):
        if player == 1:
            playerCheck = self.player2
        elif player == 2:
            playerCheck = self.player1
        for row in playerCheck.homeBoard:
            for element in row:
                if element == '@':
                    return False
        return True

    def gameInitialization(self):
        print('Hello Player, we need to place ships on your side before proceeding.')
        playerRandom = input('Type "RANDOM" to random your ship positions, otherwise press enter to place them manually \n')
        if playerRandom == 'RANDOM':
            self.randomPlacement(1)
        else:
            self.manualPlacement(1)
        self.player1.printBoard()
        input('Randomizing CPU Battleship Locations, press Enter to Continue')
        self.randomPlacement(2)
        if self.devMode == True:
            print('DEVELOPER MODE ON: ENEMY BOARD SHOWN')
            self.player2.printBoard()
        self.gameLoop()

    def endGame(self, player):
        if player == 1:
            print('PLAYER 1 HAS WON!')
        elif player == 2:
            print('CPU HAS WON!')
        print('                PLAYER 1 BOARD                                                    CPU BOARD')
        for index in range(10):
            print(self.player1.homeBoard[index],'          ',self.player2.homeBoard[index])


    def gameLoop(self):
        while True:
            self.playerMove()
            if self.isVictorious(1):
                self.endGame(1)
                break
            input("Computer's Turn")
            self.cpuMove()
            if self.isVictorious(2):
                self.endGame(2)
                break



while True:
    game = Game()
    again = input('Play Again? [Y/N]')
    if again == 'Y' or again == 'y':
        continue
    else:
        break

