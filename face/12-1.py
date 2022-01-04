import cv2

haar = cv2.CascadeClassifier('../haarCascades/haar-cascade-\
files-master/haarcascade_frontalface_default.xml')

image = cv2.imread('../bts.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = haar.detectMultiScale(image_gray,1.1,3)

for x, y, w, h in faces:
	cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)



cv2.imwrite('./ bts-makrded.jpg', image)
