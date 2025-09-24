import numpy as np
import matplotlib.pyplot as plt
import math
import json


def divupdown(l,L,R):
  l = l[L:R]
  maxh = 10000
  minh = 0
  for i in range(len(l)):
    if maxh>l[i][7][1]:
        maxh = l[i][7][1]
    if minh<l[i][7][1]:
        minh = l[i][7][1]
  print("maxh:", maxh)
  print("minh:", minh)

  pl = []
  for i in range(len(l)):pl.append(l[i][7][1])
  
  upl = []
  downl = []
  uprep = []
  downrep = []
  up = True 
  down = False
  threshold = 30
  for i in range(len(l)):
    if l[i][7][1]<minh-threshold and l[i][7][1]>maxh+threshold:
      if up : upl.append(l[i].tolist())
      if down : downl.append(l[i].tolist())
      if len(upl)==1: print("index up start", i)
      if len(downl)==1: print("index down start", i)

    if up and l[i][7][1]<maxh+threshold:
      up = False
      down = True
      uprep.append(upl)
      upl = []
      print("index up end:", i)

    if down and l[i][7][1]>minh-threshold:
      up = True
      down = False
      downrep.append(downl)
      downl = []
      print("index down end:", i)

  return uprep,downrep

if __name__=="__main__":
  f = open('../divdata/startend.txt', 'r')
  lines = f.readlines()
  f.close()
  items = []
  for line in lines:
    items.append(line.split())
    print(items)
  file = "../posedata/"
  upl = []
  downl = []
  for i in range(4):
    l = np.load(file+"good/"+str(i)+".npy")
    uprep,downrep = divupdown(l,int(items[i][1]),int(items[i][2]))
    print(len(uprep))
    print(len(downrep))
    upl += uprep
    downl += downrep
  np.save('good_upreps.npy', np.array(upl, dtype=object))
  np.save('good_downreps.npy', np.array(downl, dtype=object))
  
  for i in range(4):
    l = np.load(file+"bad/"+str(i)+".npy")
    uprep,downrep = divupdown(l,int(items[i+4][1]),int(items[i+4][2]))
    print(len(uprep))
    print(len(downrep))
    np.save('bad'+str(i)+'_upreps.npy', np.array(uprep, dtype=object))
    np.save('bad'+str(i)+'_downreps.npy', np.array(downrep, dtype=object))

  # l = np.load(file+str(0)+".npy")
  # print(len(l))
  # uprep,downrep = divupdown(l,350,2180)
  # print(len(uprep))
  # print(len(downrep))
