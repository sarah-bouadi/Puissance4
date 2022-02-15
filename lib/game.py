# Class Game, define the environement of the game and it rules
from lib.pawn import *
from lib.grid import *

class Game:
    #grid = [[Pawn(0, 0, 2), Pawn(1, 0, 1)],[Pawn(0, 1, 1), Pawn(1, 1, 1)]]


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
        self.__grid = Grid(size).matrix

    def getPawn(self, grid, column, row):
        """
        the pawn's getter
        :param grid: the game's grid
        :param column: the column to check
        :param row: the row to check
        :return: the pawn at the position (column, grid) or raise an error if no pawn
        """
        try:
            if isinstance(grid.matrix[row][column], Pawn):
                return grid.matrix[row][column]
            else:
                print("il n y a pas de pion à cette position")
                return 0
        except:
            print("saisir une position valide sur la grille")


    def getLeftNeighbour(self, grid, pawn):
        """
        return the left neighbour
        :param grid: the game's grid
        :param pawn: the pawn to test
        :return: left neighbour
        """
        try:
            isinstance(pawn, Pawn)
            left_column = pawn.column - 1
            if left_column >= 0 and isinstance(self.getPawn(grid, left_column, pawn.row), Pawn):
                self.getPawn(grid, left_column, pawn.row)
            else:
                print("Il n y a pas de voisin à gauche")
        except ValueError:
            raise AttributeError("Mettre un pion valide")



    def getRightNeighbour(self, grid, pawn):
        """
        return the right side neighbour
        :param grid: the game's grid
        :param pawn: the pawn to test
        :return: right side neighbour
        """
        try:
            isinstance(pawn, Pawn)
            right_column = pawn.column + 1
            if right_column <= grid.getSize() and isinstance(self.getPawn(grid, right_column, pawn.row), Pawn):
                self.getPawn(grid, right_column, pawn.row)
            else:
                print("Il n y a pas de voisin à droite")
        except ValueError:
            raise AttributeError("Mettre un pion valide")


    def getUpNeighbour(self, grid, pawn):
        """
        return the up side neighbour
        :param pawn: the pawn to test
        :return: up neighbour
        """
        try:
            isinstance(pawn, Pawn)
            up_row = pawn.row + 1
            if up_row <= grid.getSize() and isinstance(self.getPawn(grid, pawn.column, up_row), Pawn):
                self.getPawn(grid, pawn.column, up_row)
            else:
                print("Il n y a pas de voisin en haut")
        except ValueError:
            raise AttributeError("Mettre un pion valide")

    def getDownNeighbour(self, pawn):
        """
        return the down side neighbour
        :param pawn: the pawn to test
        :return: down neighbour
        """
        try:
            isinstance(pawn, Pawn)
            down_row = pawn.row - 1
            if down_row >= 0 and isinstance(self.getPawn(grid, pawn.column, down_row), Pawn):
                self.getPawn(grid, pawn.column, down_row)
            else:
                print("Il n y a pas de voisin en bas")
        except ValueError:
            raise AttributeError("Mettre un pion valide")



    def checkHorizentalWinner(self, player):
        pass

    def checkVerticalWinner(self, player):
        pass
    
    def checkLeftDiagonalWinner(self, player):
        pass
    
    def checkRightDiagonalWinner(self, player):
        pass
    
    def checkWinner(self):
        return checkHorizentalWinner(self, player) or