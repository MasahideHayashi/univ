import cv2
import sys

file = "video/good/0.mp4"
cap = cv2.VideoCapture(file)

cap = cv2.VideoCapture(file)
if not cap.isOpened():
  print("Error opening video file")
  sys.exit()


count = 0
while True:
  ret, frame = cap.read()
  count += 1
  if ret:
    if count == 350+71: 
      cv2.imshow('Frame', frame)
      cv2.waitKey(0)
    if count == 350+98: 
      cv2.imshow('Frame', frame)
      cv2.waitKey(0)

  else:
    break

cap.release()
cv2.destroyAllWindows()