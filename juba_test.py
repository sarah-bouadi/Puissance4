from lib.grid import *
from lib.pawn import *

if __name__ == "__main__":
    #grille = [[None, 1, None, None],
              # [None, None, None, None],
              # [None, None, None, None],
              # [None, None, 2, None],
              # ]
    grille = Grid(4)
    grille.initMatrix()
    pion = Pawn(1)


    grille.add_pawn_grid(pion, 3)
    grille.display()
