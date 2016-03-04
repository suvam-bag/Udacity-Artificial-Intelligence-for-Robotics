p = [0.2,0.2,0.2,0.2,0.2]
world = ['green','red','red','green','green']
pHit = 0.6
pMiss = 0.2
measurements = ['red','green']


def sense(p,measurements):
    q = [[]] * len(world)
    for t in range(len(measurements)):
        for i in xrange(len(world)):
            if world[i] == measurements[t]:
                q[i] = float(p[i]*0.6)
            else:
                q[i] = float(p[i]*0.2)
        s = sum (q)
        for j in xrange(len(q)):
            q[j] = q[j]/s
    
    return q


print sense(p,measurements)
