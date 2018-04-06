import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(14,RPi.GPIO.OUT)

print("start")

for i in range (0,10):
    RPi.GPIO.output(14,True)
    time.sleep(0.5)
    RPi.GPIO.output(14,False)
    time.sleep(0.5)

print("end")
RPi.GPIO.cleanup()
