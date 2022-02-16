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
    
