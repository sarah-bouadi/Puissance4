from lib.grid import *
from lib.pawn import *
from lib.player import *
from lib.game import *
from lib.save import *

if __name__ == "__main__":
    #grille = [[None, 1, None, None],
              # [None, None, None, None],
              # [None, None, None, None],
              # [None, None, 2, None],
              # ]


    # grille = Grid(4)
    # grille.initMatrix()
    # pion = Pawn(1)
    # player1 = Player("Reda", 1)
    # player2 = Player("Souleman", 2)
    # jeu = Game(grille, player1)

    # player1.add_pawn_grid(grille, 1)
    # player1.add_pawn_grid(grille, 1)
    # player1.add_pawn_grid(grille, 1)

    # player2.add_pawn_grid(grille, 2)
    # player2.add_pawn_grid(grille, 2)
    # player2.add_pawn_grid(grille, 2)

    # print(grille)

    #print(jeu.count_right_neighbour(grille, grille.matrix[3][0]))
    #print(jeu.checkVerticalWinner(grille, grille.matrix[3][1]))
    #print(jeu.getLeftNeighbour(grille, grille.matrix[3][0]))
    #print(jeu.count_left_neighbour(grille, grille.matrix[3][3]))
    #print(jeu.checkVerticalWinner(grille, grille.matrix[3][1]))
    #print(jeu.count_down_neighbour(grille, grille.matrix[0][1]))
    #print(jeu.getDownNeighbour(grille, grille.matrix[0][1]))
    #print(jeu.getPawn(grille, 1, 1))
    #print(jeu.getDiagonalLeftDownNeighbour(grille, grille.matrix[3][1]))
    #print(jeu.count_diagonal_right_neighbour(grille, grille.matrix[3][1]))
    #print(jeu.checkRightDiagonalWinner(grille, grille.matrix[3][0]))
    #print(jeu.getDiagonalLeftUpNeighbour(grille, grille.matrix[3][3]))
    #print(jeu.count_diagonal_right_neighbour(grille, grille.matrix[2][2]))
    #print(jeu.checkLeftDiagonalWinner(grille, grille.matrix[3][3]))


    uploadeDatas = uploadGame('src/save.txt')

    grille = uploadeDatas[0]
    player1 = uploadeDatas[1]
    player2 = uploadeDatas[2]

    jeu = Game(grille, player1, player2)
    jeu.grid = grille
    jeu.player1 = player1
    jeu.player2 = player2

    print(jeu.grid)

    # for i in range(jeu.grid.getSize()):
    #     for j in range(jeu.grid.getSize()):
    #         print(jeu.grid.matrix[i][j], end=" ")
    #     print("\n")

    # print(jeu.getPawn(0, 0))    


    # print(grille, player1, player2, grille.matrix[0][1])
    # print(jeu.grid)
    # test = jeu.getDownNeighbour(jeu.grid.matrix[1][3])
    # test = jeu.getPawn(2, 3)
    # print(jeu.grid.matrix[1][3].row, jeu.grid.matrix[1][3].column)
    # print(test, type(test))
    # print(jeu.getDownNeighbour(jeu.grid.matrix[1][2]))
    print(jeu.checkWinner(jeu.grid.matrix[0][3]))
