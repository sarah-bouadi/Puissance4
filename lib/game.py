# Class Game, define the environement of the game and it rules
class Game():
    
    # Constructor of the class
    def __init__(self, grid, player1, player2=None, difficulty=0):
        self.grid = grid
        self.player1 = player1
        self.player2 = player2
        self.difficulty = difficulty

    # Return the color of the left pawn neighbour
    def getColorLeftNeighbour(self, pawn):
        pass

    # Return the color of the right pawn neighbour
    def getColorRightNeighbour(self, pawn):
        pass

    def checkHorizentalWinner(self,player):
        pass

    def checkVerticalWinner(self,player):
        pass
    
    def checkLeftDiagonalWinner(self,player):
        pass
    
    def checkRightDiagonalWinner(self,player):
        pass
    
