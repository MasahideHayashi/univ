from mmpose.apis import MMPoseInferencer
import numpy as np

#img_path = '../tests/data/coco/000000000785.jpg'   # replace this with your own image path
video_path = "data/bad2.mp4"

# instantiate the inferencer using the model alias
inferencer = MMPoseInferencer('human')

# The MMPoseInferencer API employs a lazy inference approach,
# creating a prediction generator when given input
result_generator = inferencer(video_path, show=False)
results = [result for result in result_generator]
l = []
for i in range(len(results)):
    l.append(results[i]["predictions"][0][0]["keypoints"])

l = np.array(l)
np.save("bad2", l)
