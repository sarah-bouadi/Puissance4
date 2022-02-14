# Class Game, define the environement of the game and it rules
from lib.pawn import *
from lib.grid import *

class Game:
    grid = [[Pawn(0, 0, 2), Pawn(1, 0, 1)],[Pawn(0, 1, 1), Pawn(1, 1, 1)]]


    # Constructor of the class
    def __init__(self, grid, player1, player2=None, difficulty=0):
        self.grid = grid
        self.player1 = player1
        self.player2 = player2
        self.difficulty = difficulty

    @property
    def grid(self):
        """
        :return: the game's grid
        """
        return self.__grid

    @grid.setter
    def grid(self, size):
        """
        Set a grid
        :param size: the size of the grid
        """
        self.__grid = grid(size)

    def getPawn(self, grid, column, row):
        """
        :param grid: the game's grid
        :param column: the column to check
        :param row: the row to check
        :return: the pawn at the position (column, grid) or raise an error if no pawn
        """
        try:
            if isinstance(grid[row][column], Pawn):
                print(grid[row][column])
            else:
                print("il n y a pas de pion à cette position")
        except:
            print("saisir une position valide sur la grille")


    def getLeftNeighbour(self, grid, pawn):
        """
        return the left neighbour
        :param pawn: the pawn to test
        :return: left neighbour
        """
        try:
            isinstance(pawn, Pawn)
        except ValueError:
            print("Mettre un pion valide")
            raise
        else:
            left_column = pawn.column - 1
            if isinstance(grid[pawn.row][left_column], Pawn):
                self.getPawn(grid, left_column, pawn.row)
            else:
                print("Il n y a pas de voisin à gauche")


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
    
