import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN_ANO = [23, 4, 17, 8, 22, 25, 15, 14]
PIN_CAT = [7, 18, 9, 24, 2, 10, 3, 27]

for ano in range(8):
    GPIO.setup(PIN_ANO[ano], GPIO.OUT)
for cat in range(8):
    GPIO.setup(PIN_CAT[cat], GPIO.OUT)

NormalFace = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 1, 0, 0, 1, 0, 0 ],
              [ 0, 0, 1, 0, 0, 1, 0, 0 ],
              [ 0, 0, 1, 0, 0, 1, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

MovedNormalFace = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 1, 0, 0, 1, 0 ],
                   [ 0, 0, 0, 1, 0, 0, 1, 0 ],
                   [ 0, 0, 0, 1, 0, 0, 1, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

SmailFace = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
             [ 0, 0, 0, 0, 0, 0, 0, 0 ],
             [ 0, 1, 1, 0, 0, 1, 1, 0 ],
             [ 0, 1, 1, 0, 0, 1, 1, 0 ],
             [ 0, 0, 0, 0, 0, 0, 0, 0 ],
             [ 0, 0, 1, 0, 0, 1, 0, 0 ],
             [ 0, 0, 1, 1, 1, 1, 0, 0 ],
             [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

MovedSmailFace = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                  [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                  [ 0, 0, 1, 1, 0, 0, 1, 1 ],
                  [ 0, 0, 1, 1, 0, 0, 1, 1 ],
                  [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                  [ 0, 0, 0, 1, 0, 0, 1, 0 ],
                  [ 0, 0, 0, 1, 1, 1, 1, 0 ],
                  [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

while True:
    for cat in range(8):
        GPIO.setup(PIN_CAT[cat], False) # LOWに変更
		# アノードのループ
        SelectFace = int(input("顔選択=>"))
		for ano in range(8):
            if SelectFace == 1:
			    GPIO.setup( PIN_ANO[ano], NormalFace[cat][ano] ) # HIGH or LOW
            elif SelectFace == 2:
			    GPIO.setup( PIN_ANO[ano], MovedNormalFace[cat][ano] ) # HIGH or LOW
            elif SelectFace == 3:
			    GPIO.setup( PIN_ANO[ano], SmailFace[cat][ano] ) # HIGH or LOW
            elif SelectFace == 4:
			    GPIO.setup( PIN_ANO[ano], MovedSmailFace[cat][ano] ) # HIGH or LOW
        time.sleep(0.0001) # 点灯時間（100μ秒）
		for ano in range(8):
			GPIO.setup(PIN_ANO[ano], False) # LOWに戻す
		GPIO.setup(PIN_CAT[cat], True); # HIGHに戻す
GPIO.cleanup()