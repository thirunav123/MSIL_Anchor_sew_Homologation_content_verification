import cv2,pytesseract,time
cap=cv2.VideoCapture(0)
# x=1000
# y=400
# w=950
# h=500
# buffersize=2
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1944)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,2592)
x=450
y=50
w=530
h=270
buffersize=1
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_BUFFERSIZE,buffersize)
text="AAA"

while True:
    start=time.perf_counter()
    ret,frame=cap.read()
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("capture",cv2.resize(frame,(800,600)))
    if cv2.waitKey(1) and 0xFF ==ord('q'):
        break
    print(cap.get(3),cap.get(4))
    
cv2.destroyAllWindows()
#find_text()
