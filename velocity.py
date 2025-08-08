import numpy as np
import invkinematics as kine
import matplotlib.pyplot as plt
import math

def get_velocitylist(l):
    F = [0,20]
    rs = []
    for i in range(len(l)-1):
        t0,t1,l0,l1 = kine.calc_theta(l[i])
        J = kine.calc_jacovianMatrix(t0,t1,l0,l1)
        dt0,dt1 = kine.calc_deltheta(l[i],l[i+1])
        r = kine.calc_velocity(J,dt0,dt1)
        rs.append(r)
    return rs
        

l = np.load("good.npy")
rs = get_velocitylist(l)
r = [math.sqrt(pow(x[0]+x[1],2)) for x in rs]
l2 = np.load("bad.npy")
rs2 = get_velocitylist(l2)
r2 = [math.sqrt(pow(x[0]+x[1],2)) for x in rs2]


fig = plt.figure()
fig.suptitle("velocity")

ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(range(len(r)), r)
ax1.set_ylim(0,20)
ax2.plot(range(len(r2)), r2)
ax2.set_ylim(0,20)

plt.show()
