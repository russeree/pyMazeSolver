##
# @auth: Reese Russell
# @desc: Python Maze Solver

#Dependencies
import sys
import maze_functions as mazeLib

##
# @Schedule
# 1. Add another node that starts at another valid seed location and uses
# another thread/process, once a branch has been exhausted, list it's shortest
# path in another lookup table, There will be 2 luts, one for solve paths with
# walls and one for without, if the leaf is set to become a branch at that point
# evaluate it to see if it higher or lower than that paths shortest value, if lower
# sum and added to list of complete, if higher kill the leaf. This should be
# added to the leaf destruction tab.

#Constants (non pythonic)
debug = True
lut = None
opt_lut = None
grid = [[0, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 0]]
#Get some info about the 2D array analysis
cols = len(grid[0])
rows = len(grid)
#Print out some debug info
if(debug):
    print("Your grid has " + str(rows) + " rows and " + str(cols) + " columns.")
#First Invert the matrix for easy if else clause gen
for i in range (len(grid)):
    for j in range (len(grid[i])):
        if grid[i][j] == 1:
            grid[i][j] = 0
        else:
            grid[i][j] = 1
for i in grid:
    print(i)
#Keep a list of maze path values
path_lengths = []
#Initialize the branch lookup table
lut = [[[] for x in range(cols)] for y in range(rows)]
opt_lut = [[{'wall': None, 'no_wall': None} for x in range(cols)] for y in range(rows)]
#Put the maze in a dictonary to make it readable and with easy to access parameters
maze = {'maze': grid, 'height': rows, 'width': cols}
#Initial branch [[col, row, last traversed leaf index, leaves, wall_built]]
branch = {'x':0, 'y':0, 'leafs':[], 'wall_built': False, 'parent': None, 'steps':0}
#Run the iterator for the maze
mazeLib.iterator(branch, maze, lut, path_lengths, opt_lut)
#Sort the results and print the minimum
path_lengths.sort()
print("The shortest path is " +  str(path_lengths[0] + 1))
