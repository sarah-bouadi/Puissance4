# Classe Pawn, represent the pawn, each one could be Yellow or Red


class Pawn():

    # Constructor of the class
    def __init__(self, color, column, row):
        self.color = color
        self.column = column
        self.row = row
        self.position = (row, column)

    # Return the color of the Pawn
    def getColor(self):
        return self.color
    
    # Set a color to the pawn
    def setColor(self, color):
        self.color = color
    
    # Return the position of the pawn
    def getPosition(self):
        return self.position
    
    # Set a position to a pawn
    def setPosition(self, position):
        self.position = position

    # Return the column of the pawn
    def getColumn(self):
        return self.column

    # # Set the column of the pawn
    # def setColumn(self,column):
    #     if column>=0 or column<=0 and cel.siEmpty():
    #         self.column = column
    #     else: 
    #         raise ValueError('Saisir une colonne valide !')

    # Return the row of the pawn
    def getRow(self):
        return self.row

    # # Set the row of the pawn
    # Je doute encore de l'utilité de cette méthode car le joueur ne choisit que les colonnes et jamais les lignes
    # def setRow(self,row):
    #     if row>=0 or row<=0 and cel.siEmpty():
    #         self.row = row
    #     else: 
    #         raise ValueError('Saisir une ligne valide !')

    
        
