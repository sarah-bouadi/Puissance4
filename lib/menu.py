"""
Author: TRAORE Souleman

Date: 24.01.2022

Start game class, for the user interactions.

"""

import lib.grid as grid
import lib.save as save
import lib.player as player
import lib.game as game
from termcolor import colored
import os

class Start_Game:
    def __init__(self) -> None:
        self.last_pawn_played_position = (0, 0)

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
                    print(colored(f"*Bad input, your input must be between {good_entering_list[0]} and {good_entering_list[-1]}", "red"), end='\n\n')
                    entering = self.input_entering(msg, good_entering_list)
                    return entering

        except:
            print("You must use a list in second parameter or entering letters without accents.")
            print(colored(f"*Bad input, your input must be between {good_entering_list[0]} and {good_entering_list[-1]}", "red"), end='\n\n')
            entering = self.input_entering(msg, good_entering_list)
            return entering

    def print_start_menu(self):
        """
        Prints the start game menu
        """
        print(colored("##### PUISSANCE 4 #####", "blue"), end="\n\n")
        print("- 1 - Start a new game")
        print("- 2 - Continue a game ")
        print("- 3 - Quit the game", end="\n\n")

    def print_game_mode_menu(self):
        """
        Prints the game mode menu
        """
        print(colored("##### Game Mode #####", "yellow"), end="\n\n")
        print("- 1 - Player vs Player")
        print("- 2 - Player vs Computer")
        print("- 3 - Return to game start menu")
        print("- 4 - Quit to game ", end="\n\n")

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
            print(colored("-****** Grid Size ******-", "blue"), end='\n\n')
            grid_size = self.input_entering("- Please enter the grid size: ", list(range(100)))
            while int(grid_size)<=3:
                print(colored("* Bad size input, you must enter size > 3. Please retry.", "red"),end='\n\n')
                grid_size = self.input_entering("- Please enter the grid size: ", list(range(100)))

            self.game_save_file_path = input("\nType the name of this session(without extension): ")
            self.game_save_file_path = 'src/' + self.game_save_file_path + '.txt'
            self.grid = grid.Grid(int(grid_size))
            self.grid.initMatrix()
            print(self.grid)

            #Game mode menu and choices
            self.print_game_mode_menu()
            self.game_mode_choices()

            
        #Continue a saved game
        elif start_choice == 2:
            
            print("List of save files:")
            save_list = [print(i.replace('.txt', '')) for i in os.listdir('src')]
            
            self.game_save_file_path = input("\nType the name of the game session (without extension): ")
            self.game_save_file_path = 'src/' + self.game_save_file_path + '.txt'
            print(colored("**** .... Loading .... ****", "yellow"))
            
            if os.path.exists(self.game_save_file_path):
                #Charge str matrix
                uploadDatas = save.uploadGame(self.game_save_file_path)
                self.grid = uploadDatas[0]
                self.player1 = uploadDatas[1]
                self.player2 = uploadDatas[2]
                self.last_pawn_played_position = uploadDatas[3]
                if self.grid.isFull():
                    self.grid.initMatrix()
                print(colored("***** Game session charged *****", "green"))
                self.play_game()
            else:
                print(colored("There is no such save file, please start a new game", "red"))
                self.lauch_game()
        #Quit the game
        elif start_choice == 3:
            self.input_quit_game()

    def switch_player(self, game):
        """
        Switch the current_player instance between player1 and player2 instances
        """
        if self.current_player == game.player1:
            self.current_player = game.player2
        else:
            self.current_player = game.player1

    def play_game(self):
        """
            Play the game
        """
        valid_entries = list(range(self.grid.getSize()))
        valid_entries.append('q')
        
        our_input = 1

        self.game = game.Game(self.grid, self.player1, self.player2)
        self.game.grid = self.grid
        self.game.player1 = self.player1
        self.game.player2 = self.player2
        self.current_player = self.game.player1
        
        while our_input!='q' and not self.game.grid.isFull() and \
        not self.game.checkWinner(self.game.grid.getMatrix()[self.last_pawn_played_position[0]][self.last_pawn_played_position[1]]):
            print(self.game.grid)
            
            our_input = self.input_entering(f"* It is {self.current_player.name}'s turn: ", valid_entries)
            if our_input == 'q':
                #Ask a confirmation to quit the game
                entery = self.input_entering("Do you really want to quit the game?(y/n)\n",['y','n'])
                print(entery)
                if entery == 'y':
                    save.saveGame(self.game_save_file_path, self.game, self.last_pawn_played_position)
                    exit()
                else:
                    our_input = self.input_entering(f"* It is {self.current_player.name}'s turn: ", valid_entries)
                    column_input = int(our_input)  
            else:
                column_input = int(our_input) 

            #Add a new pawn in the grid
            self.current_player.add_pawn_grid(self.game.grid, column_input)

            # Check the winner
            row = self.game.grid.get_grid_row_from_column(column_input)
            if row is None:
                row = 0
            else:
                row = int(row) - 1

            self.last_pawn_played_position = (row, column_input)    

            #Switch the players
            self.switch_player(self.game)

            #Automatic grid save
            self.game.grid.display()
            save.saveGame(self.game_save_file_path, self.game, self.last_pawn_played_position)

            #If the grid is full
            if self.game.grid.isFull():
                if self.game.checkWinner(self.game.grid.getMatrix()[self.last_pawn_played_position[0]][self.last_pawn_played_position[1]]):
                    break
                print(colored("**** No Winners !****", "red"), end='\n\n')
                entery = self.input_entering("Do you want to restart the game?(y/n)\n",['y','n'])
                if entery == 'y':
                    self.game.grid.initMatrix()
                    self.game.grid.display()
                    save.saveGame(self.game_save_file_path, self.game, self.last_pawn_played_position)

                    self.print_start_menu()
                    self.start_menu_choices()
                #The case that the grid is full, we will remove its save file
                else:
                    print("")
                    import os
                    if os.path.exists(self.game_save_file_path):
                        os.remove(self.game_save_file_path)   
            
    def lauch_game(self):
        self.print_start_menu()
        self.start_menu_choices()