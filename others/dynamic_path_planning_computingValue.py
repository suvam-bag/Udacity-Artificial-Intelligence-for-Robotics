# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    init = [0,0]

    closed = [[0 for row in range(len(grid[0]))]for col in range(len(grid[0]))]
    closed[goal[0]][goal[1]] = 1
    
    expand = [[-99 for row in range(len(grid[0]))]for col in range(len(grid[0]))]
    expand[goal[0]][goal[1]] = 0

    x = goal[0]
    y = goal[1]
    g = 0

    open = [[g, x, y]]

    found = False
    resign = False
    count = 0
           
    while found is False and resign is False:
        if len(open) == 0:
           resign = True
           expand == -1

        else:
           open.sort()
           open.reverse()
           next = open.pop()

           x = next[1]
           
           y = next[2]
           
           g = next[0]

           expand[x][y] = count
           count += 1

           if x == init[0] and y == init[1]:
               found = True

           else:
               for i in range(len(delta)):
                   x2 = x - delta[i][0]
                   y2 = y - delta[i][1]
                   if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                       if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                           g2 = g + cost
                           open.append([g2, x2, y2])
                           closed[x2][y2] = 1

    for i in range(len(expand)):
        print expand[i]
           
    

    
compute_value(grid, goal, cost)
    # ----------------------------------------
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
  
