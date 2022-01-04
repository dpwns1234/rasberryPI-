import time
import RPi.GPIO as GPIO
trig = 20
echo = 16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)


# led setting
led = 6
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0);


def measureDistance(trig, echo):
    time.sleep(0.5)
    GPIO.output(trig, True) # 신호 1
    #time.sleep(0.00001) # 짧은 시간을 나타내기 위함
    GPIO.output(trig, False) # 신호가 1-> 0으로 떨어질 때 초음파발생

    while(GPIO.input(echo) == 0):
    	pass
    pulse_start = time.time() # echo 신호가 1인 경우, 초음파 발사된 순간 	while(GPIO.input(echo) == 1):
    while(GPIO.input(echo) == 1):
        pass
    pulse_end = time.time() # 초음파 신호가 도착한 순간
	# echo 신호가 1->0으로 되면 보낸 초음파 수신 완료

    pulse_duration = pulse_end - pulse_start
    return 340*100/2*pulse_duration
    
while True :
    distance = measureDistance(trig, echo)
    print("물체와의 거리는%fcm입니다" % distance)
    onOff = 0;
    # 10cm 미만이면 led 불 켜기
    if(distance < 10):
        onOff = 1
    # 10cm 이상이면 led 불 끄기
    else:
        onOff = 0
    GPIO.output(led, onOff);

