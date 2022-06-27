from motorModule import Motor
import keyboardModule as kp
import CameraModule as cam
import laneModule as lm
import sys
import cv2
import pygame

#############
motor= Motor(3,4,17,27)
#############

kp.init()

def main():
    pass
        
if __name__ == '__main__':
    cap = cv2.VideoCapture('vid1.mp4')
    cam = cam.camera(cap)
    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
 
        img=cam.readCamera(display=False)
        img = cv2.resize(img,(480,240))
        curve = lm.getLaneCurve(img,display=2)
        print(curve)
            
        if curve >=-0.25 and curve <=0.20:
            motor.forward()
                 
        elif curve <= -0.24:
            motor.leftTurn()
        
        elif curve >= 0.20:
            motor.rightTurn()
          
        if cv2.waitKey(1) & 0xFF == 27:
            #kp.close()
            break
        
    cap.release()
    cv2.destroyAllWindows()   

        