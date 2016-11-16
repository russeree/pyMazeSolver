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
def legal_list(dims, loc):
    moves = []
    removal_idx = []
    #Generate a list of all possible moves
    for y in range (-1,2):
        for x in range (-1,2):
            moves.append([(loc[0] + x),(loc[0] + y)])
    #Remove the current location from the array
    moves.remove([0,0])
    #Check if when cords are multiplied they are 0 or positive
    for idx, loc in enumerate(moves):
        if((loc[0] < 0) or (loc[1] < 0)):
            removal_idx.append(idx)
            print("Need to remove " + str(loc))
    for remove_element in (removal_idx):
        moves[remove_element] = [0,0]
    #!!FIXME!! Make a filter that works
    filter(lambda a: a != [0,0], moves)
    print(moves)
    return(moves)

lol = legal_list([4,4],[0,0])
