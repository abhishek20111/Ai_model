import cv2
from random import randrange
import win32com.client

def speech(str):
    speak = win32com.client.Dispatch("SAPI.SpVoice")
    speak.speak(str)


training_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')


#speech("hi buddy how are you")
webcam = cv2.VideoCapture(0)
#speech("this software will detect smile on your face .")
#speech("If it show green box in your smile then your smile is awesome")
while True:
    successful_frame_read, frame = webcam.read()

    #if there is an error(or it start reading any video it break from loop)
    if not successful_frame_read:
        break

    #must include gray scale(image in black and white)
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detechting faces
    face_cordinates = training_face_data.detectMultiScale(grayscale_img)


    # we actual use loop for it
    for (x, y, w, h) in face_cordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0 , 0 , 255), 4)

        #it make the cordnate limited for program to search it only give cordinate in face (in last it use nupy 2D)
        the_faces = frame[y:y+h, x:x+w]

        # convert the_face in gray image
        face_Graycale_img = cv2.cvtColor(the_faces, cv2.COLOR_BGR2GRAY)

        smile_cordinates = smile_detector.detectMultiScale(face_Graycale_img, scaleFactor=1.7, minNeighbors=13)

        #it check smile in faces
        #for (x1, y1, w1, h1) in smile_cordinates:
            #cv2.rectangle(the_faces, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 3)

        # Lable this face as smiling
        if len(smile_cordinates) >0:
            cv2.putText(frame, 'smiling', (x, y+h+40), fontScale =3, fontFace = cv2.FONT_HERSHEY_PLAIN, color = (255, 255, 255))


    cv2.imshow('Smile detector', frame)
    key = cv2.waitKey(1)

    # stop if any presing any key
    if key == 81 or key == 113:
        break

webcam.release()
cv2.destroyAllWindows()



# while True:
#     #for reading current frame
#     successful_frame_read, frame = webcam.read()

    #
    # #must include gray scale(image in black and white)
    # grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #
    # # Detechting faces
    # face_cordinates = training_face_data.detectMultiScale(grayscale_img)
    #
    # # we actual use loop for it
    # for (x, y, w, h) in face_cordinates:
    #     #cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(128, 256), randrange(256), randrange(256)), 4)
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0 , 0 , 255), 4)

    # cv2.imshow('clever Programmer Face Detector', frame)
    # key = cv2.waitKey(1)

    #stop if any presing any key
    # if key == 81 or key == 113:
    #     break
# #Release videocamp object
# webcam.release()