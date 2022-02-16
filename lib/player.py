

from asyncio.windows_events import NULL


class Player():

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getId(self):
        return self.id

    def getName(self):
        return self.name  

        #Returns a tuple like: ((player1_id, player1_name), (player2_id, player2_name))
    def initialize_P_vs_P(self):
        player1_name = input("- Enter the name of player 1: ")
        player1_id = input("- Enter the id of player 1: ")

        player2_name = input("- Enter the name of player 2: ")
        player2_id = input("- Enter the id of player 2: ")
        return ((player1_id, player1_name), (player2_id, player2_name))

    #Returns a tuple like: ((player1_id, player1_name), (player2_id, player2_name))
    def initialize_P_vs_computer(self):
        player1_name = input("- Enter the name of player 1: ")
        player1_id = input("- Enter the id of player 1: ")

        return ((player1_id, player1_name), (None, None))    

    def get_grid_row_from_column(self, grid, column):
        row = grid.get_size()
        while grid.matrix[row][column] != 0:
            row -= 1
        if row == 0:
            print("The column is full!")
            return None
        return row

    def add_pawn_grid(self, pion, grid, column):
        row = self.get_grid_row_from_column(grid, column)
        if row is not None:
            pion.row, pion.column = row, column
            grid.matrix[row][column] = pion
        else:
            print("Column is full, please choose another column")
             

