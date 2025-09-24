import cv2
import sys

file = "../video/bad/3.mp4"
cap = cv2.VideoCapture(file)

cap = cv2.VideoCapture(file)
if not cap.isOpened():
  print("Error opening video file")
  sys.exit()


count = 0
while True:
  ret, frame = cap.read()
  count += 1
  if count < 250:
    continue
  if ret:
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    elif cv2.waitKey(1) & 0xFF == ord('s'):
      print(count)
  else:
    break

cap.release()
cv2.destroyAllWindows()