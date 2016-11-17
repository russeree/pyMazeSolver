##
# @auth: Reese Russell
# @desc: Python Maze Solver
#

#Dependencies
import sys
import maze_functions as mazeLib
#Constants (non pythonic)
debug = True
grid = [[0,1,1,0],
        [0,0,0,1],
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
            grid[i][j] = 1

#Put the maze in a dictonary to make it readable and with easy to access parameters
maze = {'maze': grid, 'height': rows, 'width': cols}
#solve the maze for min condition with 1 wall change
#2d arrays are array[row][column]
cur_min = None
#Initial branch [[col, row, last traversed leaf index, leaves, wall_built]]
branch = {'x': 0, 'y': 0, 'last_leaf': 0, 'leafs':[], 'wall_built': False}

mazeLib.leaf_gen(maze,branch)
