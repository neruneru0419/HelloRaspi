import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)

status = 0
print("start")
try:
    while True:
        value = GPIO.input(25)
        if value != status:
            print("hoge")
            print(value)
            status = value

except(KeyboardInterrupt):
    print("interrupt")

GPIO.cleanup()

