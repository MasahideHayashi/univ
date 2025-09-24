from mmpose.apis import MMPoseInferencer
import numpy as np
import os

#img_path = '../tests/data/coco/000000000785.jpg'   # replace this with your own image path
video_path = "video/youtube"

files = os.listdir(video_path)

# instantiate the inferencer using the model alias
inferencer = MMPoseInferencer('human')

# The MMPoseInferencer API employs a lazy inference approach,
# creating a prediction generator when given input
for file in files:
    if file[-4:] != ".mov" : continue
    result_generator = inferencer(video_path+"/"+file, show=False)
    results = [result for result in result_generator]
    l = []
    for i in range(len(results)):
        l.append(results[i]["predictions"][0][0]["keypoints"])
    
    l = np.array(l)
    np.save("posedata/youtube/"+file[0:-4], l)
