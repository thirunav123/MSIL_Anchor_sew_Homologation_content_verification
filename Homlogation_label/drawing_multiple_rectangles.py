import cv2,pytesseract,time
cap=cv2.VideoCapture(0)
buffersize=2
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_BUFFERSIZE,buffersize)
text="AAA"
frame=cv2.imread("/home/rane123/Desktop/s_im2.jpg")
x=
y=0
w=350
h=40
cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
cv2.rectangle(frame,(x,y),(x+w,y+23+h),(0,255,0))
cv2.rectangle(frame,(x,y),(x+w,y+46+h),(0,255,0))
cv2.rectangle(frame,(x,y),(x+w,y+69+h),(0,255,0))
cv2.rectangle(frame,(x,y),(x+w,y+92+h),(0,255,0))
cv2.rectangle(frame,(x,y),(x+w,y+115+h),(0,255,0))
# cv2.rectangle(frame,(x,y),(x+w,y+150+h),(0,255,0))
cv2.imshow("capture",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()