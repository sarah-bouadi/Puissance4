"""
Author: TRAORE Souleman

Date: 24.01.2022

Start game class, for the user interactions.

"""

from curses.ascii import isdigit
import lib.grid as gridz
import lib.save as save
import lib.player as player
import lib.game as game


class Start_Game:
    def __init__(self) -> None:
        pass

    def input_quit_game(self):
        """
        Confirm if must quit the game or cancel it to return to 
        game start menu
        """
        confirmation_quit = input("Are you sure to quit the game ? (y/n)")
        if confirmation_quit.lower() == 'y':
            exit()
        elif confirmation_quit.lower() == 'n':    
            self.start_menu_choices()
        else:
            print("Bad enterring, Retry: ")
            self.input_quit_game()

    def input_entering(self, msg, good_entering_list):
        """
        Return the user's input if it is in the indicated list
        :param msg: Message to print before the input
        :param good_entering_list: List of good inputs

        :return : The user's good input
        """
        entering = input(msg)

        try:
            if isinstance(good_entering_list, list) and isinstance(entering, str):
                if (entering in good_entering_list) or (int(entering) in good_entering_list):
                    return entering
                else:
                    print("*Bad input, your input must be in",good_entering_list, end='\n\n')
                    entering = self.input_entering(msg, good_entering_list)
                    return entering

        except:
            print("You must use a list in second parameter or entering letters without accents.")
            print("*Bad input, your input must b in",good_entering_list)
            entering = self.input_entering(msg, good_entering_list)
            return entering

    def print_start_menu(self):
        """
        Prints the start game menu
        """
        print("##### PUISSANCE 4 #####", end="\n\n")
        print("- 1 - Start a new game")
        print("- 2 - Continue a game ")
        print("- 3 - Quit the game", end="\n\n")

    def print_game_mode_menu(self):
        """
        Prints the game mode menu
        """
        print("##### Game Mode #####", end="\n\n")
        print("- 1 - Player vs Player")
        print("- 2 - Player vs Computer")
        print("- 3 - Return to game start menu")
        print("- 4 - Quit to game ", end="\n\n")

    def display_grid(self):
        """
        Display the grid
        """
        self.grid.display()

    def game_mode_choices(self):  
        """
        Ask an input to the user to
        - iniatialize two user :It creates two players instances in this class
        - return to the game start menu
        - or quit the game
        """  
        start_choice = self.input_entering("- Please enter your choice: ",[1,2,3,4])
        start_choice = int(start_choice)
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
        #Quit the game
        elif start_choice == 4:
            self.input_quit_game() 

        #initialize players
        if start_choice == 1 or start_choice == 2:
            #Initialize players
            self.player1 = players_datas[0]
            self.player2 = players_datas[1]
            print(self.player1)
            print(self.player2)      

        #Play the game
        self.play_game() 

    def start_menu_choices(self):  
        """
        Ask an input to the user to :
        - start a new game and initialize the grid
        - continue from a saved game
        - or quit the game
        """ 
        start_choice = self.input_entering("- Please enter your choice: ",[1,2,3])
        start_choice = int(start_choice)
        #Create a new game
        if start_choice == 1:
            #Initialize grid
            print("-****** Grid Size ******-", end='\n')
            grid_size = self.input_entering("- Please enter the grid size: ", list(range(100)))
            while int(grid_size)<=3:
                print("* Bad size input, you must enter size > 3. Please retry.",end='\n\n')
                grid_size = self.input_entering("- Please enter the grid size: ", list(range(100)))

            self.game_save_file_path = input("\nType the name of this session(without extension): ")
            self.game_save_file_path = 'src/' + self.game_save_file_path + '.txt'
            self.grid = grid.Grid(int(grid_size))
            self.grid.initMatrix()
            self.display_grid()

            #Game mode menu and choices
            self.print_game_mode_menu()
            self.game_mode_choices()
        #Continue a saved game
        elif start_choice == 2:
            self.game_save_file_path = input("\nType the name of the game session (without extension): ")
            self.game_save_file_path = 'src/' + self.game_save_file_path + '.txt'
            print("* Charging last game session......")
            import os
            if os.path.exists(self.game_save_file_path):
                #Charge str matrix
                uploadeDatas = save.uploadGame(self.game_save_file_path)
                self.grid = uploadeDatas[0]
                self.player1 = uploadeDatas[1]
                self.player2 = uploadeDatas[2]
                if self.grid.isFull():
                    self.grid.initMatrix()
                print("***** Game session charged *****")
                self.play_game()
            else:
                print("There is no such save file, please start a new game")
                self.lauch_game()
        #Quit the game
        elif start_choice == 3:
            self.input_quit_game()

    def switch_player(self):
        """
        Switch the current_player instance between player1 and player2 instances
        """
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play_game(self):
        """
            Play the game
        """
        valid_entries = list(range(self.grid.getSize()))
        valid_entries.append('q')
        self.current_player = self.player1
        our_input = 1
        status = False 
        while our_input!='q' and not self.grid.isFull() and not status:
            print(self.grid)
            
            our_input = self.input_entering(f"*It is player {self.current_player.name} turn now: ", valid_entries)
            if our_input == 'q':
                #Ask a confirmation to quit the game
                entery = self.input_entering("Do you really want to quit the game?(y/n)",['y','n'])
                if entery == 'y':
                    save.saveGame(self.game_save_file_path, self.grid, self.player1, self.player2)
                    exit()
            else:
                column_input = int(our_input)

            #Add a new pawn in the grid
            self.current_player.add_pawn_grid(self.grid, column_input)
            
            #Check the winner
            # row = self.grid.get_grid_row_from_column(column_input) - 1
            # status = game.checkWinner(self.grid,self.grid.getMatrix()[row][column_input], self.player1, self.player2)
            
            #Switch the players
            self.switch_player()

            #Automatic grid save
            self.grid.display()
            save.saveGame(self.game_save_file_path, self.grid, self.player1, self.player2)
          
            if self.grid.isFull():
                print("**** No Winners !****")
                entery = self.input_entering("Do you want to restart?(y/n)",['y','n'])
                if entery == 'y':
                    self.grid.initMatrix()
                    self.grid.display()
                    # save.saveGame(self.game_save_file_path, self.grid, self.player1, self.player2)

                    # self.print_start_menu()
                    # self.start_menu_choices()
                else:
                    import os
                    if os.path.exists(self.game_save_file_path):
                        os.remove(self.game_save_file_path)
            
    def lauch_game(self):
        self.print_start_menu()
        self.start_menu_choices()