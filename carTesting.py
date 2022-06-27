import RPi.GPIO as GPIO
import time

N1, N2, N3, N4 = 3, 4, 17, 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(N1, GPIO.OUT) #fw left
GPIO.setup(N2, GPIO.OUT) #bw left
GPIO.setup(N3, GPIO.OUT) #fw right
GPIO.setup(N4, GPIO.OUT) #bw right

try:
    while True:
        #forward moving
        print("running N1, running N3")
        GPIO.output(N1, GPIO.HIGH) # fW left
        GPIO.output(N3, GPIO.HIGH) #FW right
        time.sleep(1)
        GPIO.output(N1, GPIO.LOW)
        GPIO.output(N3, GPIO.LOW)
        time.sleep(1)
        
        #backward moving
        print("running N2, running N4")
        GPIO.output(N2, GPIO.HIGH) # BW left
        GPIO.output(N4, GPIO.HIGH) # BW right
        time.sleep(1)
        GPIO.output(N2, GPIO.LOW)
        GPIO.output(N4, GPIO.LOW)
        time.sleep(1)
        
        #left moving
        print("running N4")
        GPIO.output(N4, GPIO.HIGH) # BW right
        time.sleep(1)
        GPIO.output(N4, GPIO.LOW)
        time.sleep(1)
        
        #right moving
        print("running N2")
        GPIO.output(N2, GPIO.HIGH) # FW right
        time.sleep(1)
        GPIO.output(N2, GPIO.LOW)
        time.sleep(1)
                            
except KeyboardInterrupt: 
	print("KeyBoard Interrupt:")
	
except:
	print("Some Error")

finally:
	print("Cleaning UP:")
	GPIO.cleanup()
