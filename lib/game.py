# Class Game, define the environement of the game and it rules
from lib.pawn import *
from lib.grid import *
from lib.player import *


class Game:

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

    def getPawn(self, grid, row, column):
        """
        the pawn's getter
        :param grid: the game's grid
        :param column: the column to check
        :param row: the row to check
        :return: the pawn at the position (column, grid) else None
        """
        try:
            if 0 <= column <= grid.getSize() and 0 <= row <= grid.getSize():
                if isinstance(grid.matrix[row][column], Pawn):
                    return grid.matrix[row][column]
                return None
            return None
        except:
            return None

    def getLeftNeighbour(self, grid, pawn):
        """
        return the left neighbour
        :param grid: the game's grid
        :param pawn: the pawn to test
        :return: left neighbour
        """
        try:
            if isinstance(pawn, Pawn):
                left_column = pawn.column - 1
                return self.getPawn(grid, pawn.row, left_column)
        except ValueError:
            raise AttributeError("Insert a valid pawn")

    def getRightNeighbour(self, grid, pawn):
        """
        return the right side neighbour
        :param grid: the game's grid
        :param pawn: the pawn to test
        :return: right side neighbour
        """
        try:
            if isinstance(pawn, Pawn):
                right_column = pawn.column + 1
                return self.getPawn(grid, pawn.row, right_column)
        except ValueError:
            raise AttributeError("Insert a valid pawn")

    def getUpNeighbour(self, grid, pawn):
        """
        return the up side neighbour
        :param pawn: the pawn to test
        :return: up neighbour
        """
        try:
            if isinstance(pawn, Pawn):
                up_row = pawn.row - 1
                return self.getPawn(grid, up_row, pawn.column)
        except ValueError:
            raise AttributeError("Insert a valid pawn")

    def getDownNeighbour(self, grid, pawn):
        """
        return the down side neighbour
        :param pawn: the pawn to test
        :return: down neighbour
        """
        try:
            if isinstance(pawn, Pawn):
                down_row = pawn.row + 1
                return self.getPawn(grid, down_row, pawn.column)
        except ValueError:
            raise AttributeError("Insert a valid pawn")

    def getDiagonalLeftDownNeighbour(self, grid, pawn):
        """
        return the left down diagonal neighbour
        :param grid: the grid to check 
        :param pawn: the pawn to check
        :return: left diagonal neighbour
        """
        if isinstance(pawn, Pawn):
            x = pawn.row + 1
            y = pawn.column - 1
            return self.getPawn(grid, x, y)

    def getDiagonalLeftUpNeighbour(self, grid, pawn):
        """
        return the left Up diagonal neighbour
        :param grid: the grid to check 
        :param pawn: the pawn to check
        :return: left diagonal neighbour
        """
        if isinstance(pawn, Pawn):
            x = pawn.row - 1
            y = pawn.column - 1
            return self.getPawn(grid, x, y)

    def getDiagonalRightDownNeighbour(self, grid, pawn):
        """
        return the Right down diagonal neighbour
        :param grid: the grid to check 
        :param pawn: the pawn to check
        :return: Right diagonal neighbour
        """
        if isinstance(pawn, Pawn):
            x = pawn.row + 1
            y = pawn.column + 1
            return self.getPawn(grid, x, y)

    def getDiagonalRightUpNeighbour(self, grid, pawn):
        """
        return the Right Up diagonal neighbour
        :param grid: the grid to check 
        :param pawn: the pawn to check
        :return: Right diagonal neighbour
        """
        if isinstance(pawn, Pawn):
            x = pawn.row - 1
            y = pawn.column + 1
            return self.getPawn(grid, x, y)

    def count_up_neighbour(self, grid, pawn):
        """
        count the number of same pawn neighbour up
        :param grid: the grid where to check
        :param pawn: the pawn to check
        :return: cpt the number of neighbours
        """
        tmp = pawn
        cpt = 0
        while isinstance(tmp, Pawn):
            if isinstance(self.getUpNeighbour(grid, tmp), Pawn):
                if tmp.color == self.getUpNeighbour(grid, tmp).color:
                    cpt += 1
            tmp = self.getUpNeighbour(grid, tmp)
        return cpt

    def count_down_neighbour(self, grid, pawn):
        """
        count the number of same pawn neighbour down
        :param grid: the grid where to check
        :param pawn: the pawn to check
        :return: cpt the number of neighbours
        """
        tmp = pawn
        cpt = 0
        while isinstance(tmp, Pawn):
            if isinstance(self.getDownNeighbour(grid, tmp), Pawn):
                if tmp.color == self.getDownNeighbour(grid, tmp).color:
                    cpt += 1
            tmp = self.getDownNeighbour(grid, tmp)
        return cpt

    def count_left_neighbour(self, grid, pawn):
        """
        count the number of same pawn neighbour at left
        :param grid: the grid where to check
        :param pawn: the pawn to check
        :return: cpt the number of neighbours
        """
        tmp = pawn
        cpt = 0
        while isinstance(tmp, Pawn):
            if isinstance(self.getLeftNeighbour(grid, tmp), Pawn):
                if tmp.color == self.getLeftNeighbour(grid, tmp).color:
                    cpt += 1
            tmp = self.getLeftNeighbour(grid, tmp)
        return cpt

    def count_right_neighbour(self, grid, pawn):
        """
        count the number of same pawn neighbour at right
        :param grid: the grid where to check
        :param pawn: the pawn to check
        :return: cpt the number of neighbours
        """
        tmp = pawn
        cpt = 0
        while isinstance(tmp, Pawn):
            if isinstance(self.getRightNeighbour(grid, tmp), Pawn):
                if tmp.color == self.getRightNeighbour(grid, tmp).color:
                    cpt += 1
            tmp = self.getRightNeighbour(grid, tmp)
        return cpt

    def count_diagonal_left_neighbour(self, grid, pawn):
        """
        count the number of neighbours with same color as pawn
        :param grid: the grid to check
        :param pawn: the pawn to check 
        :return: the number of diagonal left neighbours with the same color
        """
        tmp = pawn
        cpt = 0
        if isinstance(tmp, Pawn):
            diagonal_left_up_neighbour = self.getDiagonalLeftUpNeighbour(grid, tmp)
            while isinstance(diagonal_left_up_neighbour, Pawn):
                tmp = diagonal_left_up_neighbour
                diagonal_left_up_neighbour = self.getDiagonalLeftUpNeighbour(grid, tmp)
                if tmp.color == pawn.color:
                    cpt += 1
                    # tmp = self.getDiagonalLeftUpNeighbour(grid, tmp)
            tmp = pawn
            diagonal_Right_down_neighbour = self.getDiagonalRightDownNeighbour(grid, tmp)
            while isinstance(diagonal_Right_down_neighbour, Pawn):
                tmp = diagonal_Right_down_neighbour
                diagonal_Right_down_neighbour = self.getDiagonalRightDownNeighbour(grid, tmp)
                if tmp.color == pawn.color:
                    cpt += 1
        return cpt

    def count_diagonal_right_neighbour(self, grid, pawn):
        """
        count the number of neighbours with same color as pawn
        :param grid: the grid to check
        :param pawn: the pawn to check
        :return: the number of diagonal left neighbours with the same color
        """
        tmp = pawn
        cpt = 0
        if isinstance(tmp, Pawn):
            diagonal_right_up_neighbour = self.getDiagonalRightUpNeighbour(grid, tmp)
            while isinstance(diagonal_right_up_neighbour, Pawn):
                tmp = diagonal_right_up_neighbour
                diagonal_right_up_neighbour = self.getDiagonalRightUpNeighbour(grid, tmp)
                if tmp.color == pawn.color:
                    cpt += 1
                    
            tmp = pawn
            diagonal_left_down_neighbour = self.getDiagonalLeftDownNeighbour(grid, tmp)
            while isinstance(diagonal_left_down_neighbour, Pawn):
                tmp = diagonal_left_down_neighbour
                diagonal_left_down_neighbour = self.getDiagonalLeftDownNeighbour(grid, tmp)
                if tmp.color == pawn.color:
                    cpt += 1
        return cpt

    def checkVerticalWinner(self, grid, pawn):
        """
                return 1 if there's a vertical winner, else 0
                :param grid: the grid of the game
                :param pawn: the played pawn
                :return: True or False
                """
        if self.count_up_neighbour(grid, pawn) + self.count_down_neighbour(grid, pawn) + 1 >= 4:
            return True
        return False

    def checkHorizontalWinner(self, grid, pawn):
        """
        return 1 if there's an horizental winner, else 0
        :param pawn: the played pawn
        :return: true or false
        """
        if self.count_left_neighbour(grid, pawn) + self.count_right_neighbour(grid, pawn) + 1 >= 4:
            return True
        return False


    def checkLeftDiagonalWinner(self, grid, pawn):
        """
                return True if there's a diagonal left winner, else False
                :param player: the player who played the pawn
                :param pawn: the played pawn
                :return: True or False
                """
        return self.count_diagonal_left_neighbour(grid, pawn) + 1 >= 4

    def checkRightDiagonalWinner(self, grid, pawn):
        """
                return True if there's a diagonal right winner, else False
                :param player: the player who played the pawn
                :param pawn: the played pawn
                :return: int 1 or 0
                """
        return self.count_diagonal_right_neighbour(grid, pawn) + 1 >= 4

    def getPlayerFromColor(self, color, player1, player2):
        """
        Return the associated player to the color in param
        :param color: the param to check
        :param player1: player to check
        :param player2: player to check
        :return: the associated player to the color in param
        """
        return player1 if player1.choosen_color == color else player2

    def checkWinner(self, grid, pawn, player1, player2):
        """
        returns the winner of the game
        :param grid: the grid to check
        :param pawn: the last pawn added
        :param player1, player2: players of the game
        :return: True if player won else false
        """
        if self.checkHorizontalWinner(grid, pawn) \
                or self.checkVerticalWinner(grid, pawn) \
                or self.checkLeftDiagonalWinner(grid, pawn) \
                or self.checkRightDiagonalWinner(grid, pawn):

            color = pawn.color
            player = self.getPlayerFromColor(color, player1, player2)
            print(f"*** {player} you win the game ! ***")
            return True
        else:
            return False