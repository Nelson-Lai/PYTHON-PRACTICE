class Board:
    letters = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
    lettersList = ['A','B','C','D','E','F','G','H','I','J']
    numbersSet = set([1,2,3,4,5,6,7,8,9,0])

    def __init__(self):
        self.homeBoard = [['~' for x in range(10)] for y in range(10)]
        self.enemyBoard = [['~' for x in range(10)] for y in range(10)]

    def printBoard(self):
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
    def __init__(self):
        self.player1 = Board()
        self.player2 = Board()

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
            return [letter, number]

    def placeShip(self, distance):
        while True:
            self.player1.printBoard()
            print('Starting Coordinate:')
            startCoord = self.takeInput()
            print('Ending Coordinate: ')
            endCoord = self.takeInput()
            points = []
            if startCoord[0] != endCoord[0] and startCoord[1] != endCoord[1]:
                print('Invalid Placement: Try again')
                input('OK')
                continue
            else:
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

                if givenDist != distance - 1:
                    print('Invalid Placement, wrong distance, try again')
                    input('OK')
                    continue
            for index in points:
                self.player1.placeMark(index[0],index[1],'#','home')
            self.player1.printBoard()
            break





game = Game()
# player1 = Board()
# player1.printBoard()
# player1.placeMark('A','4','X','home')
# player1.printBoard()
game.placeShip(4)