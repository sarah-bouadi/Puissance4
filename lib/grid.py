EMPTY_GRID = 0
RED_PAWN = -1
RED_WIN = -4
YELLOW_PAWN = 1
YELLOW_WIN = 4

class grid:
    def __init__(self, grid_size):
        self.grid = self._initialize_grid(self.__check_grid_size(grid_size))
        
    def __check_grid_size(self, grid_size):
        if(grid_size>=4):
            return grid_size
        else:
            raise AttributeError("Please enter grid_size >=4 !")

    def _initialize_grid(self, grid_size):
        return [ [0]*grid_size for i in range(grid_size)]


    def display(self):
            print("\n")
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    print(self.grid[i][j], end=' ')
                print()
            print("\n")
