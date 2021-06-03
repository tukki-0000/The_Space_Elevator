import time
import RPi.GPIO as GPIO

t1 = time.time()

GPIO.setmode(GPIO.BCM)                                  # ピンをGPIOの番号で指定
x = 26                                              # ピンの名前を変数として定義

GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # GPIOセットアップ
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

#周波数50Hz
p1 = GPIO.PWM(21, 50)
p2 = GPIO.PWM(20, 50)

p1.start(7)
p2.start(2)
#main
try:
    if __name__ == '__main__':
        find_flg    = 0                             # フラグの初期化
        counter     = 0                             # カウンターを初期化
        while True:
            t2 = time.time()
            t3 = t2 - t1
            if t3 >= 3:
                counter = 10

            if GPIO.input(x) == GPIO.HIGH:     # LOWからHIGHになる時にカウントアップ
                if find_flg == 1:                   # 検知
                    counter += 1
                    print(counter)
                find_flg =0
            else:
                find_flg =1                         # 検知

            if counter == 10:
                dc1 = float(11.6)
                dc2 = float(7)

                p1.ChangeDutyCycle(dc1)
                p2.ChangeDutyCycle(dc2)

except KeyboardInterrupt:  #Ctrl + Cで止まらせることが多い
    pass
GPIO.cleanup()
