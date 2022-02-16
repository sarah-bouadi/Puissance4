

import lib.menu as sg

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

if __name__ == "__main__":
    sg.start_menu()       
