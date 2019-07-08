gimport RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN_ANO = [23, 4, 17, 8, 22, 25, 15, 14]
PIN_CAT = [7, 18, 9, 24, 2, 10, 3, 27]

for ano in range(8):
    GPIO.setup(PIN_ANO[ano], GPIO.OUT)
for cat in range(8):
    GPIO.setup(PIN_CAT[cat], GPIO.OUT)
ano_flg = 0

while True:
    #ここに値を入力する処理を書く
GPIO.cleanup()