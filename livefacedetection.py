import cv2  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
cap = cv2.VideoCapture(0) 
while 1:
    ret, img = cap.read()
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,205,180),2)  
        roi_color = img[y:y+h, x:x+w]
    cv2.imshow('image',img) 
   
    if cv2.waitKey(50) == ord('a'): 
        break
cap.release() 
cv2.destroyAllWindows()  
