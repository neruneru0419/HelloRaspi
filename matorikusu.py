import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN_ANO = [23, 4, 17, 8, 22, 25, 15, 14]
PIN_CAT = [7, 18, 9, 24, 2, 10, 3, 27]


def setup():
	# アノードを、LOWで初期化
	for ano in range(8):
		GPIO.setup(PIN_ANO[ano], GPIO.OUT)

	# カソードを、HIGHで初期化
	for cat in range(8):
		GPIO.setup(PIN_CAT[cat], GPIO.OUT)

def loop():
	# カソードのループ
	for cat in range(8):
		GPIO.output( PIN_CAT[cat], False) # LOWに変更
		# アノードのループ
		for ano in range(8):
			GPIO.output( PIN_ANO[ano], True) # HIGHに変更
			time.sleep(0.1) # 点灯時間
			GPIO.output( PIN_ANO[ano], False ) # LOWに戻す
		GPIO.output( PIN_CAT[cat], True ) # HIGHに戻す
GPIO.cleanup()