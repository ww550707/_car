import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(14,RPi.GPIO.IN)

flag = 0;
get = 0;

print("start")

while(1):
    get = GPIO.input(14)
    if (get == 1 & flag == 0):
        print("get")
        flag = 1
    if (get == 0):
        flag == 0
'''
for i in range (0,10):
    RPi.GPIO.output(14,True)
    time.sleep(0.5)
    RPi.GPIO.output(14,False)
    time.sleep(0.5)
'''
print("end")
RPi.GPIO.cleanup()
