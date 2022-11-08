import cv2,pytesseract,time,datetime
x=0
y=0
w=330
h=20
lh=23
frame=cv2.imread("/home/rane123/Desktop/s_im.jpg")
# crop_img=frame[y:y+h,x:x+w]
frame=cv2.medianBlur(frame,1)
s=time.perf_counter()
for i in range(6):
    cv2.rectangle(frame,(x,y),(x+w,y+h+(lh*i)),(0,0,0),1)
    crop_img=frame[y+17+lh*i:y+h+(lh*i),x:x+w]
#     cv2.imshow("im",crop_img)
#     cv2.waitKey(0)
lable_text=pytesseract.image_to_string(frame[y:y+h+(lh*i),x:x+w],config=r'--oem 3 --psm 6 -c tessedit_char_whitelist= 0I123456789:abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ')
print(lable_text)
e=time.perf_counter()
print(e-s)
# cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
# cv2.rectangle(frame,(x,y),(x+w,y+23+h),(0,255,0))
# cv2.rectangle(frame,(x,y),(x+w,y+46+h),(0,255,0))
# cv2.rectangle(frame,(x,y),(x+w,y+69+h),(0,255,0))
# cv2.rectangle(frame,(x,y),(x+w,y+92+h),(0,255,0))
# cv2.rectangle(frame,(x,y),(x+w,y+115+h),(0,255,0))
cv2.imshow("im",frame[y:y+h+(lh*i),x:x+w])
cv2.waitKey(0)
# lable_text=pytesseract.image_to_string(image,config=r'--oem 3 --psm 6 ')#-c tessedit_char_whitelist= 0123456789:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
# result_list=[]