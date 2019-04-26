'''Tic Tac Toe'''

'''create a gameboard '''
class TicTacToe:
    boardLocations = {'topLeft':[0,1],'topMid':[0,5],'topRight':[0,9],'midLeft':[2,1],'midMid':[2,5],'midRight':[2,9],'botLeft':[4,1],'botMid':[4,5],'botRight':[4,9]}
    def newGameboard(self):
        self.gameBoard = [
        '   |   |   ',
        '___|___|___',
        '   |   |   ',
        '___|___|___',
        '   |   |   ',
        '   |   |   '
        ]
        availableSet = set(['topLeft','topMid','topRight','midLeft','midMid','midRight','botLeft','botMid','botRight'])

    def placeMarker(self,location: str, mark: str):
        x,y = boardLocations[location]
        boardRow = list(self.gameBoard[x])
        boardRow[y] = mark
        self.gameBoard[x] = ''.join(boardRow)

    def displayBoard(self):
        for row in self.gameBoard:
            print(row)

game = TicTacToe()
game.newGameboard()
game.placeMarker('topMid','x')
game.displayBoard()