import cv2
face_cascade = cv2.CascadeClassifier("C:/Users/donny/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:/Users/donny/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_eye.xml")

video = cv2.VideoCapture(0)

while{True}:
    ret,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x +w, y+ h), (0,255,0), 2)
        
    cv2.imshow("frame", frame)
    if(cv2.waitKey(25) == 32):
        break

video.release()
cv2.destroyAllWindows()