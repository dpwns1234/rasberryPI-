import io
import time
import picamera
import cv2
import numpy as np

stream = io.BytesIO()
with picamera.PICamera() as camera:
	camera.resolution = (640, 480)
	camera.start_preview()
	time.sleep(10)
	camera.capture(stream, formet='jpeg')
	camera.stop_preview()


data = np.frombuffer(stream.getvalue(), dtype=np.unit8)
image = cv2.imdecode(data, 1)



haar = cv2.CascadeClassifier('../haarCascades/haar-cascade-files-master/haarcascade_frontalface_default.xml')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = haar.detectMultiScale(image_gray, 1.1, 3)

for x, y, w, h in faces:
	cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imwrite('opencv-camera.jpg', image)
