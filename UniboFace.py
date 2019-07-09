import RPi.GPIO as GPIO
import time
class DotMatrixLED:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.PIN_ANO = [23, 4, 17, 8, 22, 25, 15, 14]
        self.PIN_CAT = [7, 18, 9, 24, 2, 10, 3, 27]

        for ano in range(8):
            GPIO.setup(self.PIN_ANO[ano], GPIO.OUT)
        for cat in range(8):
            GPIO.setup(self.PIN_CAT[cat], GPIO.OUT)

        self.NormalFace = [[ 1, 1, 1, 1, 1, 1, 1, 1 ],
                           [ 1, 1, 1, 1, 1, 1, 1, 1 ],
                           [ 1, 1, 0, 1, 1, 0, 1, 1 ],
                           [ 1, 1, 0, 1, 1, 0, 1, 1 ],
                           [ 1, 1, 0, 1, 1, 0, 1, 1 ],
                           [ 1, 1, 1, 1, 1, 1, 1, 1 ],
                           [ 1, 1, 1, 1, 1, 1, 1, 1 ],
                           [ 1, 1, 1, 1, 1, 1, 1, 1 ]]

        self.MovedNormalFace = [[ 1, 1, 1, 1, 1, 1, 1, 1 ],
                                [ 1, 1, 1, 1, 1, 1, 1, 1 ],
                                [ 1, 1, 1, 0, 1, 1, 0, 1 ],
                                [ 1, 1, 1, 0, 1, 1, 0, 1 ],
                                [ 1, 1, 1, 0, 1, 1, 0, 1 ],
                                [ 1, 1, 1, 1, 1, 1, 1, 1 ],
                                [ 1, 1, 1, 1, 1, 1, 1, 1 ],
                                [ 1, 1, 1, 1, 1, 1, 1, 1 ]]

        self.SmailFace = [[ 1, 1, 1, 1, 1, 1, 1, 1 ],
                          [ 1, 1, 1, 1, 1, 1, 1, 1 ],
                          [ 1, 0, 0, 1, 1, 0, 0, 1 ],
                          [ 1, 0, 0, 1, 1, 0, 0, 1 ],
                          [ 1, 1, 1, 1, 1, 1, 1, 1 ],
                          [ 1, 1, 0, 1, 1, 0, 1, 1 ],
                          [ 1, 1, 0, 0, 0, 0, 1, 1 ],
                          [ 1, 1, 1, 1, 1, 1, 1, 1 ]]

        self.MovedSmailFace = [[ 1, 1, 1, 1, 1, 1, 1, 1 ],
                               [ 1, 1, 1, 1, 1, 1, 1, 1 ],
                               [ 1, 1, 0, 0, 1, 1, 0, 0 ],
                               [ 1, 1, 0, 0, 1, 1, 0, 0 ],
                               [ 1, 1, 1, 1, 1, 1, 1, 1 ],
                               [ 1, 1, 1, 0, 1, 1, 0, 1 ],
                               [ 1, 1, 1, 0, 0, 0, 0, 1 ],
                               [ 1, 1, 1, 1, 1, 1, 1, 1 ]]
    #ダイナミック点灯をする関数
    def SelectFace(self, face):
        try:
            while True:
                #カソードのループ
                for cat in range(8):
                    GPIO.setup(self.PIN_CAT[cat], False) # LOWに変更
                    # アノードのループ
                    for ano in range(8):
                        if face == 1:
                            GPIO.setup(self.PIN_ANO[ano], self.NormalFace[cat][ano]) # HIGH or LOW
                        elif face == 2:
                            GPIO.setup(self.PIN_ANO[ano], self.MovedNormalFace[cat][ano]) # HIGH or LOW
                        elif face == 3:
                            GPIO.setup(self.PIN_ANO[ano], self.SmailFace[cat][ano]) # HIGH or LOW
                        elif face == 4:
                            GPIO.setup(self.PIN_ANO[ano], self.MovedSmailFace[cat][ano]) # HIGH or LOW
                    time.sleep(0.0001) 
                    for ano in range(8):
                        GPIO.setup(self.PIN_ANO[ano], False) # LOWに戻す
                    GPIO.setup(self.PIN_CAT[cat], True); # HIGHに戻す
        except:
            print("ctrl+cが押されました")

UniboFace = DotMatrixLED()
while True:
    SelectUniboFace = int(input("表情を選択してください(ctrl+cで表情選択に戻ります) 1:normal 2:movednormal 3:smail 4:movedsmail 0:終了\n=>"))
    if SelectUniboFace:
        UniboFace.SelectFace(SelectUniboFace)
    else:
        break
GPIO.cleanup()