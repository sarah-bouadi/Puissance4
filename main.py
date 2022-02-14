from lib.pawn import *
from lib.game import *
from lib.player import *
from lib.grid import *

if __name__ == "__main__":
    pion = Pawn(2, 4, 1)
    pion_left = Pawn(1, 0, 2)

    test_grid_2 = Grid(4)
    test_grid_2.setMatrix()
    # grille = grid(4)
    Massi = Player(1, "Massi", 1)
    jeu = Game(test_grid_2, Massi)
    print(pion)
    print(pion_left)

    print(test_grid_2.getMatrix())

    #print(test_grid[pion_left.row][pion_left.column])
    jeu.getRightNeighbour(test_grid_2, pion_left)
