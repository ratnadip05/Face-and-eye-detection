import cv2
import  numpy as np
import  matplotlib.pyplot as plt



face_detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_face(img):
    face_img = img.copy()

    face_rectangle = face_cascade.detectMultiScale(face_img)

    for (x,y,w,h) in face_rectangle:
        cv2.rectangle(face_img,(x,y),(x+w, y + h),(255,255,255),10)
    return face_img

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(3) & 0xff==27:
        break
cap.release()
cv2.distroyAllWindows()
