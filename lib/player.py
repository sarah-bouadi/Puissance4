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
            return self.__choosen_color

        @choosen_color.setter
        def choosen_color(self, choosen_color):
            """
            choosen_color setter
            :param choosen_color: the choosen_color to attribute
            """
            self.__choosen_color = choosen_color

            # Returns a tuple like: ((player1_id, player1_name), (player2_id, player2_name))

    def initialize_P_vs_P(self):
        player1_name = input("- Enter the name of player 1: ")
        player1_choosen_color = input("- Select your color (1- for red, 2- for yellow):")

        player2_name = input("- Enter the name of player 2: ")
        player2_choosen_color = input("- Select your color (1- for red, 2- for yellow):")
        return (self.__init__(player1_choosen_color, player1_name), self.__init__(player2_choosen_color, player2_name))

    # Returns a tuple like: ((player1_id, player1_name), (player2_id, player2_name))
    def initialize_P_vs_computer(self):
        player1_name = input("- Enter the name of player 1: ")
        player1_choosen_color = input("- Select your color (1- for red, 2- for yellow):")

        return ((player1_choosen_color, player1_name), (None, None))

    def add_pawn_grid(self, grid, color, column):
        """
        add a pawn to a grid or says if the choosen column is full
        :param grid: the grid where the pawn will be added
        :param color: the color of the pawn
        :param column: the choosen column
        """
        pawn = Pawn(color)
        row = grid.get_grid_row_from_column(column)
        if row is not None:
            pawn.row = row
            print("row:", pawn.row, "column:", column)
            pawn.column = column
            grid.matrix[row][column] = pawn
        else:
            print("Column is full, please choose another column")

    def __str__(self):
        return "Name: {}; Color: {}".format(self.name, self.choosen_color)
