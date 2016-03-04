# The function localize takes the following arguments:
#
# colors:       a 2D list, each entry either 'R' (for a red cell) or 'G' (for a green cell)
#
# measurements: a list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:      a list of actions taken by the robot, each entry of the form [dy,dx], where
#               dx refers to the change in the x-direction (positive meaning movement to the right)
#               and dy refers to the change in the y-direction (positive meaning movement downward)
#               NOTE: the *first* coordinate is change in y; the *second* coordinate is change in x
#
# sensor_right: a float between 0 and 1, giving the probability that any given measurement is
#               correct; the probability that the measurement is incorrect is 1-sensor_right
#
# p_move:       a float between 0 and 1, giving the probability that any given movement command takes
#               place; the probability that the movement command fails (and the robot remains still);
#               the robot will NOT overshoot its destination in this exercise
#
# The function should RETURN (not just show) a 2D list (of the same dimensions as colors) that 
# gives the probabilities that the robot occupies each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform probability of being 
# in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.

colors = [['red', 'green', 'green', 'red' , 'red'],
      ['red', 'red', 'green', 'red', 'red'],
      ['red', 'red', 'green', 'green', 'red'],
      ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7
p_move = 0.8



#p = []
#x = len(colors) 
#y = len(colors[0])
#n = x*y


#for i in range(x):
#    p.append([])
#    for j in range(y):
#         p[i].append(1/float(n))

# >>> Insert your code here <<<         
def sense(p, Z):
    q = [[0.0 for row in range(len(p[0]))]for col in range(len(p))]
    s = 0.0
    for i in range(len(colors)):
        for j in range(len(colors[0])):
            hit = (Z == colors[i][j]) 
            q[i][j] = (p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
            s += q[i][j]
    for i in range(len(colors)):
         for j in range(len(colors[0])):
             q[i][j] = q[i][j]/s
    return q

def move(p,U):
    q = [[0.0 for row in range(len(p[0]))]for col in range(len(p))]
    for i in range(len(colors)):
        for j in range(len(colors[0])):
            q[i][j] = ( p[(i-U[0])%len(colors)][(j-U[1])%len(colors[0])]*p_move + p[i][j]*(1-p_move) )
    return q

def show(p):
    for i in range(len(p)):
        print p[i]
        


#############################################################
# For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

# initializes p to a uniform distribution over a grid of the same dimensions as colors

if len(measurements) != len(motions):
    raise ValueError, "error in size of measurement/motion vector"

pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
         
for j in xrange(len(measurements)):
    p = move(p,motions[j])
    p = sense(p, measurements[j])
    

show(p) # displays your answer
