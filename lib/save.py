"""
Author: TRAORE Souleman

Date: 24.01.2022

Contains Saving and uploading the game grid.

"""

from datetime import date
from pprint import pprint
from lib.grid import *
from lib.player import Player

import os

def saveGame(file_path, grid, player1, player2):
    """
    Save the content of the grid_matrix into src/save.txt

    :param grid: the grid object to use the grid_matrix to save and the grid size
    :param player1: the player 1 to use his datas
    :param player2: the player 2 to use his datas

    """
    with open(file_path, 'w') as f:
        #Game save date
        today = date.today()
        save_date = today.strftime("%d/%m/%Y")
        f.write(f"SAVE DATE: {save_date}\n")

        #Game mode
        if player2.name is None:
            f.write("GAME MODE: Player VS Computer\n")
        else:
            f.write("GAME MODE: Player VS Player\n")
        
        #Players datas
        f.write(f"PLAYER1: {player1.name} {player1.choosen_color}\n")
        f.write(f"PLAYER2: {player2.name} {player2.choosen_color}\n")

        #Grid Size
        f.write(f"GRID_SIZE: {grid.getSize()}\n\n")

        #Grid matrix
        for i in range(grid.getSize()):
            for j in range(grid.getSize()):
                f.write(grid.grid_to_save[i][j]+',')
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

        #Charge players datas
        player1 = Player(player1_datas[1], player1_datas[2])
        
        if game_mode[4] == 'Player\n':
            player2 = Player(player2_datas[1], player2_datas[2])
        else:
            player2 = Player(None, player2_datas[2])

        #Charge grid
        grid = Grid(int(grid_size[1].replace('\n','')))
        result_grid = []
        for i in savefile[6:]: 
            row = i.split(',')
            result_grid.append(row[0:-1])
        grid.convert_gridtxt_gridobject(result_grid)
        return (grid, player1, player2)
