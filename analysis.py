import numpy as np
import matplotlib.pyplot as plt
import invkinematics as kine
import math
import relativephase as rel
import torque as trq

if __name__ == "__main__":
  good_upreps = np.load('divdata/good_upreps.npy', allow_pickle=True)
  good_downreps = np.load('divdata/good_downreps.npy', allow_pickle=True)
  print(good_upreps.shape)
  print(type(good_upreps[0]))
  # 相対位相
  # for i in range(len(good_upreps)):
  #   rel_phase = rel.get_rellist(good_upreps[i])
  #   rel_phase2 = rel.get_rellist(good_downreps[i])
  #   plt.plot(range(len(rel_phase)), rel_phase)
  #   plt.plot(range(len(rel_phase2)), rel_phase2)
  #   plt.title("good uprep "+str(i))
  #   plt.xlabel("time (frame) ")
  #   plt.ylabel("relative phase")
  #   plt.show() 

  bad0_upreps = np.load('divdata/bad1_upreps.npy', allow_pickle=True)
  bad0_downreps = np.load('divdata/bad1_downreps.npy', allow_pickle=True)

  # for i in range(len(bad0_upreps)):
  #   rel_phase = rel.get_rellist(bad0_upreps[i])
  #   rel_phase2 = rel.get_rellist(bad0_downreps[i])
  #   plt.plot(range(len(rel_phase)), rel_phase)
  #   plt.plot(range(len(rel_phase2)), rel_phase2)
  #   plt.title("bad0 uprep "+str(i))
  #   plt.xlabel("time (frame) ")
  #   plt.ylabel("relative phase")
  #   plt.show()
  
  # uprep,downrep確認用
  # for i in range(len(good_upreps)):
  #   good5_x = []
  #   good7_x = []
  #   good9_x = []
  #   good5_y = []
  #   good7_y = []
  #   good9_y = []
  #   for j in range(len(good_upreps[i])):
  #     good5_x.append(good_upreps[i][j][5][0])
  #     good5_y.append(good_upreps[i][j][5][1])
  #     good7_x.append(good_upreps[i][j][7][0])
  #     good7_y.append(good_upreps[i][j][7][1])
  #     good9_x.append(good_upreps[i][j][9][0])
  #     good9_y.append(good_upreps[i][j][9][1])
  #   plt.plot(good5_x, good5_y, label="5")
  #   plt.plot(good7_x, good7_y, label="7")
  #   plt.plot(good9_x, good9_y, label="9")
  #   plt.title("good uprep hand trajectory")
  #   plt.xlabel("x")
  #   plt.ylabel("y")
  #   plt.legend()
  #   plt.axis("equal")
  #   plt.show()
  #   plt.close()



# トルク
# for i in range(len(good_upreps)):
#   taus = trq.get_torquelist(good_upreps[i])
#   print(taus)
#   shoulder_torque = [tau[0] for tau in taus]
#   elbow_torque = [tau[1] for tau in taus]
#   plt.plot(range(len(shoulder_torque)), shoulder_torque, label="shoulder")
#   # plt.show()
#   plt.plot(range(len(elbow_torque)), elbow_torque, label="elbow")
#   plt.title("good uprep torque"+str(i))
#   plt.legend()
#   plt.show()
#   plt.close()

# for i in range(len(good_downreps)):
#   taus = trq.get_torquelist(good_downreps[i])
#   print(taus)
#   shoulder_torque = [tau[0] for tau in taus]
#   elbow_torque = [tau[1] for tau in taus]
#   plt.plot(range(len(shoulder_torque)), shoulder_torque, label="shoulder")
#   # plt.show()
#   plt.plot(range(len(elbow_torque)), elbow_torque, label="elbow")
#   plt.title("good uprep torque"+str(i))
#   plt.legend()
#   plt.show()
#   plt.close()

# for i in range(len(bad0_upreps)):
#   taus = trq.get_torquelist(bad0_upreps[i])
#   print(taus)
#   shoulder_torque = [tau[0] for tau in taus]
#   elbow_torque = [tau[1] for tau in taus]
#   plt.plot(range(len(shoulder_torque)), shoulder_torque, label="shoulder")
#   # plt.show()
#   plt.plot(range(len(elbow_torque)), elbow_torque, label="elbow")
#   plt.title("good uprep torque"+str(i))
#   plt.legend()
#   plt.show()
#   plt.close()

# for i in range(len(bad0_downreps)):
#   taus = trq.get_torquelist(bad0_downreps[i])
#   print(taus)
#   shoulder_torque = [tau[0] for tau in taus]
#   elbow_torque = [tau[1] for tau in taus]
#   plt.plot(range(len(shoulder_torque)), shoulder_torque, label="shoulder")
#   # plt.show()
#   plt.plot(range(len(elbow_torque)), elbow_torque, label="elbow")
#   plt.title("good uprep torque"+str(i))
#   plt.legend()
#   plt.show()
#   plt.close()


# 上半身の角度の閾値
for rep in good_upreps:
  # shoulder = rep[0][5]
  # hip = rep[0][11]
  # print(math.degrees(math.atan2(shoulder[1]-hip[1], -shoulder[0]+hip[0])))
  shoulder = rep[-1][5]
  hip = rep[-1][11]
  print(math.degrees(math.atan2(shoulder[1]-hip[1], -shoulder[0]+hip[0])))