import RPi.GPIO as GPIO
import time
class DotMatrixLED:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        #ここを適宜書き換える
        self.PIN_ANO = [16, 4, 5, 11, 7, 12, 18, 19]
        self.PIN_CAT = [10, 17, 9, 13, 2, 8, 3, 6]
        self.time_count = 0
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
                                 [ 0, 0, 1, 0, 0, 1, 0, 0 ],
                                 [ 0, 0, 1, 1, 1, 1, 0, 0 ],
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
                        if self.time_count % 1500 <= 750:
                            GPIO.output(self.PIN_ANO[ano], self.smile_face[cat][ano]) # HIGH or LOW
                        else:
                            GPIO.output(self.PIN_ANO[ano], self.moved_smile_face[cat][ano]) # HIGH or LOW
                    time.sleep(0.0001) 
                    for ano in range(8):
                        GPIO.output(self.PIN_ANO[ano], False) # LOWに戻す
                    GPIO.output(self.PIN_CAT[cat], True) # HIGHに戻す
                self.time_count += 1
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
