class Player():

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @property
    def id(self):
        """
        id getter
        :return: the player's id
        """
        return self.__id

    @id.setter
    def id(self, id):
        """
        id setter
        :param id: the id to attribute
        """
        self.__id = id    

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

        #Returns a tuple like: ((player1_id, player1_name), (player2_id, player2_name))
    def initialize_P_vs_P(self):
        player1_name = input("- Enter the name of player 1: ")
        player1_id = input("- Enter the id of player 1: ")

        player2_name = input("- Enter the name of player 2: ")
        player2_id = input("- Enter the id of player 2: ")
        return (self.__init__(player1_id, player1_name), self.__init__(player2_id, player2_name))

    #Returns a tuple like: ((player1_id, player1_name), (player2_id, player2_name))
    def initialize_P_vs_computer(self):
        player1_name = input("- Enter the name of player 1: ")
        player1_id = input("- Enter the id of player 1: ")

        return ((player1_id, player1_name), (None, None))    
             
    def __str__(self):
        return "Player number: {} ;Name: {}".format(self.id, self.name)
