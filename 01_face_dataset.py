import cv2
import os

cam= cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input('\n Silahkan masukkan user nama-angle(kanan,kiri,atas,bawah), kemudian enter: ')

print("\n [INFO] Kamera sedang menganalisa wajah anda")

count = 0
img_count = 0

while(True):

    ret, img = cam.read()   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 4)

    for (x,y,w,h) in faces:
        
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1
        img_count += 1
        
        img_name = "{}_{:04d}.jpg".format(face_id, img_count)
        cv2.imwrite("D:/deteksimuka-dataset/dataset/" + img_name, gray[y:y+h,x:x+w])
        
        cv2.imshow('image',img)
        
        k = cv2.waitKey(10) & 0xff
        
        if k == 27:
            print("Esc key pressed. Exiting...")
            break

    if count >= 50:
        print("50 images captured. Exiting...")
        break
        

print("\n Analisa Selesai")
cam.release()
cv2.destroyAllWindows()
