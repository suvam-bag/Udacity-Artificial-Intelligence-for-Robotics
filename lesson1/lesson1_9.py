#import collections
#collections.deque()
p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def move(p, U=0):    
    return [p[i-U] for i in range(len(p))]
    #or for i in range(len(p)):
     #      q.append(p[(i-U)%len(p)]) # watch the % operator use
     #      return q

print move(p,1)
