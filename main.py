##
# @auth: Reese Russell
# @desc: Python Maze Solver
##
#Some system imports
import sys
#Constants
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

#solve the maze for min condition with 1 wall change
#2d arrays are array[row][column]
cur_min = None
nxt_val = None
## branches [[col, row, wall_built]]
branches = [[0,0,False]] #Initial Branch Seed

##
# @desc: Generates possibles leaf nodes for a branch
# @param: [grid] the maze
# @param: [branch] the branch to be tested
def leaf_gen(grid, branch):
    print("STUB FUNCTION")
##
# @desc: Generates a list of legal test points for leaf generation
# @param: [dims] Maze dimensions [x][y]
# @param: [loc] test location [x][y]
# @return: [moves] this will be where the list of legal moves is stored
# @note: Only works with 2d arrays, does not eliminate your previous move
# @note: Moves in the Y direction should be multiplied by negative one unless you want to invert the Y axis
def legal_list(dims, loc):
    #Default Template for valid moves (up, down, left, right], List = [[x,y], ...]
    moves = [[0,1],[0,-1],[-1,0],[1,0]]
    valid_moves = []
    removal_idx = []
    #Filer moves that would put the player out of the maze + and - bounds, place invalid indices in removal idx
    for idx, movement in enumerate(moves):
        #Filter the moves that cause negative array access (look up if there is a method to shortening this)
        if(((loc[0] + movement[0]) < 0) or ((loc[1] + movement[1]) < 0) or ((loc[0] + movement[0]) > dims[0]) or ((loc[1] + movement[1]) > dims[1])):
            removal_idx.append(idx)
    print (removal_idx)
    #Check if when cords are multiplied they are 0 or positive
    print(moves)
    return(moves)

#testing the legal_list
lol = legal_list([4,4],[4,4])
