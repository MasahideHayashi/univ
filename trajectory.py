import numpy as np
import matplotlib.pyplot as plt
import invkinematics as kine
import math
import relativephase as rel
import torque as trq
import cv2

# fa(x) = -355(x-0.15)^2 + 8x
# fb(x) = -49(x-0.65)^2 + 6x
def Fa(x):
  return -355/3*(x-0.15)**3 + 8*x
def Fb(x):
  return -49/3*(x-0.65)**3 + 6*x

if __name__ == "__main__":
  good_upreps = np.load('divdata/good_upreps.npy', allow_pickle=True)
  good_downreps = np.load('divdata/good_downreps.npy', allow_pickle=True)

# 肩の軌道　移動距離の確認
  # for rep in good_upreps:
  #   diff = []
  #   for i in range(len(rep)-1):
  #     diff.append(math.sqrt((rep[i+1][5][0]-rep[i][5][0])**2 + (rep[i+1][5][1]-rep[i][5][1])**2))
  #   plt.bar(range(len(diff)), diff)
  #   plt.show()
  # for rep in good_upreps:
  #   # print(rep[0][5], rep[-1][5])
  #   print(math.sqrt((rep[-1][5][0]-rep[0][5][0])**2 + (rep[-1][5][1]-rep[0][5][1])**2))

# 肘と肩の角度のグラフ表示
  # for index in range(len(good_upreps)):
  #   elbow_angles = []
  #   shoulder_angles = []
  #   for i in range(len(good_upreps[index])):
  #     theta0,theta1,_,_ = kine.calc_theta(good_upreps[index][i])
  #     shoulder_angles.append(np.rad2deg(math.pi/2 - theta0))
  #     elbow_angles.append(np.rad2deg(np.pi - theta1))
  #   print(shoulder_angles)
  #   print(elbow_angles)
  #   plt.plot(shoulder_angles, elbow_angles)
  #   plt.show()


# 肩の軌道計算
  shoulder_start = good_upreps[0][0][5]
  shoulder_end = good_upreps[0][-1][5]
  dx = shoulder_end[0]-shoulder_start[0]
  dy = shoulder_end[1]-shoulder_start[1]
  shoulderlist = []
  splitnum = 50
  splitlist = [] # 各区間ごとの肩の移動距離リスト
  # 動作前半（30%まで）はFa、後半はFbで軌道を近似し、各区間の移動距離を計算
  for i in range(1,int(splitnum*0.3)+1):
    splitlist.append((Fa(i/splitnum)-Fa((i-1)/splitnum))/4.4)
  for i in range(int(splitnum*0.3)+1, splitnum+1):
    splitlist.append((Fb(i/splitnum)-Fb((i-1)/splitnum))/4.4)
  # print(len(splitlist))
  # print(sum(splitlist)) #ほぼ1.0
  for i in range(splitnum+1):
    shoulderlist.append([shoulder_start[0]+dx*sum(splitlist[:i]), shoulder_start[1]+dy*sum(splitlist[:i])])

# 肩の軌道表示
  # cap = cv2.VideoCapture("video/good/0.mp4")
  # for _ in range(350):
  #   cap.read()
  # ret, frame = cap.read()
  # for i in range(len(shoulderlist)):
  #   cv2.circle(frame, (int(shoulderlist[i][0]), int(shoulderlist[i][1])), 3, (0,0,255), -1)
  # cv2.imshow("frame", frame)
  # cv2.waitKey(0)
  # for _ in range(50):
  #   cap.read()
  # ret, frame = cap.read()
  # for i in range(len(shoulderlist)):
  #   cv2.circle(frame, (int(shoulderlist[i][0]), int(shoulderlist[i][1])), 3, (0,0,255), -1)
  # cv2.imshow("frame", frame)
  # cv2.waitKey(0)
  # while True:
  #   ret, frame = cap.read()
  #   if not ret:
  #     break
  #   for i in range(len(shoulderlist)):
  #     cv2.circle(frame, (int(shoulderlist[i][0]), int(shoulderlist[i][1])), 3, (0,0,255), -1)
  #   cv2.imshow("frame", frame)
  #   if cv2.waitKey(1) & 0xFF == ord('q'):
  #     break

# 肘の軌道表示
  l0 = math.sqrt((good_upreps[0][-1][5][0]-good_upreps[0][-1][7][0])**2 + (good_upreps[0][-1][5][1]-good_upreps[0][-1][7][1])**2)
  l1 = math.sqrt((good_upreps[0][-1][7][0]-good_upreps[0][-1][9][0])**2 + (good_upreps[0][-1][7][1]-good_upreps[0][-1][9][1])**2)
  print("l0, l1:", l0, l1)
  shoulderangle_start, elbowangle_start, _, _ = kine.calc_theta(good_upreps[0][0])
  shoulderangle_end, elbowangle_end, _, _ = kine.calc_theta(good_upreps[0][-1])
  print(np.rad2deg(shoulderangle_start), np.rad2deg(elbowangle_start))
  elbowlist = []
  for i in range(len(shoulderlist)):
    theta0 = shoulderangle_start + (shoulderangle_end - shoulderangle_start)*i/splitnum
    theta1 = elbowangle_start + (elbowangle_end - elbowangle_start)*i/splitnum
    elbowx = shoulderlist[i][0] + l0*math.cos(theta0)
    elbowy = shoulderlist[i][1] + l0*math.sin(theta0)
    elbowlist.append([elbowx, elbowy])
  wristlist = []
  for i in range(len(shoulderlist)):
    theta0 = shoulderangle_start + (shoulderangle_end - shoulderangle_start)*i/splitnum
    theta1 = elbowangle_start + (elbowangle_end - elbowangle_start)*i/splitnum
    wristx = shoulderlist[i][0] + l0*math.cos(theta0) + l1*math.cos(theta0+theta1)
    wristy = shoulderlist[i][1] + l0*math.sin(theta0) + l1*math.sin(theta0+theta1)
    wristlist.append([wristx, wristy])
  
  cap = cv2.VideoCapture("video/good/0.mp4")
  for _ in range(350):
    cap.read()
  ret, frame = cap.read()
  for i in range(len(elbowlist)):
    cv2.circle(frame, (int(shoulderlist[i][0]), int(shoulderlist[i][1])), 3, (0,255,0), -1)
    cv2.circle(frame, (int(elbowlist[i][0]), int(elbowlist[i][1])), 3, (0,0,255), -1)
    cv2.circle(frame, (int(wristlist[i][0]), int(wristlist[i][1])), 3, (255,0,0), -1)
  cv2.imshow("frame", frame)
  cv2.waitKey(0)
  for _ in range(50):
    cap.read()
  ret, frame = cap.read()
  for i in range(len(elbowlist)):
    cv2.circle(frame, (int(shoulderlist[i][0]), int(shoulderlist[i][1])), 3, (0,255,0), -1)
    cv2.circle(frame, (int(elbowlist[i][0]), int(elbowlist[i][1])), 3, (0,0,255), -1)
    cv2.circle(frame, (int(wristlist[i][0]), int(wristlist[i][1])), 3, (255,0,0), -1)
  cv2.imshow("frame", frame)
  cv2.waitKey(0)