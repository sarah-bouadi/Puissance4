# Classe Pawn, represent the pawn, each one could be Yellow or Red


class Pawn:



    test_grid = [['.', '.', '.', '.'],
                 ['X', 'X', '.', 'O'], 
                 ['X', 'O', 'O', 'X'],
                 ['X', 'O', 'X', 'O']]

    '''Constructor of the class'''
    def __init__(self, column, row=0, color=None):
        self.color = color
        self.column = column
        self.row = row
        self.position = (self.row, self.column)

    # Return the color of the Pawn
    @property
    def color(self):
        """
        :return: the pawn's color
        """
        colors = {1: "red", 2: "yellow"}
        try:
            int(self.__color)
            return colors[self.__color]
        except Exception as e:
            print("Veuillez d'abord attribuer une couleur")


    # Set a color to the pawn
    @color.setter
    def color(self, color):
        self.__color = color

    # Return the column of the pawn
    @property
    def column(self):
        return self.__column

    # Set a column to a pawn
    @column.setter
    def column(self, column):
        self.__column = column
    
    # Return the row of the pawn
    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, row):
        self.__row = row
        
    # Return the position of the pawn
    @property
    def position(self):
        return self.__position
    
    # Set a position to a pawn
    @position.setter
    def position(self, position):
        self.__position = position


    def __str__(self):
        return f"({self.color}, {self.position})"