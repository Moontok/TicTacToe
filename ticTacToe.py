
def main():
    print('LETS PLAY TIC-TAC-TOE!\nEnter a command as: X1 or O3')
    gameOver = False
    b = Board()
    print(b)
    while not gameOver:
        playerInput = input('Input: ')
        if b.inputCheck(playerInput):
            b.setXO(playerInput)
        print(b)
        gameOver = b.checkWinState() or b.checkDraw()
    print('Thanks for playing!')

class Board:
    def __init__(self):
        self.board: str = self.createBoard()
        self.locs: list = self.getLocs()

    def __str__(self):
        return f'\n#####\n{self.board}\n#####\n'

    def createBoard(self):
        return '1|2|3\n-----\n4|5|6\n-----\n7|8|9'

    def getLocs(self):
        locs: list = []
        for i, char in enumerate(self.board):
            if char.isdigit():
                locs.append(i)
        return locs

    def setXO(self, playerInput):
        self.board = self.board.replace(playerInput[1], playerInput[0].upper())

    def inputCheck(self, playerInput):
        if len(playerInput) > 2 or playerInput[0].lower() not in 'xo' or not playerInput[1].isdigit():
            print('Invalid Input Entered.')
            return False
        elif playerInput[1] not in self.board:
            print('Spot already used.')
            return False        
        return True

    def checkWinState(self):
        winStates = [
                        [0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8],
                        [0, 3, 6],
                        [1, 4, 7],
                        [2, 5, 8],
                        [0, 4, 8],
                        [2, 4, 6]
                    ]

        for state in winStates:
            if self.board[self.locs[state[0]]] == self.board[self.locs[state[1]]] == self.board[self.locs[state[2]]]:
                print(f'\n***{self.board[self.locs[state[0]]]} WINS!***\n')
                return True
        return False
    
    def checkDraw(self):
        for char in self.board:
            if char.isdigit():
                return False
        print('\n***DRAW! NO WINNERS!***\n')
        return True

if __name__ == '__main__':
    main()
