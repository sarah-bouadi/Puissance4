from lib.grid import *
from lib.pawn import *
from lib.player import *

if __name__ == "__main__":
    #grille = [[None, 1, None, None],
              # [None, None, None, None],
              # [None, None, None, None],
              # [None, None, 2, None],
              # ]
    grille = Grid(4)
    grille.initMatrix()
    pion = Pawn(1)
    player1 = Player("Reda", 1)

    player1.add_pawn_grid(grille, 1, 2)
    print(grille)

