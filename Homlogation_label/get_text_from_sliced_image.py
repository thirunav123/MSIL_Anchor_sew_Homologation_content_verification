import cv2,pytesseract,time,datetime
x=0
y=0
w=350
h=40
lh=23
frame=cv2.imread("/home/rane123/Desktop/s_im2.jpg")
# crop_img=frame[y:y+h,x:x+w]
s=time.perf_counter()
for i in range(6):
    cv2.rectangle(frame,(x,y),(x+w,y+h+(lh*i)),(0,0,0))
    crop_img=frame[y+17+lh*i:y+h+(lh*i),x:x+w]
#     cv2.imshow("im",crop_img)
#     cv2.waitKey(0)
    lable_text=pytesseract.image_to_string(crop_img)#,config=r'--oem 3 --psm 6 ')#-c tessedit_char_whitelist= 0123456789:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(lable_text)
e=time.perf_counter()
print(e-s)
# cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
# cv2.rectangle(frame,(x,y),(x+w,y+23+h),(0,255,0))
# cv2.rectangle(frame,(x,y),(x+w,y+46+h),(0,255,0))
# cv2.rectangle(frame,(x,y),(x+w,y+69+h),(0,255,0))
# cv2.rectangle(frame,(x,y),(x+w,y+92+h),(0,255,0))
# cv2.rectangle(frame,(x,y),(x+w,y+115+h),(0,255,0))
cv2.imshow("im",frame)
cv2.waitKey(0)
# lable_text=pytesseract.image_to_string(image,config=r'--oem 3 --psm 6 ')#-c tessedit_char_whitelist= 0123456789:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
# result_list=[]