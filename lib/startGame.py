"""
Menu of the game 
"""

def input_quit_game():
    confirmation_quit = input("Are you sure to quit the game ? (y/n)")
    if confirmation_quit.lower() == 'y':
        exit()
    elif confirmation_quit.lower() == 'n':    
        pass
        #start_menu()
    else:
        print("Bad enterring, Retry: ")
        input_quit_game()

def game_mode_menu():
    print("##### Game Mode #####", end="\n\n")
    print("- 1 - Player vs Player")
    print("- 2 - Player vs Computer ")
    print("- 3 - Return to game start", end="\n\n")

def start_menu():
    print("##### PUISSANCE 4 #####", end="\n\n")
    print("- 1 - Start a new game")
    print("- 2 - Continue a game ")
    print("- 3 - Quit", end="\n\n")

    start_choice = input("- Please enter your choice: ")

    if start_choice == 1:
        game_mode_menu()
    elif start_choice == 2:
        pass
        #startGame()
    elif start_choice == 3:
        input_quit_game()
    else:
        print("Bad Entrering, please Retry: ")
        start_menu()

def start_game():
    pass