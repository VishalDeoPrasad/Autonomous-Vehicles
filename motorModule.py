import RPi.GPIO as GPIO
import time

class Motor:
    def __init__(self, n1, n2, n3, n4):
        self.N1, self.N2, self.N3, self.N4 = n1, n2, n3, n4

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.N1, GPIO.OUT) #fw left
        GPIO.setup(self.N2, GPIO.OUT) #bw left
        GPIO.setup(self.N3, GPIO.OUT) #fw right
        GPIO.setup(self.N4, GPIO.OUT) #bw right
        
    def forward(self, t=0):
        GPIO.output(self.N1, GPIO.HIGH) # LF
        GPIO.output(self.N2, GPIO.LOW) # LB
        GPIO.output(self.N3, GPIO.HIGH) # RF
        GPIO.output(self.N4, GPIO.LOW) # RB
        time.sleep(t)
    
    def backward(self, t=0):
        GPIO.output(self.N1, GPIO.LOW) # LF
        GPIO.output(self.N2, GPIO.HIGH) # LB
        GPIO.output(self.N3, GPIO.LOW) # RF
        GPIO.output(self.N4, GPIO.HIGH) # RB
        time.sleep(t)
        
    def leftTurn(self, t=0):
        GPIO.output(self.N1, GPIO.LOW) # LF
        GPIO.output(self.N2, GPIO.HIGH) # LB
        #GPIO.output(self.N2, GPIO.LOW) # LB
        GPIO.output(self.N3, GPIO.HIGH) # RF
        GPIO.output(self.N4, GPIO.LOW) # RB
        time.sleep(t)
        
    def rightTurn(self, t=0):
        GPIO.output(self.N1, GPIO.HIGH) # LF
        GPIO.output(self.N2, GPIO.LOW) # LB
        GPIO.output(self.N3, GPIO.LOW) # RF
        GPIO.output(self.N4, GPIO.HIGH) # RB
        #GPIO.output(self.N4, GPIO.LOW) # RB
        time.sleep(t)
    
    def stop(self, t=0):
        GPIO.output(self.N1, GPIO.LOW) # LF
        GPIO.output(self.N2, GPIO.LOW) # LB
        GPIO.output(self.N3, GPIO.LOW) # RF
        GPIO.output(self.N4, GPIO.LOW) # RB
        time.sleep(t)

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

if __name__ == '__main__' :
    motor = Motor(3,4,17,27)
    while True:
        main()
    
    
    

    
'''
try:
    while True:
        pass
                            
    
                            
		
except KeyboardInterrupt: 
	print("KeyBoard Interrupt:")
	
except:
	print("Some Error")

finally:
	print("Cleaning UP:")
	GPIO.cleanup()
'''
