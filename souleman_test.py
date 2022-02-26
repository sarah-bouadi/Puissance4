
    #Initialize the grid with grid_size     
from lib.menu import Start_Game
from lib.pawn import *
from lib.game import *
from lib.player import *
from lib.save import *


if __name__ == "__main__":

    pion_rouge = Pawn(1)
    pion_jaune = Pawn(2)

    grid = Grid(4)
    grid.initMatrix()
    grid.display()

    player_naruto = Player(1, "Naruto")

    players_datas = player_naruto.initialize_P_vs_P()
    player1 = players_datas[0]
    player2 = players_datas[1]

    print(player1, player1.choosen_color)
    print(player2, player2.choosen_color)

    player1.add_pawn_grid(grid, 0)
    player1.add_pawn_grid(grid, 0)
    player2.add_pawn_grid(grid, 0)
    player2.add_pawn_grid(grid, 2)
    player1.add_pawn_grid(grid, 1)

    print(grid.isFull())

    print(grid)
    grid.display()
    saveGame('src/save.txt',grid, player1, player2)
    player2.add_pawn_grid(grid, 2)
    player1.add_pawn_grid(grid, 1)
    grid.display()

    game = Game
    print(grid, grid.grid_to_save)
    saveGame('src/save.txt', game)

    # del grid, player1, player2
    # print("###################################")
    # uploadeDatas = uploadGame('src/save.txt')
    # grid = uploadeDatas[0]
    # player1 = uploadeDatas[1]
    # player2 = uploadeDatas[2]

    # print(player1, player1.choosen_color)
    # print(player2, player2.choosen_color)
    # print(grid)

    # startGame = Start_Game()
    # entery = startGame.input_entering("lets see:", [1,2,3,4,'q'])
    # print(entery, type(entery))

    # player1.add_pawn_grid(grid, int(player1.choosen_color), 1)
    # player2.add_pawn_grid(grid, int(player2.choosen_color), 0)

    # startGame = Start_Game()
   
    # startGame.grid = grid
    # startGame.play_game()

    # print(grid)

