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
        """
        size getter
        :return: the grid's size
        """
        return self.grid_size

    def setSize(self, size):
        """
        size setter
        :param size: the size to attribute
        """
        self.grid_size = size

    def getMatrix(self):
        """
        matrix getter
        :return: the matrix
        """
        return self.matrix

    def setMatrix(self,matrix):
        """
        matrix setter
        :param matrix: the matrix to attribute
        """
        self.matrix = matrix

    def initMatrix(self):
        """
        return matrix 
        """
        self.matrix = self._initialize_grid(self.__check_grid_size())


    def __check_grid_size(self):
        """
        check the grid's size
        """
        if self.grid_size>=4:
            return self.grid_size
        else:
            raise AttributeError("Please enter grid_size >=4 !")

    def isFull(self):
        """
        check if the matrix is full 
        return True if it's full
        return False if it's not full
        """
        for i in range(self.getSize()):
            for j in range(self.getSize()):
                if self.getMatrix()[i][j] == None or self.getMatrix()[i][j] == 'None':
                    return False
        return True 
 
    def _initialize_grid(self, grid_size):
        """
        initialize grid 
        :param grid_size: the grid's size 
        """
        return [[None]*grid_size for i in range(grid_size)]

    def get_grid_row_from_column(self, column):
        """
        getting the grid's row from column
        :param column: the grid's column
        """
        for i in range(self.grid_size-1, -1,-1):
            if self.matrix[i][column] == 'None' or self.matrix[i][column] == None:
                return i
        return None

    def display(self):
        """
        display grid
        :return grid_txt: the grid in format txt
        """
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
        """
        convert the grid in format txt to object grid
        :param grid_txt: the grid in format txt
        """
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
        """
        display grid
        """
        return self.display()


    