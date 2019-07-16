import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN_ANO = [16, 4, 5, 11, 7, 12, 18, 19]
PIN_CAT = [10, 17, 9, 13, 2, 8, 3, 6]

for ano in range(8):
    GPIO.setup(PIN_ANO[ano], GPIO.OUT)
for cat in range(8):
    GPIO.setup(PIN_CAT[cat], GPIO.OUT)
ARRAY_A = [ [ 1, 1, 1, 0, 0, 1, 1, 1 ],
            [ 1, 1, 0, 1, 1, 0, 1, 1 ],
            [ 1, 0, 1, 1, 1, 1, 0, 1 ],
            [ 1, 0, 0, 1, 1, 1, 0, 1 ],
            [ 1, 0, 1, 1, 1, 1, 0, 1 ],
            [ 1, 0, 1, 1, 1, 1, 0, 1 ],
            [ 1, 0, 0, 0, 0, 0, 0, 1 ],
            [ 1, 0, 1, 1, 1, 1, 0, 1 ] ]

while True:
    for cat in range(8):
        GPIO.output(PIN_CAT[cat], False) # LOWに変更
            # アノードのループ
        for ano in range(8):
            GPIO.output( PIN_ANO[ano], ARRAY_A[cat][ano] ) # HIGH or LOW
        time.sleep(0.0001) # 点灯時間（100μ秒）
        for ano in range(8):
            GPIO.output(PIN_ANO[ano], False) # LOWに戻す
        GPIO.output(PIN_CAT[cat], True); # HIGHに戻す
GPIO.cleanup()
