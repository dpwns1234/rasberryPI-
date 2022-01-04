import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def ledOnOff(led, onOff):
    GPIO.output(led, onOff)

led = 6 # 핀 번호 6
GPIO.setup(led, GPIO.OUT) # 핀 6을 출력으로 지정

button = 21 # 핀 번호 21
GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN) # 핀 21을 입력으로 지정. 풀다운 효과 지정
print("스위치를 누르고 있는 동안 LED가 On되고 놓으면 꺼집니다.")
while True :
    btnStatus = GPIO.input(button) # 버튼 즉, 핀 21의 디지털 값(0/1)을 읽기
    ledOnOff(led, btnStatus) # 읽은 값(0/1)을 핀 6으로 출력


