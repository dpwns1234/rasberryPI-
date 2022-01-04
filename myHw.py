import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# led, button setUp
led1 = 5 # 공부 start led
led2 = 6 # 공부 stop led
button = 21
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)

# 초음파 센서 setUp
trig = 20
echo = 16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)


def startLed():
	GPIO.output(led1, 1)
	GPIO.output(led2, 0)

def stopLed():
	GPIO.output(led1, 0)
	GPIO.output(led2, 1)

def measureDistance(trig, echo):
	time.sleep(0.5)
	GPIO.output(trig, True) # 신호 1
	#time.sleep(0.00001) # 짧은 시간을 나타내기 위함
	GPIO.output(trig, False) # 신호가 1-> 0으로 떨어질 때 초음파발생

	while(GPIO.input(echo) == 0): # 아직 echo 가 신호를 안 쐈으면 쏠 때까지 대기
		pass
	pulse_start = time.time() # echo 신호가 1인 경우, 초음파 발사된 순간
	while(GPIO.input(echo) == 1):
		pass 
	pulse_end = time.time() # 초음파 신호가 도착한 순간
	# echo 신호가 1->0으로 되면 보낸 초음파 수신 완료

	pulse_duration = pulse_end - pulse_start
	return 340*100/2*pulse_duration

