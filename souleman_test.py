
    #Initialize the grid with grid_size     
from lib.pawn import *
from lib.game import *
from lib.player import *

if __name__ == "__main__":

    pion_rouge = Pawn(1)
    pion_jaune = Pawn(2)

    grid = Grid(4)
    grid.initMatrix()
    grid.display()

    row = grid.get_grid_row_from_column(2)

    player_naruto = Player(1, "Naruto")
    print(player_naruto)

    #print(row)
    player_naruto.add_pawn_grid(grid, 1, 0)
    player_naruto.add_pawn_grid(grid, 2, 0)
    player_naruto.add_pawn_grid(grid, 2, 0)
    player_naruto.add_pawn_grid(grid, 2, 0)
    player_naruto.add_pawn_grid(grid, 2, 0)
    player_naruto.add_pawn_grid(grid, 2, 2)
    player_naruto.add_pawn_grid(grid, 1, 1)
    grid.display()


    #Develop testadd
