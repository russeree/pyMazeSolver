##
# @auth: Reese Russell
# @desc: Python Maze Solver Functions

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
    leafs = [] #Store the leafs
    #legal positions for a leaf to grow
    legal_moves = legal_list([maze['width'],maze['height']], [branch['x'], branch['y']])
    #overlay these moves onto the maze and list all possible moves
    #!!!FIXME!!! There is a row col addressing swap I do not understand
    for candidate in (legal_moves):
        if(maze['maze'][candidate[0]][candidate[1]] == 1):
            leaf = {'x': candidate[1], 'y': candidate[0], 'leafs': [], 'wall_built': branch['wall_built'], 'parent': branch['id'], 'best_child': None, 'id': (branch['id'] + 1)}
            leafs.append(leaf)
        elif((maze['maze'][candidate[0]][candidate[1]] == 0) and (branch['wall_built'] == False)):
            leaf = {'x': candidate[1], 'y': candidate[0], 'leafs': [], 'wall_built': True, 'parent': branch['id'], 'best_child': None, 'id': (branch['id'] + 1)}
            leafs.append(leaf)
    return leafs
##
# @desc: Takes a list of leaves and returns a branch
# @param: [branch] Takes in a branch and generates a list of leafs
# @param: [maze] list as a maze
# @return: Returns a branch with a list of leafs
def grow_leafs(maze, branch):
    #places leafs in in the current branch for evaluation
    branch['leafs'] = leaf_gen(maze, branch)
##
# @desc: Iterates through a branches leafs and determines if there is death, growth, or end condition
# @param:[seed_branch] takes in the branch to be evaluated
# @param:[maze] takes in the maze to be solved
def solve_maze(maze, seed_branch):
    #Stores a list of branches that reached position [[y - 1],[x -1]]
    path_lengths = []``
    #Pruning index this is a list of leaves that need to removed from the current branch because they produce no seeds
    pruning_idx = []
    #For each leaf in the current branch check to see if it was able to grow leaves so it can become of branch or one of the leafs was the win condition
    for idx, leaf in enumerate(current_branch['leafs']):
        # Grow the leafs on the branch
        grow_leafs(maze, leaf)
        if (not leaf['leafs']): #If no leafs grow the branch has died
            pruning_idx.append[idx]
        elif (leaf['id'] > (maze['height'] * maze['width'])): #If the branch has exceeded to moves in the maze the branch has died
            pruning_idx.append[idx]
        elif (leaf['y'] == (maze['height'] - 1)): #If the leaf exists on lower wall of the maze check the x cordinate
            if(leaf['x'] == (maze['width'] - 1)): #If the leaf is on the outer edge too record the number of branches
                pruning_idx.append(leaf['id'])
    #prune the dead leafs and turn the new ones into branchs
    for index in sorted(pruning_idx, reverse = True):
        del current_branch['leafs'][index]

