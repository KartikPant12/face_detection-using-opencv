# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:32:17 2019

@author: kP
"""


import cv2
import numpy as np
from cv2 import *
#face_cascade = cv2.CascadeClassifier('D:\opencv\data\haarcascades\haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('C:\\Users\\kartik pant\\Desktop\\Master OpenCV\Haarcascades\\haarcascade_frontalface.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\kartik pant\\Desktop\\Master OpenCV\\Haarcascades\\haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
print(cap)
while True:
    ret,img = cap.read()
    #print(ret,img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #print('this is me',cap)
    #print(gray)
    faces = face_cascade.detectMultiScale(gray,2,6)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh)  in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,250,0),2)
    cv2.imshow('img',img) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        breakq
cap.release()
cv2.destroyAllWindows()