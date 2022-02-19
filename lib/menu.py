"""
Start_Game of the game 
"""

import lib.grid as grid
import lib.save as save
import lib.player as player

class Start_Game:
    def __init__(self) -> None:
        # self.grid = None
        pass

    def input_quit_game(self):
        confirmation_quit = input("Are you sure to quit the game ? (y/n)")
        if confirmation_quit.lower() == 'y':
            exit()
        elif confirmation_quit.lower() == 'n':    
            self.start_menu_choices()
        else:
            print("Bad enterring, Retry: ")
            self.input_quit_game()

    def input_entering(self, msg, good_entering_list):
        entering = int(input(msg))
        # if entering in good_entering_list:
        #     return entering
        # else:
        #     print("Bad entering, please retry: ")
        #     self.input_entering(msg, good_entering_list)

        try:
            if isinstance(good_entering_list, list):
                if entering in good_entering_list:
                    return entering
                else:
                    print("Bad entering !", end='\n\n')
                    self.input_entering(msg, good_entering_list)
        except:
            raise AttributeError("You must use a list.")

    def print_start_menu(self):
        print("##### PUISSANCE 4 #####", end="\n\n")
        print("- 1 - Start a new game")
        print("- 2 - Continue a game ")
        print("- 3 - Quit the game", end="\n\n")

    def print_game_mode_menu(self):
        print("##### Game Mode #####", end="\n\n")
        print("- 1 - Player vs Player")
        print("- 2 - Player vs Computer")
        print("- 3 - Return to game start")
        print("- 4 - Quit to game ", end="\n\n")

    def display_grid(self):
        self.grid.display()

    def game_mode_choices(self):    
        start_choice = self.input_entering("- Please enter your choice: ",[1,2,3,4])
        players_datas = ()
        tmp = player.Player(0, "Tanjiro")
        #Create a new game
        if start_choice == 1:
            players_datas = tmp.initialize_P_vs_P()
        #Continue a saved game
        elif start_choice == 2:
            players_datas = tmp.initialize_P_vs_computer()
        #Return to game mode
        elif start_choice == 3:
            self.print_start_menu()
            self.start_menu_choices()
            self.print_game_mode_menu()
            self.game_mode_choices()
        #Quit the game
        elif start_choice == 4:
            self.input_quit_game() 

        if start_choice == 1 or start_choice == 2:
            #Initialize players
            self.player1 = players_datas[0]
            self.player2 = players_datas[1]
            print(self.player1)
            print(self.player2)       

    def start_menu_choices(self):  
        start_choice = self.input_entering("- Please enter your choice: ",[1,2,3])

        #Create a new game
        if start_choice == 1:
            print("-****** Grid Size ******-", end='\n')
            grid_size = None
            while not isinstance(grid_size, int):
                grid_size = self.input_entering("- Please enter the grid size: ", list(range(100)))

            self.grid = grid.Grid(grid_size)
            self.grid.initMatrix()
            self.display_grid()
        #Continue a saved game
        elif start_choice == 2:
            #Charge str matrix
            saved_matrix = save.uploadFile('src/save.txt')
            #Convert into Pawn object matrix
            # self.grid.matrix = grid.str_to_pawn_matrix(saved_matrix)
        
        #Quit the game
        elif start_choice == 3:
            self.input_quit_game()