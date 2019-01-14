import cv2
import numpy as np
import sqlite3


recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)

while True:
    ret, im =cam.read()
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        conn = sqlite3.connect('student.db')
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf <=60):
            if(Id==1):
                 
                ATT="YES"
                IDD=2
                Id="Danyson"
                conn.execute("UPDATE  STUDENT_DET  SET  ATTENDANCE= ?  WHERE  reg_no= ?", (ATT, IDD))
                Id="sakthi"
              
        if(conf <=60):
            if(Id==2):
             ATT="YES"
             IDD=1
             Id="Danyson"
             conn.execute("UPDATE  STUDENT_DET  SET  ATTENDANCE= ?  WHERE  reg_no= ?", (ATT, IDD))
        
        else:
            Id=Id

        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id) , (x,y-40), font, 2, (255,255,255), 3)
        conn.commit()
        conn.close()
    cv2.imshow('im',im)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
