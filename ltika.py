import RPi.GPIO as GPIO
import time

# GPIOの初期化/出力に設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

#無限ループ
while True:
    GPIO.output(2,True)
    time.sleep(1) # sleep1秒
                
    GPIO.output(2,False) # LED点灯
    time.sleep(1) # sleep1秒
GPIO.cleanup()
