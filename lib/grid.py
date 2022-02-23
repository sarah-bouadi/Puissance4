from re import X
from lib.pawn import *

class Grid:
    def __init__(self, grid_size):
        """
        Constructor of the grid
        :param grid_size: int the size of the grid
        :param matrix: the matrix of the grid
        """
        self.grid_size = grid_size
        self.matrix = []
        #= self._initialize_grid(self.__check_grid_size())


    def getSize(self):
        return self.grid_size

    def setSize(self, size):
        self.grid_size = size

    def getMatrix(self):
        return self.matrix

    def setMatrix(self,matrix):
        self.matrix = matrix

    def initMatrix(self):
        self.matrix = self._initialize_grid(self.__check_grid_size())

    def __check_grid_size(self):
        if self.grid_size>=4:
            return self.grid_size
        else:
            raise AttributeError("Please enter grid_size >=4 !")

    def isFull(self):
        for i in range(self.getSize()):
            for j in range(self.getSize()):
                if self.matrix[i][j] == None:
                    return False
        return True 

    def _initialize_grid(self, grid_size):
        return [[None]*grid_size for i in range(grid_size)]

    def get_grid_row_from_column(self, column):
        row = self.grid_size-1
        while row >= 0 and self.matrix[row][column] != None :
            row -= 1
        if row == -1:
            print("The column is full!")
            return None
        return row

    def display(self):
        grid_txt = ""
        self.grid_to_save = [[None]*self.grid_size for i in range(self.grid_size)]

        print("\n")
        for i in range(self.getSize()):
            for j in range(self.getSize()):
                if isinstance(self.matrix[i][j], Pawn):
                    grid_txt += str(self.matrix[i][j])
                    self.grid_to_save[i][j] = str(self.matrix[i][j])
                else:
                    grid_txt += ' . '
                    self.grid_to_save[i][j] = ' . '
            grid_txt += '\n'
        grid_txt += '\n'
        return grid_txt

    def convert_gridtxt_gridobject(self,grid_txt):

        grid_object = self._initialize_grid(self.getSize())

        for i in range(self.getSize()):
            for j in range(self.getSize()):
                if grid_txt[i][j] == ' X ' :
                    grid_object[i][j] = Pawn(1)
                elif grid_txt[i][j] == ' O ' :
                    grid_object[i][j] = Pawn(2)
                else:
                    grid_object[i][j] = 'None'
        self.setMatrix(grid_object)

    def __str__(self):
        return self.display()


    