from motorModule import Motor
import keyboardModule as kp

motor = Motor(17,22,27, 2,3,4)

kp.init()

def main():
    print(kp.getKey('s'))
    
    if kp.getKey("UP"):
        motor.move(0.6, 0, 0.1)
        
    elif kp.getKey("DOWN"):
        motor.move(-0.6, 0, 0.1)
        
    elif kp.getKey("LEFT"):
        motor.move(0.5, 0.3, 0.1)
    
    elif kp.getKey("RIGHT"):
        motor.move(0.5, -0.3, 0.1)
    
    else:
        motor.stop(0.1)
        
if __name__ == '__main__':
    while True:
        main()
        

        