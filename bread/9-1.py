import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # BCM 모드로 작동
GPIO.setwarnings(False) # 경고글이 출력되지 않게 설정

def ledOnOff(led, onOff): # led 번호의 핀에 onOff(0/1) 값 출력하는 함수
        GPIO.output(led, onOff)

led = 6 # 핀 번호 GPIO6 의미
GPIO.setup(led, GPIO.OUT) # GPIO 6번 핀을 출력 선으로 지정.

onOff = 1 # 1은 디지털 출력 값. 1 = 5V
print("LED를 지켜 보세요.")

# 5번 LED를 깜박임
for i in range(10):
        ledOnOff(led, onOff) # led가 연결된  핀에 1또는 0의 디지털 값 출력
        time.sleep(1)
        onOff = 0 if onOff == 1 else 1 # 0과 1의 토글링

