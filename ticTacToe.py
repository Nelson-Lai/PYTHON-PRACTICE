'''Tic Tac Toe'''
import random
'''create a gameboard '''
class TicTacToe:
    def __init__(self):
        self.newGameboard()
        self.victory = 0
        print("Let's play a game of TicTacToe")
        self.gameLoop()



    boardLocations = {'topLeft':[0,1],'topMid':[0,5],'topRight':[0,9],'midLeft':[2,1],'center':[2,5],'midRight':[2,9],'botLeft':[4,1],'botMid':[4,5],'botRight':[4,9]}
    backLocations = {'topLeft':[0,0],'topMid':[0,1],'topRight':[0,2],'midLeft':[1,0],'center':[1,1],'midRight':[1,2],'botLeft':[2,0],'botMid':[2,1],'botRight':[2,2]}


    def newGameboard(self):
        self.gameBoard = [
        '   |   |   ',
        '___|___|___',
        '   |   |   ',
        '___|___|___',
        '   |   |   ',
        '   |   |   '
        ]
        self.availableSet = set(['topLeft','topMid','topRight','midLeft','center','midRight','botLeft','botMid','botRight'])
        self.backBoard = [[0,0,0],[0,0,0],[0,0,0]]

    def placeMarker(self,location: str, mark: str):
        x,y = self.boardLocations[location]
        xback, yback = self.backLocations[location]
        if mark == 'x':
            self.backBoard[xback][yback] = 1
        elif mark == 'o':
            self.backBoard[xback][yback] = -1
        boardRow = list(self.gameBoard[x])
        boardRow[y] = mark
        self.gameBoard[x] = ''.join(boardRow)
        self.availableSet.remove(location)

    def displayBoard(self):
        for row in self.gameBoard:
            print(row)

    def checkVictory(self) -> int:
        for row in self.backBoard:
            if sum(row) == 3:
                return 1
            elif sum(row) == -3:
                return -1

        for column in range(3):
            columnsum = 0
            for row in self.backBoard:
                columnsum += row[column]
            if columnsum == 3:
                return 1
            elif columnsum == -3:
                return -1

        diagonalsum1 = 0
        diagonalsum2 = 0
        for diagonal in range(3):
            diagonalsum1 += self.backBoard[diagonal][diagonal]
            diagonalsum2 += self.backBoard[diagonal][2-diagonal]

        if diagonalsum1 == 3 or diagonalsum2 == 3:
            return 1
        elif diagonalsum1 == -3 or diagonalsum2 == -3:
            return -1
        return 0


    def computerMove(self):
        move = random.choice(list(self.availableSet))
        self.placeMarker(move,'o')

    def gameLoop(self):
        while self.victory == 0:
            if self.availableSet:
                self.displayBoard()
                self.victory = self.checkVictory()
                if self.victory == 1:
                    print('Player Victory')
                    break
                elif self.victory == -1:
                    print('CPU Victory')
                    break

                print('Available Moves:')
                print(self.availableSet)
                move = input('>>')
                if move not in self.availableSet:
                    continue
                self.placeMarker(move,'x')
                self.displayBoard()

                self.victory = self.checkVictory()
                if self.victory == 1:
                    print('Player Victory')
                    break
                elif self.victory == -1:
                    print('CPU Victory')
                    break

                if self.availableSet:
                    input('Press Enter to see Computer Move')
                    self.computerMove()
            else:
                self.displayBoard()
                print('Draw Game!')
                break

newGame = 'Y'
while True:
    if newGame == 'Y':
        game = TicTacToe()
        newGame = input('New Game? [Y/N]:')
    else:
        break

pass