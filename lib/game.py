# Class Game, define the environement of the game and it rules
from lib.pawn import *
from lib.grid import *
from lib.player import *
from termcolor import *

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
    def grid(self, grid):
        """
        Set a grid
        :param size: the size of the grid
        """
        self.__grid = grid

    def getPawn(self, row, column):
        """
        the pawn's getter
        
        :param column: the column to check
        :param row: the row to check
        :return: the pawn at the position (column, grid) else None
        """
        grid = self.grid 
        try:
            if 0 <= column < grid.getSize() and 0 <= row < grid.getSize():
                if isinstance(grid.matrix[row][column], Pawn):
                    return grid.matrix[row][column]
                return None
            return None
        except:
            return None

    def getLeftNeighbour(self, pawn):
        """
        return the left neighbour
        :param pawn: the pawn to test
        :return: left neighbour
        """
        try:
            if isinstance(pawn, Pawn):
                left_column = pawn.column - 1
                return self.getPawn(pawn.row, left_column)
        except ValueError:
            raise AttributeError("Insert a valid pawn")

    def getRightNeighbour(self, pawn):
        """
        return the right side neighbour
        :param pawn: the pawn to test
        :return: right side neighbour
        """
        try:
            if isinstance(pawn, Pawn):
                right_column = pawn.column + 1
                return self.getPawn(pawn.row, right_column)
        except ValueError:
            raise AttributeError("Insert a valid pawn")

    def getUpNeighbour(self, pawn):
        """
        return the up side neighbour
        :param pawn: the pawn to test
        :return: up neighbour
        """
        try:
            if isinstance(pawn, Pawn):
                up_row = pawn.row - 1
                return self.getPawn(up_row, pawn.column)
        except ValueError:
            raise AttributeError("Insert a valid pawn")

    def getDownNeighbour(self, pawn):
        """
        return the down side neighbour
        :param pawn: the pawn to test
        :return: down neighbour
        """
        try:
            if isinstance(pawn, Pawn):
                down_row = pawn.row + 1
                return self.getPawn(down_row, pawn.column)
        except ValueError:
            raise AttributeError("Insert a valid pawn")

    def getDiagonalLeftDownNeighbour(self, pawn):
        """
        return the left down diagonal neighbour
        :param pawn: the pawn to check
        :return: left diagonal neighbour
        """
        if isinstance(pawn, Pawn):
            x = pawn.row + 1
            y = pawn.column - 1
            return self.getPawn(x, y)

    def getDiagonalLeftUpNeighbour(self, pawn):
        """
        return the left Up diagonal neighbour
        :param pawn: the pawn to check
        :return: left diagonal neighbour
        """
        if isinstance(pawn, Pawn):
            x = pawn.row - 1
            y = pawn.column - 1
            return self.getPawn(x, y)

    def getDiagonalRightDownNeighbour(self, pawn):
        """
        return the Right down diagonal neighbour
        :param pawn: the pawn to check
        :return: Right diagonal neighbour
        """
        if isinstance(pawn, Pawn):
            x = pawn.row + 1
            y = pawn.column + 1
            return self.getPawn(x, y)

    def getDiagonalRightUpNeighbour(self, pawn):
        """
        return the Right Up diagonal neighbour
        :param pawn: the pawn to check
        :return: Right diagonal neighbour
        """
        if isinstance(pawn, Pawn):
            x = pawn.row - 1
            y = pawn.column + 1
            return self.getPawn(x, y)

    def count_up_neighbour(self, pawn):
        """
        count the number of same pawn neighbour up
        :param pawn: the pawn to check
        :return: cpt the number of neighbours
        """
        tmp = pawn
        cpt = 0
        while isinstance(tmp, Pawn):
            if isinstance(self.getUpNeighbour(tmp), Pawn):
                if tmp.color == self.getUpNeighbour(tmp).color:
                    cpt += 1
            tmp = self.getUpNeighbour(tmp)
        return cpt

    def count_down_neighbour(self, pawn):
        """
        count the number of same pawn neighbour down
        :param pawn: the pawn to check
        :return: cpt the number of neighbours
        """
        tmp = pawn
        cpt = 0
        while isinstance(tmp, Pawn):
            if isinstance(self.getDownNeighbour(tmp), Pawn):
                if tmp.color == self.getDownNeighbour(tmp).color:
                    cpt += 1
            tmp = self.getDownNeighbour(tmp)
        return cpt

    def count_left_neighbour(self, pawn):
        """
        count the number of same pawn neighbour at left
        :param pawn: the pawn to check
        :return: cpt the number of neighbours
        """
        tmp = pawn
        cpt = 0
        while isinstance(tmp, Pawn):
            if isinstance(self.getLeftNeighbour(tmp), Pawn):
                if tmp.color == self.getLeftNeighbour(tmp).color:
                    cpt += 1
            tmp = self.getLeftNeighbour(tmp)
        return cpt

    def count_right_neighbour(self, pawn):
        """
        count the number of same pawn neighbour at right
        :param pawn: the pawn to check
        :return: cpt the number of neighbours
        """
        tmp = pawn
        cpt = 0
        while isinstance(tmp, Pawn):
            if isinstance(self.getRightNeighbour(tmp), Pawn):
                if tmp.color == self.getRightNeighbour(tmp).color:
                    cpt += 1
            tmp = self.getRightNeighbour(tmp)
        return cpt

    def count_diagonal_left_neighbour(self, pawn):
        """
        count the number of neighbours with same color as pawn
        :param pawn: the pawn to check
        :return: the number of diagonal left neighbours with the same color
        """
        tmp = pawn
        cpt = 0
        if isinstance(tmp, Pawn):
            diagonal_left_up_neighbour = self.getDiagonalLeftUpNeighbour(tmp)
            while isinstance(diagonal_left_up_neighbour, Pawn):
                tmp = diagonal_left_up_neighbour
                diagonal_left_up_neighbour = self.getDiagonalLeftUpNeighbour(tmp)
                if tmp.color == pawn.color:
                    cpt += 1
                    # tmp = self.getDiagonalLeftUpNeighbour(grid, tmp)
            tmp = pawn
            diagonal_Right_down_neighbour = self.getDiagonalRightDownNeighbour(tmp)
            while isinstance(diagonal_Right_down_neighbour, Pawn):
                tmp = diagonal_Right_down_neighbour
                diagonal_Right_down_neighbour = self.getDiagonalRightDownNeighbour(tmp)
                if tmp.color == pawn.color:
                    cpt += 1
        return cpt

    def count_diagonal_right_neighbour(self, pawn):
        """
        count the number of neighbours with same color as pawn
        :param pawn: the pawn to check
        :return: the number of diagonal left neighbours with the same color
        """
        tmp = pawn
        cpt = 0
        if isinstance(tmp, Pawn):
            diagonal_right_up_neighbour = self.getDiagonalRightUpNeighbour(tmp)
            while isinstance(diagonal_right_up_neighbour, Pawn):
                tmp = diagonal_right_up_neighbour
                diagonal_right_up_neighbour = self.getDiagonalRightUpNeighbour(tmp)
                if tmp.color == pawn.color:
                    cpt += 1

            tmp = pawn
            diagonal_left_down_neighbour = self.getDiagonalLeftDownNeighbour(tmp)
            while isinstance(diagonal_left_down_neighbour, Pawn):
                tmp = diagonal_left_down_neighbour
                diagonal_left_down_neighbour = self.getDiagonalLeftDownNeighbour(tmp)
                if tmp.color == pawn.color:
                    cpt += 1
        return cpt

    def checkVerticalWinner(self, pawn):
        """
                return 1 if there's a vertical winner, else 0
                :param grid: the grid of the game
                :param pawn: the played pawn
                :return: True or False
                """
        if self.count_up_neighbour(pawn) + self.count_down_neighbour(pawn) + 1 >= 4:
            return True
        return False

    def checkHorizontalWinner(self, pawn):
        """
        return 1 if there's an horizental winner, else 0
        :param pawn: the played pawn
        :return: true or false
        """
        grid = self.grid
        if self.count_left_neighbour(pawn) + self.count_right_neighbour(pawn) + 1 >= 4:
            return True
        return False


    def checkLeftDiagonalWinner(self, pawn):
        """
                return True if there's a diagonal left winner, else False
                :param player: the player who played the pawn
                :param pawn: the played pawn
                :return: True or False
                """
        return self.count_diagonal_left_neighbour(pawn) + 1 >= 4

    def checkRightDiagonalWinner(self, pawn):
        """
                return True if there's a diagonal right winner, else False
                :param player: the player who played the pawn
                :param pawn: the played pawn
                :return: int 1 or 0
                """
        return self.count_diagonal_right_neighbour(pawn) + 1 >= 4

    def getPlayerFromColor(self, color):
        """
        Return the associated player to the color in param
        :param color: the param to check
        :return: the associated player to the color in param
        """
        player1 = self.player1
        player2 = self.player2
        return player1 if player1.choosen_color == color else player2

    def checkWinner(self, pawn):
        """
        returns the winner of the game
        :param pawn: the last pawn added
        :return: True if player won else false
        """
        if self.checkHorizontalWinner(pawn) \
                or self.checkVerticalWinner(pawn) \
                or self.checkLeftDiagonalWinner(pawn) \
                or self.checkRightDiagonalWinner(pawn):

            color = pawn.color
            player = self.getPlayerFromColor(color)
            print(self.grid, end='\n\n')
            print(colored(f"*** {player}", "green"), colored("wins the game ! ***\n\n", "green"))
            return True
        else:
            return False