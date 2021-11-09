import cv2
from random import randrange

traing_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#image you can select
#img = cv2.imread('smile.jpg')
#img = cv2.imread('tonny.jpg')
#img = cv2.imread('smile2.jpg')
#img = cv2.imread('smile3.jpg')

#Now we use webcam to run
webcam = cv2.VideoCapture(0)

#iterate forever over frame
while True:
    #for reading current frame
    successful_frame_read, frame = webcam.read()


    #must include gray scale(image in black and white)
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detechting faces
    face_cordinates = traing_face_data.detectMultiScale(grayscale_img)

    # we actual use loop for it
    for (x, y, w, h) in face_cordinates:
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(128, 256), randrange(256), randrange(256)), 4)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0 , 0 , 255), 4)

    cv2.imshow('clever Programmer Face Detector', frame)
    key = cv2.waitKey(1)

    #stop if any presing any key
    if key == 81 or key == 113:
        break
#Release videocamp object
webcam.release()

"""
#Detechting faces
face_cordinates = traing_face_data.detectMultiScale(grayscale_img)

#draw the rectangle in side of face
#(x, y, w, h) = face_cordinates[0]
#we actual use loop for it
for (x, y, w, h) in face_cordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128,256), randrange(256), randrange(256)), 4)

#print face cordinate of image
#print(face_cordinates)


cv2.imshow('clever Programmer Face Detector',img)
cv2.waitKey()
print("Code Comppleted")
"""

