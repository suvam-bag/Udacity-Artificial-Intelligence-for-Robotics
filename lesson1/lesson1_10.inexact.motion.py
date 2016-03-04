#Modify the move function to accommodate the added 
#probabilities of overshooting or undershooting 
#the intended destination.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1
q = []
q1 = []
q2 = []

def sense(p, Z):
    #q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    #q = []
    for i in range(len(p)):
        #q.append((p[((i-U)-1)%len(p)])*pUndershoot)
        #q.append((p[((i-U)+1)%len(p)])*pOvershoot)
        q.append((p[(i-U)%len(p)])*pExact)
    return q



def moveUndershoot(p, U):
    #q1 = []
    for i in range(len(p)):
        #q.append((p[((i+1)-U)%len(p)])*0.1)
        #q.append((p[((i-1)-U)%len(p)])*0.1)
        q1.append((p[(i-U)%len(p)])*pUndershoot)
    return q1

def moveOvershoot(p, U):
    #q2 = []
    for i in range(len(p)):
        #q.append((p[((i+1)-U)%len(p)])*0.1)
        #q.append((p[((i-1)-U)%len(p)])*0.1)
        q2.append((p[(i-U)%len(p)])*pOvershoot)
    return q2

move(p, 1)
moveUndershoot(p, 0)
moveOvershoot(p, 2)
zipped_list = zip(q,q1, q2)
print [sum(item) for item in zipped_list]

