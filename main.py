from lib.pawn import *
from lib.game import *
from lib.player import *

if __name__ == "__main__":

    test_grid = [['.', '.', '.', '.'],
                 ['X', 'X', '.', 'O'],
                 ['X', 'O', 'O', 'X'],
                 ['X', 'O', 'X', 'O']]

    massi = Player(1, "Massi", 1)
    jeu = Game((4, 4), massi)

    pion = Pawn(2, 0, 1)
    pion_left = Pawn(1, 0, 2)

    jeu.getLeftNeighbour(pion)
