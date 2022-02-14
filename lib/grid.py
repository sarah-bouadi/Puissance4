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

    # def getSize(self):
    #     return self.grid_size

    def setSize(self, size):
        self.grid_size = size

    def getMatrix(self):
        return self.matrix

    def setMatrix(self):
        self.matrix = self._initialize_grid(self.__check_grid_size())

    def __check_grid_size(self):
        if self.grid_size>=4:
            return self.grid_size
        else:
            raise AttributeError("Please enter grid_size >=4 !")

    def _initialize_grid(self, grid_size):
        return [[0]*grid_size for i in range(grid_size)]


    def display(self):
            print("\n")
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    print(self.grid[i][j], end=' ')
                print()
            print("\n")
