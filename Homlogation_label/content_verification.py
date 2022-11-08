import cv2,pytesseract,PIL.ImageOps,time
from picamera import PiCamera
#cv2.CAP_PROP_BUFFERSIZE=1
#buffersize=1
#cap=cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_BUFFERSIZE,buffersize)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,3040)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,4056)
#print(cap.get(cv2.CAP_PROP_BUFFERSIZE))
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
x=1600
y=1200
w=1250
h=700
camera = PiCamera()
#camera.stop_preview()
#camera.start_preview()
#time.sleep(8)
camera.resolution=(4056,3040)

while True:
    #a=input()
    count=0
    #while count<buffersize+2:
    #    ret,frame=cap.read()
        #if ret:
     #   count=count+1
    camera.capture("/home/rane123/Desktop/msil4.jpg")
    frame=cv2.imread("/home/rane123/Desktop/msil4.jpg")
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    #print(cap.get(3),cap.get(4))
    #cv2.imshow("capture",cv2.resize(frame,(800,600)))
    crop_img=frame[y:y+h,x:x+w]
    crop_img_rotated=cv2.rotate(crop_img,cv2.ROTATE_180)
    invert_image=cv2.bitwise_not(crop_img_rotated)
    crop_img=cv2.rotate(crop_img,cv2.ROTATE_180)
    crop_img_gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    #(thresh, blackAndWhiteImage) = cv2.threshold(crop_img_gray, 25, 255, cv2.THRESH_BINARY)
    #cv2.imshow("capture",cv2.resize(invert_image,(800,600)))
    #if a=="s":
    cv2.imwrite("/home/rane123/Desktop/inv_im.jpg",invert_image)
    text=pytesseract.image_to_string(invert_image,config='')
    print("Text:",text)
    #cv2.imshow("capture",frame)
    cv2.waitKey(0) #& 0xFF ==ord('q'):
    #   break
    #time.sleep(.1)
#cap.release()
#cv2.destroyAllWindows()