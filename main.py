##
# @auth: Reese Russell
# @desc: Python Maze Solver

#Dependencies
import sys
import maze_functions as mazeLib
#Constants (non pythonic)
debug = True
lut = None
grid = [[0,0,1,0],
        [1,0,0,1],
        [1,1,0,0],
        [1,1,1,0]]
#Get some info about the 2D array analysis
cols = len(grid[0])
rows = len(grid)
# Quick check to make sure the user isn't throwing some bogus dims on the array for maze solver.
for col in range(rows):
    if len(grid[col]) != rows:
        sys.exit("Input grid is invlid: " + str(len(grid[col])) + " columns in row " + str(rows))
#Print out some debug info
if(debug):
    print("Your grid has " + str(rows) + " rows and " + str(cols) + " columns.")
#First Invert the matrix for easy if else clause gen
for i in range (cols):
    for j in range (rows):
        if grid[i][j] == 1:
            grid[i][j] = 0
        else:
            grid[i][j] = w
#Initialize the branch lookup table
lut = [[None for x in range(cols)] for y in range(rows)]
#Put the maze in a dictonary to make it readable and with easy to access parameters
maze = {'maze': grid, 'height': rows, 'width': cols}
#A tree will contain all of the branches
tree = []
#Store the current minimum for best_child checking
cur_min = None #The current minimum path
#Initial branch [[col, row, last traversed leaf index, leaves, wall_built]]
branch = {'x':0, 'y':0, 'leafs':[], 'wall_built': False, 'parent': None, 'steps':0}

mazeLib.leaf_gen(maze,branch)
mazeLib.grow_leafs(maze,branch)
