import numpy as np
import invkinematics as kine
import matplotlib.pyplot as plt

def get_torquelist(l):
    F = [0,20]
    taus = []
    for i in range(len(l)-1):
        t0,t1,l0,l1 = kine.calc_theta(l[i])
        J = kine.calc_jacovianMatrix(t0,t1,l0,l1)
        dt0,dt1 = kine.calc_deltheta(l[i],l[i+1])
        tau = kine.calc_torque(F,J)
        taus.append(tau)
    return taus
        

if __name__=="__main__":
    l = np.load("good.npy")
    taus = get_torquelist(l)
    tau = [x[0] for x in taus]
    l2 = np.load("bad2.npy")
    taus2 = get_torquelist(l2)
    tau2 = [x[0] for x in taus2]


    fig = plt.figure()
    fig.suptitle("touque")

    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)

    ax1.plot(range(len(tau)), tau)
    ax1.set_ylim(-5000,5000)
    ax2.plot(range(len(tau2)), tau2)
    ax2.set_ylim(-5000,5000)

    plt.show()
