from motorModule import Motor
import keyboardModule as kp
import CameraModule as cam
import laneModule as lm
import sys
import cv2
import pygame

motor= Motor(3,4,17,27)

kp.init()

def main():
    pass
        
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cam = cam.camera(cap)
    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
 
        img=cam.readCamera(display=True)
        img = cv2.resize(img,(480,240))
        curve = lm.getLaneCurve(img,display=1)
        print(curve)
        #main()
        if kp.getKey('q'):
            print("Quiting")
            motor.stop()
            kp.close()
            break
            #sys.exit()
            
        elif kp.getKey("UP") :
            motor.forward()
            
        elif kp.getKey("DOWN"):
            motor.backward()
            
        elif kp.getKey("LEFT") :
            motor.leftTurn()
        
        elif kp.getKey("RIGHT"):
            motor.rightTurn()
        
        else:
            motor.stop()
        
        if cv2.waitKey(1) & 0xFF == 27:
            motor.stop()
            kp.close()
            break
    cap.release()
    cv2.destroyAllWindows()   

        