import invkinematics

from mmpose.apis import MMPoseInferencer
import numpy as np


#img_path = '../tests/data/coco/000000000785.jpg'   # replace this with your own image path
img_path = "data/dum"

# instantiate the inferencer using the model alias
inferencer = MMPoseInferencer('human')

# The MMPoseInferencer API employs a lazy inference approach,
# creating a prediction generator when given input
result_generator = inferencer(img_path, show=False)
results = [result for result in result_generator]

a = results[0]["predictions"][0][0]["keypoints"]
b = results[1]["predictions"][0][0]["keypoints"]

at0,at1,al0,al1 = invkinematics.calc_theta(a)
bt0,bt1,bl0,bl1 = invkinematics.calc_theta(b)
J = invkinematics.calc_jacovianMatrix(at0,at1,al0,al1)
deltheta0,deltheta1 = invkinematics.calc_deltheta(a,b)
r = invkinematics.calc_velocity(J,deltheta0,deltheta1)
F = [0,10]
tau = invkinematics.calc_torque(F,J)
print("r", r)
print("tau", tau)

