import RPi.GPIO as GPIO
import time

Trig_Pin = 20
Echo_Pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig_Pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Echo_Pin, GPIO.IN)

time.sleep(2)

def checkdist():
    GPIO.output(Trig_Pin, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    t1 = time.time()
    while GPIO.input(Echo_Pin):
        pass
    t2 = time.time()
    return (t2-t1) *340/2

try:
    while True:
        print ('Distance:%0.2f m' % checkdist())
        time.sleep(3)
except KeyboardInterrupt:
    GPIO.cleanup()
'''
import RPi.GPIO
import time

stop = 14
D_1 = 21
D_2 = 22
D_3 = 23
D_4 = 24

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(stop,RPi.GPIO.IN)#红外检测距离
RPi.GPIO.setup(D_1,RPi.GPIO.OUT)#电机1
RPi.GPIO.setup(D_2,RPi.GPIO.OUT)#电机2
RPi.GPIO.setup(D_3,RPi.GPIO.OUT)#电机3
RPi.GPIO.setup(D_4,RPi.GPIO.OUT)#电机4

flag = 0;
get = 0;

print("start")

while(1):
    if(GPIO.input(14)==1):
        RPi.GPIO.output(D_1,False)
        RPi.GPIO.output(D_2,False)
        RPi.GPIO.output(D_3,False)
        RPi.GPIO.output(D_4,False)
    else:
        RPi.GPIO.output(D_1,True)
        RPi.GPIO.output(D_2,True)
        RPi.GPIO.output(D_3,True)
        RPi.GPIO.output(D_4,True)

    get = GPIO.input(14)
    if (get == 1 & flag == 0):
        print("get")
        flag = 1
    if (get == 0):
        flag == 0
        '''
'''
for i in range (0,10):
    RPi.GPIO.output(14,True)
    time.sleep(0.5)
    RPi.GPIO.output(14,False)
    time.sleep(0.5)
'''
print("end")
RPi.GPIO.cleanup()
