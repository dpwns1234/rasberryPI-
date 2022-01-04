# publisher/subscriber

import time
import paho.mqtt.client as mqtt
import myCamera # 카메라 사진 보내기
import myHw

flag = False # True이면 "action" 메시지를 수신하였음을 나타냄
ledState = 0 # 1이면 led에 불을 키고 0 이면 Led에 불을 끈다.
def on_connect(client, userdata, flag, rc):
        client.subscribe("facerecognition", qos = 0)
        client.subscribe("led", qos = 0)
def on_message(client, userdata, msg) :
        global flag
        global ledState
        command = msg.payload.decode("utf-8")
        if command == "action" :
                print("action msg received..")
                flag = True

        # topic = 'led'
        elif command == "On":
            ledState = 1
        elif command == "Off":
            ledState = 0


broker_ip = "localhost" # 현재 이 컴퓨터를 브로커로 설정

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_ip, 1883)
# loop 스레드 생성
client.loop_start()


# myLed에 만들면 ledState가 서로 달라서 웹버튼과 라즈베리파이버튼의 연동이 안됨.
def buttonPressed(pin):
    global ledState
    # led가 꺼져 있다면
    if ledState == 0:
        ledState = 1
        client.publish('clock', 'start', qos=0)    # 토픽 button으로 start란 메세지를 보내준다. -> mqttio.js
    # 켜져 있다면
    else:
        ledState = 0
        client.publish('clock', 'stop', qos=0)    # 토픽 button으로 stop이란 메세지를 보내준다. -> mqttio.js

# button 스레드 생성
myHw.GPIO.add_event_detect(myHw.button, myHw.GPIO.RISING, buttonPressed, 200)



while True :
        if flag==True : # "action" 메시지 수신. 사진 촬영
                imageFileName = myCamera.takePicture() # 카메라 사진 촬영
                print(imageFileName)
                client.publish("image", imageFileName, qos=0)
                flag = False

        # sub 받아서 ledState에 따라 led에 불이 켜지고 꺼지고를 결정한다.
        if(ledState == 1):
                myHw.startLed()
        else:
                myHw.stopLed()


        distance = myHw.measureDistance(myHw.trig, myHw.echo) # 매개변수 이렇게 해도 되나?
        # 공부 중인데(led가 켜져있는데) 스마트폰이 10 이상 떨어지면 스탑워치 종료
        if (ledState == 1 and distance > 10.0) :
            client.publish('clock', 'stop')
            print("공부 중 스마트폰 사용을 자제해주세요.") # 이건 어디에 출력되는거지?


        time.sleep(1)

client.loop_end()
client.disconnect()

