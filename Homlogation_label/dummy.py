# # import cv2,pytesseract,time
# # from PIL import Image
# # import PIL.ImageOps
# # frame=Image.open("/home/rane123/Desktop/f_im1667397487.jpg")
# # x=555
# # y=350
# # w=350
# # h=160
# # invert_image=PIL.ImageOps.invert(frame)
# # croppedIm2 = invert_image.crop((x,y, x+w,y+(h/2)))
# # croppedIm2 = croppedIm2 .rotate(2)
# # rot_img2 = croppedIm2.transpose(Image.ROTATE_180)
# # rot_img2.show()
# # 
# # croppedIm3 = invert_image.crop((x,y+(h/2), x+w,y+h))
# # rot_img3 = croppedIm3.transpose(Image.ROTATE_180)
# # croppedIm3 = croppedIm3 .rotate(2)
# # rot_img3.show()
# # # rot_img1 = croppedIm2 .rotate(354)
# # # rot_img1.show()
# # text2= pytesseract.image_to_string(rot_img2,config='')
# # print (text2)
# # text3= pytesseract.image_to_string(rot_img3,config='')
# # print (text3)
# #
# import cv2,pytesseract,time
# cap=cv2.VideoCapture(0)
# x=770
# y=600
# w=700
# h=380
# pw,ph=2592,1944
# buffersize=2
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,ph)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,pw)
# cap.set(cv2.CAP_PROP_BUFFERSIZE,buffersize)
# text="AAA"
# 
# while True:
#     start=time.perf_counter()
#     ret,frame=cap.read()
#     frame=cv2.rotate(frame,cv2.ROTATE_180)
#     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#     cv2.imshow("capture",cv2.resize(frame,(800,600)))
#     if cv2.waitKey(1) and 0xFF ==ord('q'):
#         break
#     print(cap.get(3),cap.get(4))
#     
# cv2.destroyAllWindows()
# #find_text()
# 
#
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
buffersize=2
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_BUFFERSIZE,buffersize)
text="AAA"

while True:
    #input()
    c=0
    while c<=buffersize:
        ret,frame=cap.read()
        c=c+1
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("capture",cv2.resize(frame,(800,600)))
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
#find_text()

