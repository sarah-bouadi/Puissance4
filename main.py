from lib.pawn import *
from lib.game import *
from lib.player import *
from lib.grid import *

if __name__ == "__main__":
    pion = Pawn(2, 4, 1)
    pion_left = Pawn(1, 0, 2)

    test_grid = [
                 ['X', 'X', pion, 'O'],
                 ['.', '.', '.', '.'],
                 ['X', 'X', '.', 'O'],
                 ['X', 'O', 'O', 'X'],
                 ['X', pion_left, pion, 'O']]
    # grille = grid(4)
    massi = Player(1, "Massi", 1)
    jeu = Game(test_grid, massi)
    print(pion)
    print(pion_left)
    #print(test_grid[pion_left.row][pion_left.column])


    jeu.getLeftNeighbour(test_grid, pion)
