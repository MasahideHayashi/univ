from mmpose.apis import MMPoseInferencer
import numpy as np

img_path = '../tests/data/coco/000000000785.jpg'   # replace this with your own image path
video_path = ("data/good.mp4")

# instantiate the inferencer using the model alias
inferencer = MMPoseInferencer('human')

# The MMPoseInferencer API employs a lazy inference approach,
# creating a prediction generator when given input
result_generator = inferencer(video_path, show=True)
results = [result for result in result_generator]

#result = next(result_generator)
#print(result["predictions"][0][0]["keypoints"])
l = []
l.append(result["predictions"][0][0]["keypoints"])
l.append(result["predictions"][0][0]["keypoints"])
l = np.array(l)
print(l)

np.save("smpl", l)
