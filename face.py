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
point = 0
pin = 
while True:
    pin = int(input("ano=>0 cat=>1"))
    ano_flg = int(input())
    point = int(input())
    if pin == 0:
        GPIO.setup(PIN_ANO[point], ano_flg)
GPIO.cleanup()