import cv2
import sys
import numpy as np
#from matplotlib import pyplot as plt

#키넥트 카메라 작동
image = cv2.VideoCapture(0)

 # 카메라가 열렸는지 확인
if not image.isOpened():
    print("Camera open failed!") # 열리지 않았으면 문자열 출력
    sys.exit()
    
#객체 생성 및 학습데이터 불러오기, 전신 검출 xml파일
filename = 'haarcascade_fullbody.xml'
body_cascade = cv2.CascadeClassifier(filename)

if body_cascade.empty():
    print('XML load failed!')
    sys.exit()
    
while True:
    ret, frame = image.read()
    
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    body = body_cascade.detectMultiScale(gray, 1.1, 2, 0, minSize=(70,70))
    
    for (x,y,w,h) in body:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    
    
    cv2.imshow('video', frame)
    
    #키보드 입력을 받기 위해서 대기시간 1초 줌 
    if cv2.waitKey(1)&0xFF == 27: 
        break

image.release()
cv2.destroyAllWindows()