import RPi.GPIO as GPIO
import time
class DotMatrixLED:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        #ここを適宜書き換える
        self.PIN_ANO = [23, 4, 17, 8, 22, 25, 15, 14]
        self.PIN_CAT = [7, 18, 9, 24, 2, 10, 3, 27]

        for ano in range(8):
            GPIO.setup(self.PIN_ANO[ano], GPIO.OUT)
        for cat in range(8):
            GPIO.setup(self.PIN_CAT[cat], GPIO.OUT)

        self.normal_face = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                            [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                            [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                            [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                            [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

        self.moved_normal_face = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                  [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                  [ 0, 0, 0, 1, 0, 0, 1, 0 ],
                                  [ 0, 0, 0, 1, 0, 0, 1, 0 ],
                                  [ 0, 0, 0, 1, 0, 0, 1, 0 ],
                                  [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                  [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                  [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

        self.smile_face = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                           [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                           [ 0, 1, 1, 0, 0, 1, 1, 0 ],
                           [ 0, 1, 1, 0, 0, 1, 1, 0 ],
                           [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                           [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                           [ 0, 0, 1, 1, 1, 1, 0, 0 ],
                           [ 0, 0, 0, 0, 0, 0, 0, 0 ]]

        self.moved_smile_face = [[ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                 [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                 [ 0, 0, 1, 1, 0, 0, 1, 1 ],
                                 [ 0, 0, 1, 1, 0, 0, 1, 1 ],
                                 [ 0, 0, 0, 0, 0, 0, 0, 0 ],
                                 [ 0, 0, 0, 1, 0, 0, 1, 0 ],
                                 [ 0, 0, 0, 1, 1, 1, 1, 0 ],
                                 [ 0, 0, 0, 0, 0, 0, 0, 0 ]]
    #ダイナミック点灯をする関数
    def select_face(self, face):
        try:
            while True:
                #カソードのループ
                for cat in range(8):
                    GPIO.output(self.PIN_CAT[cat], False) # LOWに変更
                    # アノードのループ
                    for ano in range(8):
                        #選択された数字によって顔を変化
                        if face == 1:
                            GPIO.output(self.PIN_ANO[ano], self.normal_face[cat][ano]) # HIGH or LOW
                        elif face == 2:
                            GPIO.output(self.PIN_ANO[ano], self.moved_normal_face[cat][ano]) # HIGH or LOW
                        elif face == 3:
                            GPIO.output(self.PIN_ANO[ano], self.smile_face[cat][ano]) # HIGH or LOW
                        elif face == 4:
                            GPIO.output(self.PIN_ANO[ano], self.moved_smile_face[cat][ano]) # HIGH or LOW
                    time.sleep(0.0001) 
                    for ano in range(8):
                        GPIO.output(self.PIN_ANO[ano], False) # LOWに戻す
                    GPIO.output(self.PIN_CAT[cat], True) # HIGHに戻す
        except:
            print("ctrl+cが押されました")
            GPIO.cleanup


unibo_face = DotMatrixLED()
while True:
    try:
        select_unibo_face = int(input("表情を選択してください(選択した後はctrl+cで表情選択に戻ります) 1:normal 2:movednormal 3:smile 4:movedsmile 0:終了\n=>"))
        if select_unibo_face:
            unibo_face.select_face(select_unibo_face)
        else:
            GPIO.cleanup()
            break
    except:
        print("ctrl+cが押されました")
        GPIO.cleanup