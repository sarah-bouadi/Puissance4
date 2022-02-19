EMPTY_GRID = 0
RED_PAWN = -1
RED_WIN = -4
YELLOW_PAWN = 1
YELLOW_WIN = 4

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

    def initMatrix(self):
        self.matrix = self._initialize_grid(self.__check_grid_size())

    def __check_grid_size(self):
        if self.grid_size>=4:
            return self.grid_size
        else:
            raise AttributeError("Please enter grid_size >=4 !")

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

    def add_pawn_grid(self, pawn, column):
        row = self.get_grid_row_from_column(column)
        if row is not None:
            pawn.row = row
            print("row:", pawn.row)
            pawn.column = column
            self.matrix[row][column] = pawn
        else:
            print("Column is full, please choose another column")

    def display(self):
        print("\n")
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                print(self.matrix[i][j], end=' ')
            print()
        print("\n")
