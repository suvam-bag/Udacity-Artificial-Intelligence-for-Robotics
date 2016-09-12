#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import rospy 
#import roslib  
import time  
import cv2
import os
import numpy as np
import math
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#import random
#import pylab
#from std_msgs.msg import String
#from geometry_msgs.msg import Twist
#from geometry_msgs.msg import Vector3
#from tf2_msgs.msg import TFMessage
#from sensor_msgs.msg import PointCloud2
#from sensor_msgs.msg import Image
#from image_converter import ToOpenCV
#from cv_bridge import CvBridge, CvBridgeError
#from nav_msgs.msg import Odometry
#from tf2_msgs import TFMessage  #this is for tf_static


#init is declared global because it will get updated after every iteration
init = [0, 0, 0]   #[row,col,direction]
                   #direction = 0: up
                   #1: left
                   #2: down
                   #3: right

class hello(object):
    #not needed.....the init...instead pass goal as argument in GET
    #def __init__(self, goal):
        #this variable should be received from Sam's voice input
    #    self.goal = goal

    def GET(self, goal):

        #-----------
        #User Instructions
        #
        #Implement the function leftTurnPolicy below
        #
        #You are given a car in grid with initial state init. Your task is to compute and return the car's optimal path to #the position specified in the goal;
        #the costs for each motion are as defined in cost.
        #
        #There are four motion directions: up, left, down and right
        #Increasing the index in this array corresponds to making a left turn, and decreasing the index corresponds to 
        #making a right turn.

        forward = [[-1,  0],   #go up
                   [ 0, -1],   #go left
                   [ 1,  0],   #go down
                   [ 0,  1]]   #go right

        forward_name = ['up',  'left',  'down',  'right' ]
        #delta_name = ['^','<','v','>']

        #action has 3 values: right turn, no turn, left turn
        action = [-1, 0, 1]
        action_name = ['R', 'F', 'L']

        #cost value
        cost = [2, 1, 1]

        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        print (np.asarray(grid))
        #init = [0, 0, 0]   #[row,col,direction]
                           #direction = 0: up
                           #1: left
                           #2: down
                           #3: right
        #self.init = init
        #init = [5, 0, 0]
        
        
        initx = init[0]
        inity = init[1]
        print ('current init position is', init)
        
        
        #take items from user from prompt and create the goal positions 
        #goal = self.goal
        #goal = [len(grid)-4, len(grid[0])-10]
        #goal = [len(grid)-5, len(grid[0])-8]
        #goal = [len(grid)-2, len(grid[0])-4]
        #goal = [len(grid)-1, len(grid[0])-2]
        #goal = [len(grid)-7, len(grid[0])-8]
        #goal = [len(grid)-10, len(grid[0])-10]
        #goal = [len(grid)-5, len(grid[0])-3]
        #goal = [len(grid)-1, len(grid[0])-3]
        #goal = [len(grid)-3, len(grid[0])-7]
        #goal = [len(grid)-12, len(grid[0])-2]
        print ('current goal position is', goal)
       
    

    #def optimum_policy2D(self):
        #Initialize an empty return grid and a 3D best-value matrix
        policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
        bestvalue = [[[999 for o in range(len(forward))] for y in range(len(grid[0]))] for x in range(len(grid))]

        goalx = goal[0]
        goaly = goal[1]


        #Initialize the frontier with the starting state 
        #We'll keep a running path for how we got to each state in the frontier, so 
        #when we reach the goal we can just play back the actions to make the grid
        #Our heuristic is "manhattan distance" - non-diagonal distance if  no obstacles.

        x = init[0]
        y = init[1]
        o = init[2]
        path = []
        g = 0
        h = abs(x - goalx) + abs(y - goaly)
        f = g + h

        frontier = []
        frontier.append([f, g, x, y, o, path])
        bestvalue[x][y][o] = g

        #Run the A-Star algorithm
        while(len(frontier) > 0):
            frontier.sort()
            # print "frontier:", frontier

            current = frontier.pop(0)
            g = current[1]
            x = current[2]
            y = current[3]
            o = current[4]
            path = current[5]

            if x == goalx and y == goaly:
                frontier = []

            else: 
                # print "take:", current
                for a in range(len(action)):
                    o2 = (o + action[a]) % len(forward)
                    x2 = x + forward[o2][0]
                    y2 = y + forward[o2][1]
                    g2 = g + cost[a]
                
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                    #If this is the cheapest way we have found to get to the next state, add it to the frontier

                        if g2 < bestvalue[x2][y2][o2]:
                            h2 = abs(x2 - goalx) + abs(y2 - goaly)
                            f2 = g2 + h2
                            path2 = list(path)
                            path2.append(a)
                            nxt = [f2, g2, x2, y2, o2, path2]
                            # print "add:", nxt
                            frontier.append(nxt)
                            bestvalue[x2][y2][o2] = g2

        #Now chart the path in the policy grid so we can return it
        x = init[0]
        y = init[1]
        o = init[2]

        ####---------------------------------------------------------------------#########
        #these initial conditions might be needed to solve the initial direction of the robot (past problem faced in amigobot)
        
        #pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,6)))
        #time.sleep(3.7)
        #pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,-6)))
        #time.sleep(0.4)

        ####---------------------------------------------------------------------#########

        for i in range(len(path)):
            a = path[i]
            policy2D[x][y] = action_name[a]
            o = (o + action[a]) % len(forward)
            x += forward[o][0]
            y += forward[o][1]              
            #turn left
            if action_name[a] == action_name[2]:
                pass
                #print action_name[a]
                #pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,6)))                   
                #time.sleep(2)
                #pub.publish(Twist(Vector3(0.3,0,0),Vector3(0,0,0)))
                #time.sleep(1)           
            #go forward
            elif action_name[a] == action_name[1]:
                pass
                #print action_name[a]
                #pub.publish(Twist(Vector3(0.3,0,0),Vector3(0,0,0)))
                #time.sleep(1)
            #turn right                 
            else:
                pass
                #print action_name[a]
                #pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,-6)))
                #time.sleep(2)
                #pub.publish(Twist(Vector3(0.3,0,0),Vector3(0,0,0)))
                #time.sleep(1)
        
        #the '*' and 'D' should always match, if not then the goal must be blocked by some obstacle
        policy2D[x][y] =  '*'  

        #optimum_policy2D()
        #pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,0)))   
        #for i in range(len(policy2D)):
        #    print policy2D[i]
        policy2D[initx][inity] = '$'
        policy2D[goalx][goaly] = 'D'
        print np.asarray(policy2D)

        init[0] = goal[0]
        init[1] = goal[1]
        init[2] = 0
        print ('updated init position is', init)
           
            
        #rospy.spin()
 
            
        
        

def main():
    Hello = hello()
    for i in xrange(0,2):
        Hello.GET([4 + 2*i, 7 + 6*i])
   

if __name__ == "__main__":
    main()
       
       
     




























