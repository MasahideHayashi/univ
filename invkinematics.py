import numpy as np
import math

def calc_theta(a):
    l0 = math.sqrt(pow(a[5][0]-a[7][0],2)+pow(a[5][1]-a[7][1],2))
    l1 = math.sqrt(pow(a[9][0]-a[7][0],2)+pow(a[9][1]-a[7][1],2))
    x = a[9][0] - a[5][0]
    y = a[9][1] - a[5][1]
    alpha = math.acos((-(x*x+y*y)+l0*l0+l1*l1)/(2*l0*l1))
    theta1 = math.pi - alpha
    theta0 = math.atan2(y,x)-math.atan2((l1*math.sin(theta1)),(l0+l1*math.cos(theta1)))
    return theta0,theta1,l0,l1

def calc_jacovianMatrix(t0,t1,l0,l1):
    delx0 = -l0*math.sin(t0)-l1*math.sin(t0+t1)
    delx1 = -l1*math.sin(t0+t1)
    dely0 = l0*math.cos(t0)+l1*math.cos(t0+t1)
    dely1 = l1*math.cos(t0+t1)

    return [[delx0,dely0],[delx1,dely1]]

def calc_deltheta(a,b):
    a0,a1,_,_ = calc_theta(a)
    b0,b1,_,_ = calc_theta(b)
    return b0-a0, b1-a1

def calc_velocity(J,d0,d1):
    return [J[0][0]*d0+J[1][0]*d1,
            J[0][1]*d0+J[1][1]*d1]
    
def calc_torque(F,J):
    return [J[0][0]*F[0]+J[0][1]*F[1],
            J[1][0]*F[0]+J[1][1]*F[1]]

if __name__=="__main__":
    l = np.load("good.npy")
    
    for i in range(len(l)-1):
        theta0,theta1,l0,l1 = calc_theta(l[i])
        J = calc_jacovianMatrix(theta0,theta1,l0,l1)
        deltheta0,deltheta1 = calc_deltheta(l[i],l[i+1])
        r = calc_velocity(J,deltheta0,deltheta1)
        F = [0,20]
        tau = calc_torque(F,J)
        print(tau)
