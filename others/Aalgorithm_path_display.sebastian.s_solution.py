# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search():
    # ----------------------------------------
    # insert code here
    #define a list of same size as the grid and 
    #it can have only two values 0 or 1 like a flag.....1 means checked i.e - that cell 
    closed = [[0 for row in range(len(grid[0]))]for col in range(len(grid[0]))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for row in range(len(grid[0]))]for col in range(len(grid[0]))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid[0]))]

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False #flag that is set when search is complete
    resign = False #flag set if we can't find the expand
    count = 0
    
    while found is False and resign is False:
    #if my open list is empty and there's nothing to expand, then resign is true and print fail
        if len(open) == 0:
            resign = True
            #print 'fail'  
            expand == -1     

        else:
            open.sort() #sorts elements starting from smallest g_value
            open.reverse() #reverse the list
            next = open.pop() #pop the smallest g_value element...pop pops at the end so just reverse the list
            x = next[1]
            y = next[2]
            g = next[0] 

            expand[x][y] = count
            count += 1

            if x == goal[0] and y == goal[1]:
                found = True
                #print next
                
            #main logic
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0: #not yet checked and grid cell is navigable
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1 # this step is the recursion
                            action[x2][y2] = i
                            
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid[0]))]
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'
    while x != init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        policy[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2

    for i in range(len(policy)):
        print policy[i]

search()
    # ----------------------------------------

    
