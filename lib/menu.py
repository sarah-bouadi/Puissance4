"""
Menu of the game 
"""

class Menu:
    def __init__(self) -> None:
        pass

    def input_quit_game(self):
        confirmation_quit = input("Are you sure to quit the game ? (y/n)")
        if confirmation_quit.lower() == 'y':
            exit()
        elif confirmation_quit.lower() == 'n':    
            pass
            #start_menu()
        else:
            print("Bad enterring, Retry: ")
            self.input_quit_game()

    def input_entering(self, msg, good_entering_list):
        entering = input(msg)
        try:
            if isinstance(good_entering_list, list):
                if entering in list:
                    return entering
                else:
                    print("Bad entering, please retry: ")
                    self.input_entering(msg, good_entering_list)
        except:
            raise AttributeError("You must use a list.")

    def print_start_menu(self):
        print("##### PUISSANCE 4 #####", end="\n\n")
        print("- 1 - Start a new game")
        print("- 2 - Continue a game ")
        print("- 3 - Quit", end="\n\n")
 

    def print_game_mode_menu(self):
        print("##### Game Mode #####", end="\n\n")
        print("- 1 - Player vs Player")
        print("- 2 - Player vs Computer ")
        print("- 3 - Return to game start", end="\n\n")

    def game_mode_menu(self):    
        start_choice = self.input_entering("- Please enter your choice: ",[1,2,3])

        #Create a new game
        if start_choice == 1:
            self.initialize_P_vs_P()
        #Continue a saved game
        elif start_choice == 2:
            self.initialize_P_vs_computer()
        #Quit the game
        elif start_choice == 3:
            self.input_quit_game()

    def initialize_grid(self, grid):
        print("-****** Grid Size ******-", end='\n')
        grid_size = input("- Please enter the grid size: ", list(range(100)))

        #Initialize the grid with grid_size
    
    #Returns a tuple like: ((player1_id, player1_name), (player2_id, player2_name))
    def initialize_P_vs_P(self):
        player1_name = input("- Enter the name of player 1: ")
        player1_id = input("- Enter the id of player 1: ")

        player2_name = input("- Enter the name of player 2: ")
        player2_id = input("- Enter the id of player 2: ")
        return ((player1_id, player1_name), (player2_id, player2_name))

    #Returns a tuple like: ((player1_id, player1_name), (player2_id, player2_name))
    def initialize_P_vs_computer(self):
        player1_name = input("- Enter the name of player 1: ")
        player1_id = input("- Enter the id of player 1: ")

        return ((player1_id, player1_name), (None, None))
                

def start_game():
    print_start_menu()
    start_menu()
