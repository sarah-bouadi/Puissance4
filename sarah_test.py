from lib.grid import *
from lib.player import *
grid = Grid(4)

grid.initMatrix()


grid.display()

print(grid)


pion_rouge = Pawn(1)
pion_jaune = Pawn(2)

grid = Grid(4)
grid.initMatrix()
grid.display()

row = grid.get_grid_row_from_column(2)

player_naruto = Player(1, "Naruto")
print(player_naruto)

#print(row)
player_naruto.add_pawn_grid(grid, 1, 0)
player_naruto.add_pawn_grid(grid, 2, 0)
player_naruto.add_pawn_grid(grid, 2, 0)
player_naruto.add_pawn_grid(grid, 2, 0)
player_naruto.add_pawn_grid(grid, 2, 0)
player_naruto.add_pawn_grid(grid, 2, 2)
player_naruto.add_pawn_grid(grid, 1, 1)
player_naruto.add_pawn_grid(grid, 1, 1)
player_naruto.add_pawn_grid(grid, 1, 1)
player_naruto.add_pawn_grid(grid, 1, 1)
player_naruto.add_pawn_grid(grid, 2, 2)
player_naruto.add_pawn_grid(grid, 2, 2)
player_naruto.add_pawn_grid(grid, 2, 2)
player_naruto.add_pawn_grid(grid, 2, 3)
player_naruto.add_pawn_grid(grid, 2, 3)
player_naruto.add_pawn_grid(grid, 2, 3)
player_naruto.add_pawn_grid(grid, 2, 3)

print(grid)

grid.isFull()
print(grid.isFull())
