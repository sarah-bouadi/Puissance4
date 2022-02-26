
from datetime import date
from pprint import pprint
from lib.grid import *
from lib.player import Player

import os

def saveGame(file_path, game, last_pawn_played_position):
    """
    Save the content of the grid_matrix into src/save.txt

    :param game: the game object to save 

    """
    with open(file_path, 'w') as f:
        #Game save date
        today = date.today()
        save_date = today.strftime("%d/%m/%Y")
        f.write(f"SAVE DATE: {save_date}\n")

        #Game mode
        if game.player2.name is None:
            f.write("GAME MODE: Player VS Computer\n")
        else:
            f.write("GAME MODE: Player VS Player\n")
        
        #Players datas
        f.write(f"PLAYER1: {game.player1.name} {game.player1.choosen_color}\n")
        f.write(f"PLAYER2: {game.player2.name} {game.player2.choosen_color}\n")

        #Grid Size
        f.write(f"GRID_SIZE: {game.grid.getSize()}\n")

        #Last played pawn position
        f.write(f"LAST_PLAYED_PAWN_POSITION: {last_pawn_played_position[0]} {last_pawn_played_position[1]}\n\n")

        #Grid matrix
        for i in range(game.grid.getSize()):
            for j in range(game.grid.getSize()):
                f.write(game.grid.grid_to_save[i][j]+'|')
            f.write('\n')

def uploadGame(file_path):
    """
    Upload the grid matrix from src/save.txt

    :param filename: the path to the save file
    
    :return: the grid matrix in str format

    """
    with open(file_path,'r') as f:
        #Player
        savefile = f.readlines()
        game_mode = (savefile[1]).split(" ")
        player1_datas = (savefile[2]).split(" ")
        player2_datas = (savefile[3]).split(" ")
        grid_size = (savefile[4]).split(" ")
        last_pawn_played_position = (savefile[5]).split(" ")

        #Charge players datas
        player1 = Player(player1_datas[1], player1_datas[2])
        
        if game_mode[4] == 'Player\n':
            player2 = Player(player2_datas[1], player2_datas[2])
        else:
            player2 = Player(None, player2_datas[2])

        #Charge the last played pawn position
        pawn_position = (int(last_pawn_played_position[1]), int(last_pawn_played_position[2].strip('\n')))  

        #Charge grid
        grid = Grid(int(grid_size[1].replace('\n','')))
        result_grid = []
        for i in savefile[7:]: 
            row = i.split('|')
            result_grid.append(row[0:-1])
        grid.convert_gridtxt_gridobject(result_grid)
        return (grid, player1, player2, pawn_position)
