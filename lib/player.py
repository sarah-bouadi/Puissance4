from warnings import WarningMessage
from lib.pawn import *


class Player:

    def __init__(self, name, choosen_color):
        self.name = name
        self.choosen_color = choosen_color

    @property
    def name(self):
        """
        name getter
        :return: the player's name
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        id setter
        :param name: the name to attribute
        """
        self.__name = name

    @property
    def choosen_color(self):
        """
        choosen_color getter
        :return: the player's choosen_color
        """
        return int(self.__choosen_color)

    @choosen_color.setter
    def choosen_color(self, choosen_color):
        """
        choosen_color setter
        :param choosen_color: the choosen_color to attribute
        """
        self.__choosen_color = choosen_color

        # Returns a tuple like: ((player1_id, player1_name), (player2_id, player2_name))

    def initialize_P_vs_P(self):
        """
        Return two object instance of 2 human Players with inputed datas
        
        :return: A tuple which contains player1 and player2 like
            (player1, player2)

        """
        try:
            player1_name = input("- Enter the name of player 1: ")
            player1_choosen_color = input("- Select your color (1- for red, 2- for yellow):")
            if player1_choosen_color not in [1,2]:
                player1_choosen_color = 1

            player2_name = input("- Enter the name of player 2: ")
            player2_choosen_color = input("- Select your color (1- for red, 2- for yellow):")
            #Correct player2 input if needs
            if int(player1_choosen_color) == 1:
                player2_choosen_color = 2
            else:
                player2_choosen_color = 1

            players_datas = (Player(player1_name, int(player1_choosen_color)), Player(player2_name, int(player2_choosen_color)))
            return players_datas
        except Exception as err:
            print(err)
            return self.initialize_P_vs_P()

    # Returns a tuple like: ((player1_id, player1_name), (player2_id, player2_name))
    def initialize_P_vs_computer(self):
        """
        Return two object instance of 1 human and 1computer Players with inputed datas
        
        :return: A tuple which contains player1 and computer like
            (player1, computer) and with computer data as Nones

        """
        try:
            player1_name = input("- Enter the name of player 1: ")
            player1_choosen_color = input("- Select your color (1- for red, 2- for yellow):")
            if player1_choosen_color == 1:
                player2_choosen_color = 2
            else:
                player2_choosen_color = 1
            players_datas = (Player(player1_name, player1_choosen_color), Player(None, player2_choosen_color))
            return players_datas
        except Exception as err:
            print(err)
            return self.initialize_P_vs_computer()

    def add_pawn_grid(self, grid, column):
        """
        Add a pawn to a grid or says if the choosen column is full
        :param grid: the grid where the pawn will be added
        :param color: the color of the pawn
        :param column: the choosen column
        """
        try:
            pawn = Pawn(self.choosen_color)
            row = grid.get_grid_row_from_column(column)
            if row is not None:
                pawn.row = row
                print("row:", pawn.row, "column:", column)
                pawn.column = column
                grid.matrix[row][column] = pawn
                return True
            else:
                print("Column is full, please choose another column")
        except Exception as er:
            print(er)
            return False

    def __str__(self):
        return "Name: {}; Color: {}".format(self.name, self.choosen_color)
