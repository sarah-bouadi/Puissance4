
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
    #print(row)
    grid.add_pawn_grid(pion_rouge, 0)
    grid.add_pawn_grid(pion_jaune, 0)
    grid.add_pawn_grid(pion_jaune, 0)
    grid.add_pawn_grid(pion_jaune, 2)
    grid.add_pawn_grid(pion_rouge, 1)
    grid.display()

    player_naruto = Player(1, "Naruto")
    print(player_naruto)