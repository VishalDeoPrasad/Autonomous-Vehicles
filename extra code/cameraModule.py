import cv2
import sys

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#cap.set(3, 160)
#cap.set(4, 120)

if (cap.isOpened() == False):
    print("Stuggling With Opening Video Capture:")
    sys.exit()

def readCamera(record=False, display=False, size=[640, 480]):
    ret,frame = cap.read()
    if ret == True:
        img = cv2.resize(frame, (size[0], size[1]))
        if record:
            out.write(img)
            cv2.imshow("Frame",img)
                 
        if display:
            cv2.imshow("Frame",img)
        return img
        
        

if __name__ == '__main__':
    while True:
        readCamera(record=True)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

