import numpy as np
import matplotlib.pyplot as plt
import invkinematics as kine
import math
import velocity as vel

# 肘の角度とその角速度のリストを取得
def getanglevelocitylist(l):
    elb = []
    for i in range(len(l)):
        theta0,theta1,_,_ = kine.calc_theta(l[i])
        elb.append(np.rad2deg(np.pi-theta1))
    velocitylist = np.gradient(elb, 1/30)
    return elb, velocitylist


if __name__ == "__main__":
  good_upreps = np.load('divdata/good_upreps.npy', allow_pickle=True)
  good_downreps = np.load('divdata/good_downreps.npy', allow_pickle=True)
  print(good_upreps.shape)

  # for i in range(len(good_upreps)):
  #   elb_angle, velocitylist = getanglevelocitylist(good_upreps[i])
  #   elb_angle2, velocitylist2 = getanglevelocitylist(good_downreps[i])
  #   plt.plot(elb_angle, velocitylist)
  #   plt.plot(elb_angle2, velocitylist2)
  #   plt.xlabel("elbow angle")
  #   plt.ylabel("elbow angle velocity")
  #   plt.title("good uprep "+str(i))
  #   plt.show()
  
  bad0_upreps = np.load('divdata/bad3_upreps.npy', allow_pickle=True)
  bad0_downreps = np.load('divdata/bad3_downreps.npy', allow_pickle=True)

  for i in range(len(bad0_upreps)):
    elb_angle, velocitylist = getanglevelocitylist(bad0_upreps[i])
    elb_angle2, velocitylist2 = getanglevelocitylist(bad0_downreps[i])
    plt.plot(elb_angle, velocitylist)
    plt.plot(elb_angle2, velocitylist2)
    plt.xlabel("elbow angle")
    plt.ylabel("elbow angle velocity")
    plt.title("bad0 uprep "+str(i))
    plt.show()
