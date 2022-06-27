import cv2
import sys

class camera:
    def __init__(self, cap, frame_size=[640, 480]):
        self.cap = cap
        self.frame_size = frame_size
        
    def readCamera(self, display):
        if (self.cap.isOpened() == False):
            print("Stuggling With Opening Video Capture:")
            sys.exit()
            
        ret, frame = self.cap.read()
        if ret == True:
            img = cv2.resize(frame, (self.frame_size[0], self.frame_size[1]))
            if display:
                cv2.imshow("Frame",img)
            return img
            
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cam = camera(cap)
    while True:
        cam.readCamera(display=True)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

