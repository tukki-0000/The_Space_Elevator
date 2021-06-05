#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import pigpio
import sys

PIN = 18
minPulse = 650
maxPulse = 2000

print("初期化します。バッテリーを外してください。")

pi = pigpio.pi()
pi.set_servo_pulsewidth(PIN, maxPulse)

print("バッテリーを接続して、Enterを押してください。")
inp = input()
if inp == '':
    pi.set_servo_pulsewidth(PIN, minPulse)
    time.sleep(3)

print("\"stop\"")
print("\"u\" to up speed")
print("\"d\" to down speed")
speed = 1000
print("speed = %d" % speed)
while True:
    pi.set_servo_pulsewidth(PIN, speed)
    inp = input()
    if inp == "d":
        speed -= 100
        print("speed = %d" % speed)
    elif inp == "u":
        speed += 100    # incrementing the speed like hell
        print("speed = %d" % speed)
    elif inp == "stop":
        speed = 0
        pi.set_servo_pulsewidth(PIN, 0)
        break
    else:
        print("stop or u or d!")

# 終了処理
pi.stop()
