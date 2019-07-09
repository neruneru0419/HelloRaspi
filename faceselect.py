import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN_ANO = [23, 4, 17, 8, 22, 25, 15, 14]
PIN_CAT = [7, 18, 9, 24, 2, 10, 3, 27]

for ano in range(8):
    GPIO.setup(PIN_ANO[ano], GPIO.OUT)
for cat in range(8):
    GPIO.setup(PIN_CAT[cat], GPIO.OUT)
ano_flg = 0
point = 0
pin = 0 
while True:
    ano_flg = int(input("gpioflg on(0) or (1) =>"))
    pin = int(input("pin `縦(0) or 横(1) =>"))
    point = int(input("point=>"))
    if pin == 0:
        GPIO.setup(PIN_ANO[point], ano_flg)
    elif pin == 1:
        GPIO.setup(PIN_CAT[point], ano_flg)
    print("")
GPIO.cleanup()
