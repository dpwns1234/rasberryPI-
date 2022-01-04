import time
import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = 6
GPIO.setup(led, GPIO.OUT)

def increase(led, pwm): 
    print("increase the light")
    for value in range(0, 100): # 5초 동안 루프
        pwm.ChangeDutyCycle(value) # 펄스의 듀티비 커짐
        time.sleep(0.05)

def decrease(led, pwm):
    print("decrease the light")
    for value in range(99, -1, -1): # 5초 동안 루프
        pwm.ChangeDutyCycle(value) # 펄스의 듀티비 작아짐
        time.sleep(0.05)

GPIO.output(led, GPIO.LOW)
pwm = GPIO.PWM(led, 50) #50hz의 펄스를 출력하도록 설정
pwm.start(0)
while True:
    increase(led, pwm)
    decrease(led, pwm)
