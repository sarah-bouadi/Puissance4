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
    grid_txt = ""
    self.grid_to_save = self.initMatrix()

    print("\n")
    for i in range(len(self.grid)):
        for j in range(len(self.grid[i])):
            if X:
                grid_txt += 'X'
                self.grid_to_save[i][j] ='X'
            elif O:
                grid_txt += 'O'
                self.grid_to_save[i][j] ='0'
            elif NONE:
                grid_txt += '.'
                self.grid_to_save[i][j] ='.'
        grid_txt += '\n'
    grid_txt += '\n'  

    print("\n")
    return grid_txt

def __str__(self):
    return self.display()
