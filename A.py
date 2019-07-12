import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN_ANO = [23, 4, 17, 8, 22, 25, 15, 14]
PIN_CAT = [7, 18, 9, 24, 2, 10, 3, 27]

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
        GPIO.setup(PIN_CAT[cat], False) # LOWに変更
		# アノードのループ
		for ano in range(8):
			GPIO.setup( PIN_ANO[ano], ARRAY_A[cat][ano] ) # HIGH or LOW
		time.sleep(0.0001) # 点灯時間（100μ秒）
		for ano in range(8):
			GPIO.setup(PIN_ANO[ano], False) # LOWに戻す
		GPIO.setup(PIN_CAT[cat], True); # HIGHに戻す
GPIO.cleanup()