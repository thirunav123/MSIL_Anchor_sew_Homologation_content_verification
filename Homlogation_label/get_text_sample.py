import cv2,pytesseract,time
cap=cv2.VideoCapture(0)
x=570
y=385
w=350
h=180
buffersize=3
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_BUFFERSIZE,buffersize)
text="AAA"

def get_image():
    count=0
    while True:
        start=time.perf_counter()
        ret,frame=cap.read()
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        crop_img=frame[y:y+h,x:x+w]
        crop_img_rotated=cv2.rotate(crop_img,cv2.ROTATE_180)
        if cv2.waitKey(1) and 0xFF ==ord('q'):
            break
        img=cv2.medianBlur(crop_img_rotated,1)

        img=cv2.bitwise_not(crop_img_rotated)
        #img=cv2.threshold(img,50,255,cv2.THRESH_BINARY)[1]
        cv2.imshow("capture",cv2.resize(frame,(800,600)))
        #pytesseract.clear()
        text=pytesseract.image_to_string(img)
        
        cv2.imwrite("/home/rane123/Desktop/s_im.jpg",img)
        cv2.imwrite("/home/rane123/Desktop/f_im.jpg",frame)
        if count>2:
            break
        #count=count+1
        print("Text:",text)
        end=time.perf_counter()
        print(cap.get(3),cap.get(4),end-start)
        
def ocr_core(img):
    text=pytesseract.image_to_string(img)
    return text

def get_gray_scale(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def remove_noise(img):
    return cv2.medianBlur(img,1)

def thresholding(img):
    return cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
        





def remove_noise(img):
    return cv2.medianBlur(img,1)

def find_text():
    img=cv2.imread("/home/rane123/Desktop/s_im.jpg")
    img=cv2.medianBlur(img,1)
    text=pytesseract.image_to_string(img,lang='eng')
    print(pytesseract.get_languages())
    print(text)
    

get_image()
cv2.destroyAllWindows()
#find_text()