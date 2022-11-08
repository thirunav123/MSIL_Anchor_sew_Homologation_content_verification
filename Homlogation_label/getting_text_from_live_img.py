import cv2,pytesseract,PIL.ImageOps,time
from picamera import PiCamera
#cv2.CAP_PROP_BUFFERSIZE=1
buffersize=1
h=3040
w=4056
h=3000
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE,buffersize)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,2400)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,2800)
print(cap.get(cv2.CAP_PROP_BUFFERSIZE))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
x=1600
y=1200
w=1250
h=700
flag=True
while True:
    count=0
    #while count<buffersize+2:
    ret,frame=cap.read()
        #if ret:
    count=count+1
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    #print(cap.get(3),cap.get(4))
    cv2.imshow("capture",frame)
    #crop_img=frame[y:y+h,x:x+w]
    #crop_img_rotated=cv2.rotate(crop_img,cv2.ROTATE_180)
    #invert_image=cv2.bitwise_not(crop_img_rotated)
    #crop_img=cv2.rotate(crop_img,cv2.ROTATE_180)
    #crop_img_gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    #(thresh, blackAndWhiteImage) = cv2.threshold(crop_img_gray, 25, 255, cv2.THRESH_BINARY)
    #cv2.imshow("capture",cv2.resize(invert_image,(800,600)))
    #if a=="s":
    if flag:
        cv2.imwrite("/home/rane123/Desktop/inv_im.jpg",frame)
        flag=False
    #text=pytesseract.image_to_string(invert_image,config='')
    #print("Text:",text)
    #cv2.imshow("capture",frame)
    if cv2.waitKey(1) and 0xFF ==ord('q'):
        break
    #time.sleep(.1)
#cap.release()
#cv2.destroyAllWindows()