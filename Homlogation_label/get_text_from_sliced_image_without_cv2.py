import cv2,pytesseract,time,datetime
from PIL import Image
x=0
y=0
w=350
h=40
lh=23
frame=Image.open("/home/rane123/Desktop/s_im2.jpg")
# crop_img=frame[y:y+h,x:x+w]
s=time.perf_counter()
ci=frame.crop((0,10,350,40))
lable_text=pytesseract.image_to_string(ci)
# ci.show()
print(lable_text)
lable_text=pytesseract.image_to_string(ci)#,config=r'--oem 3 --psm 6 ')#-c tessedit_char_whitelist= 0123456789:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
ci=frame.crop((0,40,350,115))
ci.show()
lable_text=pytesseract.image_to_string(ci)
ci=frame.crop((0,115,350,170))
ci.show()
print(lable_text)
lable_text=pytesseract.image_to_string(ci)
# ci.show()
print(lable_text)
e=time.perf_counter()
print(e-s)