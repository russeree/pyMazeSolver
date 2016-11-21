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

# Imports
import copy

def legal_list(dims, loc):
    #Default Template for valid moves (up, down, left, right], List = [[x,y], ...]
    moves = [[0,1],[0,-1],[-1,0],[1,0]]
    removal_idx = []
    #Filer moves that would put the player out of the maze + and - bounds, place invalid indices in removal idx
    for idx, movement in enumerate(moves):
        #Filter the moves that cause negative array access (look up if there is a method to shortening this)
        if(((loc[0] + movement[0]) < 0) or ((loc[1] + movement[1]) < 0) or ((loc[0] + movement[0]) > (dims[0] - 1)) or ((loc[1] + movement[1]) > (dims[1]) - 1)):
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
    #print(legal_moves)
    #overlay these moves onto the maze and list all possible moves
    #!!!FIXME!!! There is a row col addressing swap I do not understand
    for candidate in (legal_moves):
        if(maze['maze'][candidate[1] + branch['y']][candidate[0] + branch['x']] == 1):
            leaf = {'x': candidate[0] + branch['x'], 'y': candidate[1] + branch['y'], 'leafs': [], 'wall_built': branch['wall_built'], 'parent':[branch['y'],branch['x']], 'steps': (branch['steps'] + 1)}
            leafs.append(leaf)
        elif((maze['maze'][candidate[1] + branch['y']][candidate[0] + branch['x']] == 0) and (branch['wall_built'] == False)):
            leaf = {'x': candidate[0] + branch['x'], 'y': candidate[1] + branch['y'], 'leafs': [], 'wall_built': True, 'parent':[branch['y'],branch['x']], 'steps': (branch['steps'] + 1)}
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
# @notes: At this point I have a function to generate valid leafs from a given branch \
# then I have a way to add the leafs as a list element of a branch, once this is complete you have a complete list of the branch and \
# the possible moves that can be taken, from there you can store the branch in the look up table. \
# the goal is to exhaust kill all the leafs of a branch, A leaf can die in one of two ways,
#  - The leaf has beaten the maze
#  - The leaf has no more moves to be consumed [No valid moves on the board, all valid move runs into an existing path, the wall has been built]

##
# @name: collision_check
# @desc: Checks against the lookup table to verify that a path is untraveled, This prevents loops
# @desc: [leaf] the leaf node to be checked
# @desc: [lut] Lookup table of branches
# @return: Returns a boolean
def collision_check(leaf, lut):
    #If the lookup for the next position is not empty return True for a collision
    #print ("Checking if leaf " + str(leaf) + "Colides with a lut element")
    if(lut[leaf['y']][leaf['x']] != []):
        return True
    else:
        return False
##
# @name: leaf_destruction
# @desc: given a branch with leafs, exhaust all leafs then return to the parent branch
# @param: [leaf] the branch to be evaluated
# @param: [maze] the maze, used for grabbing dimensions to check for a win condition
# @param: [lut] lookup table of branches usedd for collision checking
# @param: [completion_list] a list containing all of the previous winning conditions
def leaf_destruction(branch, maze, lut, completion_list):
    #print("Running leaf destructor on " + str(branch))
    removal_idx = [] #Stores a list of leafs to be killed off
    #Check the bounds of the array to see if there is a maze win condition
    for idx, leaf in enumerate(branch['leafs']):
        #print("Now checking for destruction " + str(leaf))
        if (leaf['y'] == (maze['height'] - 1) and (leaf['x'] == (maze['width'] - 1))):
                #print ("Removed " + str(leaf) + " because of win condition")
                completion_list.append(leaf['steps'])
                removal_idx.append(idx)
        elif collision_check(leaf, lut):
            #print("Removed " + str(leaf) + " because of colision")
            removal_idx.append(idx)
    for index in sorted(removal_idx, reverse = True):
        del branch['leafs'][index]
##
# @name: iterator
# @desc: create and exhaust all branches seeking win conditions
# @param: [seed_branch] The starting branch
# @param: [maze] the maze to be solved for
# @param: [lut] table of completed moves
# @param: [paths] a list of completed path lengths
# @note: Need to map branching to functions
def iterator (seed_branch, maze, lut, paths):
    #Loop terminator
    complete = False
    #Setup the initial seed onto the lut
    cur_pos = [seed_branch['y'], seed_branch['x']] #Current active branch
    grow_leafs(maze, seed_branch)
    #print(seed_branch)
    lut[cur_pos[0]][cur_pos[1]] = seed_branch
    #The initial loop has been created and placed into the lookup tables
    while not complete:
        #print("Iterator Debugging")
        #print("Current Position before evaluation " + str(cur_pos))
        #print("Look up table before evaluation")
        #for each in lut:
            #print(each)
        #print("-----------------")
        if not lut[cur_pos[0]][cur_pos[1]]['leafs']:
            #print("Taking a step back becuase there are no leafs")
            nxt_pos = lut[cur_pos[0]][cur_pos[1]]['parent']
            lut[cur_pos[0]][cur_pos[1]] = []
            del lut[nxt_pos[0]][nxt_pos[1]]['leafs'][0]
            cur_pos = nxt_pos
            #for each in lut:
            #    print(each)
        else:
            # print("moving into a path")
            lut[lut[cur_pos[0]][cur_pos[1]]['leafs'][0]['y']][lut[cur_pos[0]][cur_pos[1]]['leafs'][0]['x']] = lut[cur_pos[0]][cur_pos[1]]['leafs'][0]
            tmp_pos = copy.copy(cur_pos)
            cur_pos[0] = lut[tmp_pos[0]][tmp_pos[1]]['leafs'][0]['y']
            cur_pos[1] = lut[tmp_pos[0]][tmp_pos[1]]['leafs'][0]['x']
            grow_leafs(maze, lut[cur_pos[0]][cur_pos[1]])
            leaf_destruction(lut[cur_pos[0]][cur_pos[1]], maze, lut, paths)
            #print (cur_pos)
            #for each in lut:
                #print (each)
        if not lut[0][0]['leafs']:
            #print(lut[0][0]['leafs'])
            complete = True
        #print(" ")
    print("Completed")
    print(paths)
