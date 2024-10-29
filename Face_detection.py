import cv2
alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)#Syntax for importing the Haar Cascade algorithm ,It is different fir the different packages
cam = cv2.VideoCapture(0)# for capturing the video
while True:
    _,img =cam.read() #for reading the video
    grayImg =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # for converting the color to the grayscale image 
    face = haar_cascade.detectMultiScale(grayImg,1.3,4) # the syntax for detecting the multiple faces and we also oincluded the xml file within the variable
                                                        #also search and examine the algorithm for the another faces
    for (x,y,w,h) in face:
        cv2.rectangle(img ,(x,y),(x+w,y+h),(0,255,255),4)
    if len(face) == 0:
        text = "No Face Detected"
        print(text)
        cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        cv2.imshow('face detection',img)
        key = cv2.waitKey(10)
        if key == 27:
            break
    elif len(face) == 1:
        text ="Face Detected"
        print(text)
        cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow('face detection',img)
        key = cv2.waitKey(10)
        if key == 27:
            break
cam.release()
cv2.destroyAllWindows()