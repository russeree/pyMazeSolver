
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
    removal_idx = []
    #Filer moves that would put the player out of the maze + and - bounds, place invalid indices in removal idx
    for idx, movement in enumerate(moves):
        #Filter the moves that cause negative array access (look up if there is a method to shortening this)
        if(((loc[0] + movement[0]) < 0) or ((loc[1] + movement[1]) < 0) or ((loc[0] + movement[0]) > dims[0]) or ((loc[1] + movement[1]) > dims[1])):
            removal_idx.append(idx)
    #Now that you have a valid set of elements to remove; delete them from the list from greatest to least as not to affect ordering
    for index in sorted(removal_idx, reverse = True):
        del moves[index]
    #return the list of possible moves
    return(moves)
##
# @desc: Takes a branch and generates valid leafs
# @param: [maze] the maze constant that will queried for leafs
# @param: [branch] branch to be evaluated from sprout leafs
def leaf_gen(maze, branch):
    leafs = legal_list([maze['width'],maze['height']], [branch['x'], branch['y']])
    print(leafs)

##
# @desc: Tests the validity of leaf nodes, in essence, will the leaf result in a path? If yes then make the leaf a new branch
# @param: [movements] a list of possible movements inside of the maze based on bounds
# @param: [previous_branch] The previous branch (vertex) that got you to your current location
# @param: [current_branch] The current branch for leaf analysis
def branch_to_leafs(movements, previous_branch, next_branch):
    print ("STUB FUNCTION")
