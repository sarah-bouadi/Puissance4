#Initialize the grid with grid_size     
from lib.pawn import *
from lib.game import *
import lib.menu as sg


def game_init():
    start_game = sg.Start_Game()

    start_game.print_start_menu()
    start_game.start_menu_choices()


if __name__ == "__main__":
    game_init()