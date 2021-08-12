import RPi.GPIO as GPIO
import time

TRIG_PIN = 23
ECHO_PIN = 24


GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)
GPIO.setwarnings(False)

def pulseIn(PIN, start=1, end=0):
    if start==0: end = 1
    t_start = 0
    t_end = 0

    while GPIO.input(PIN) == end:
        t_start = time.time()
        
    while GPIO.input(PIN) == start:
        t_end = time.time()
    return t_end - t_start

while True:
    GPIO.output(TRIG_PIN, GPIO.LOW)
    time.sleep(0.01)
  
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    t = pulseIn(ECHO_PIN)

    distance = 34000 * t/2
    if distance <= 90:
        print(distance, "cm")
    else:
        continue
