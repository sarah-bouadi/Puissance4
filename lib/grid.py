
from ast import Str
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
                if self.getMatrix()[i][j] == None or self.getMatrix()[i][j] == 'None':
                    return False
        return True 
 
    def _initialize_grid(self, grid_size):
        return [[None]*grid_size for i in range(grid_size)]

    def get_grid_row_from_column(self, column):
        for i in range(self.grid_size-1, -1,-1):
            if self.matrix[i][column] == 'None' or self.matrix[i][column] == None:
                return i
        return None

    def display(self):
        grid_txt = ""
        self.grid_to_save = [[None]*self.grid_size for i in range(self.grid_size)]
        import re
        reaesc = re.compile(r'\x1b[^m]*m')
        
        print("\n")
        for i in range(self.getSize()):
            for j in range(self.getSize()):
                if isinstance(self.matrix[i][j], Pawn):
                    current_pawn = reaesc.sub('', str(self.matrix[i][j]))
                    grid_txt += str(self.matrix[i][j])
                    self.grid_to_save[i][j] = str(current_pawn)
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
                    new_pawn = Pawn(1)
                    new_pawn.row = i
                    new_pawn.column = j
                    grid_object[i][j] = new_pawn
                elif grid_txt[i][j] == ' O ' :
                    new_pawn = Pawn(2)
                    new_pawn.row = i
                    new_pawn.column = j
                    grid_object[i][j] = new_pawn
                else:
                    grid_object[i][j] = 'None'
        self.setMatrix(grid_object)

    def __str__(self):
        return self.display()


    