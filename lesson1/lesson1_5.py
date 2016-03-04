p = [0.2,0.2,0.2,0.2,0.2]
world = ['green','red','red','green','green']
pHit = 0.6
pMiss = 0.2
Z = 'green'
q = [[]] * len(world)

def sense(p,Z):
    for i in xrange(len(world)):
        if world[i] != Z:
            q[i] = float(p[i]*0.6)
        else:
            q[i] = float(p[i]*0.2)
    s = sum (q)
    for j in xrange(len(q)):
        q[j] = q[j]/s
    return q


print sense(p,Z)
