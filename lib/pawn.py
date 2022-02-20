# Classe Pawn, represent the pawn, each one could be Yellow or Red

COLORS = {1: "red", 2: "yellow"}
class Pawn:

    '''Constructor of the class'''
    def __init__(self, color=None):
        self.color = color
        self.column = int()
        self.row = int()
        self.position = self._get_pawn_position()

    # Return the color of the Pawn
    @property
    def color(self):
        """
        :return: the pawn's color
        """

        try:
            int(self.__color)
            return COLORS[self.__color]
        except Exception as e:
            print("Veuillez d'abord attribuer une couleur")


    @color.setter
    def color(self, color):
        """
        color setter
        :param color: (1: red, 2: yellow)
        """
        self.__color = color

    @property
    def column(self):
        """
        column getter
        :return: the pawn's column
        """
        return self.__column

    @column.setter
    def column(self, column):
        """
        column setter
        :param column: the column to attribute
        """
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

    def _get_pawn_position(self):
        return (self.row, self.column)

    def __str__(self):
        if self.color == "red":
            return " X "
        else:
            return " O "

            