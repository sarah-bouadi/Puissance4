# Class Game, define the environement of the game and it rules
from lib.pawn import *

class Game:
    grid = [[Pawn(0, 0, 2), Pawn(1, 0, 1)],[Pawn(0, 1, 1), Pawn(1, 1, 1)]]


    # Constructor of the class
    def __init__(self, grid, player1, player2=None, difficulty=0):
        self.grid = grid
        self.player1 = player1
        self.player2 = player2
        self.difficulty = difficulty


    def getPawn(self, grid, column, row):
        try:
            if isinstance(grid(column, row)):
                print(grid(column, row))
        except Exception:
            raise "Il n'existe pas de pion à cette position"


    def getLeftNeighbour(self, pion):
        """
        return the left neighbour
        :param pawn: the pawn to test
        :return: left neighbour
        """
        try:
            left_column = pion.column-1
            if left_column >= 0:
                self.getPawn(pion.column, pion.row)
            else:
                print("Il n y a pas de voisin gauche")
        except ValueError:
            print(ValueError)


    def getRightNeighbour(self, pawn):
        """
        return the right side neighbour
        :param pawn: the pawn to test
        :return: right side neighbour
        """


    def getUpNeighbour(self, pawn):
        """
        return the up side neighbour
        :param pawn: the pawn to test
        :return: up neighbour
        """
        pass

    def getDownNeighbour(self, pawn):
        """
        return the down side neighbour
        :param pawn: the pawn to test
        :return: down neighbour
        """
        pass

    def checkHorizentalWinner(self,player):
        pass

    def checkVerticalWinner(self,player):
        pass
    
    def checkLeftDiagonalWinner(self,player):
        pass
    
    def checkRightDiagonalWinner(self,player):
        pass
    
