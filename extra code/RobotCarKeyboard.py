from motorModule import Motor
import keyboardModule as kp

motor= Motor(3,4,17,27)

kp.init()

def main():
    print(kp.getKey('s'))
    
    if kp.getKey("UP"):
        motor.forward()
        
    elif kp.getKey("DOWN"):
        motor.backward()
        
    elif kp.getKey("LEFT"):
        motor.leftTurn()
    
    elif kp.getKey("RIGHT"):
        motor.rightTurn()
    
    else:
        motor.stop()
        
if __name__ == '__main__':
    while True:
        main()
        

        