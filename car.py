import PRi.GPIO
import time

RPi.GPIO.setmode(RPI.GPIO.BCM)
RPi.GPIO.setup(14,RPI.GPIO.OUT)

print("start")

for i in range (0,10):
    RPi.GPIO.output(14,True)
    time.sleep(0.5)
    RPi.GPIO.output(14,False)
    time.sleep(0.5)

print("end")
RPi.GPIO.cleanup()