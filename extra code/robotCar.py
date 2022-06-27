from motorModule1 import Motor
import time
 
motor= Motor(3,4,17,27)
 
def main():
    motor.forward(2)
    time.sleep(2)
    motor.backward(2)
    time.sleep(2)
    motor.leftTurn(2)
    time.sleep(2)
    motor.rightTurn(2)
    time.sleep(2)
    motor.stop(2)
 
if __name__ == '__main__':
    while True:
        main()