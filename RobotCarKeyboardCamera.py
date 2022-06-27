from motorModule import Motor
import keyboardModule as kp
import CameraModule as cam
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
    while True:
        #main()
        if kp.getKey('q'):
            print("Quiting")
            kp.close()
            break
            #sys.exit()
            
        elif kp.getKey("UP"):
            motor.forward()
            
        elif kp.getKey("DOWN"):
            motor.backward()
            
        elif kp.getKey("LEFT"):
            motor.leftTurn()
        
        elif kp.getKey("RIGHT"):
            motor.rightTurn()
        
        else:
            motor.stop()
        cam.readCamera(display=True)
        if cv2.waitKey(1) & 0xFF == 27:
            kp.close()
            break
    cap.release()
    cv2.destroyAllWindows()   

        