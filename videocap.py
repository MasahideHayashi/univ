import cv2
import sys

args = sys.argv

def writevideo(cap):
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    forucc = cv2.VideoWriter_fourcc("m","p","4","v")
    video = cv2.VideoWriter(args[1],forucc,fps,(w,h))

    while(cap.isOpened()):
        ret, frame = cap.read()
        video.write(frame)
        cv2.imshow("a",frame)
        if cv2.waitKey(1)&0xff==ord("q"):
            break

    cap.release()
    video.release()
    cv2.destroyAllWindows()
   

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        writevideo(cap)

