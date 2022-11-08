#import snap7
#from snap7.types import *
from PIL import Image
#from difflib import SequenceMatcher
from picamera import PiCamera
import PIL.ImageOps 
import pytesseract
from datetime import date
#client=snap7.client.Client()
#client.connect("192.168.0.1",0,1,102)
#print(bool(client.g
#print(c)
#print("afterchange:")
#count=1
#b=client.db_write(1,0,b'\x00')
#data1=client.db_read(1,0,1)
#print(data1)
#today=date.today()
#print("date is:",today)
#d1=today.strftime("%d/%m/%Y")
#a=print("DATE OF MFG :",d1)
#a=print("DATE OF MFG :",d1)
#if c==False:
# from picamera import PiCamera
# from PIL import Image
# import PIL.ImageOps,pytesseract
camera = PiCamera()
camera.resolution=(2592,1944)
x=1550
y=1200
w=1250
h=1250

    #camera.resolution=(500,500)
    #camera.start_preview()
#sleep(1)
img=camera.capture("/home/rane123/Desktop/msil3.jpg")
    #print("Done.")
    #camera.stop_preview()
col = Image.open("/home/rane123/Desktop/msil3.jpg")
invert_image=PIL.ImageOps.invert(col)
#bw = gray.point(lambda x: 0 if x<128 else 255, '1')
invert_image.save("/home/rane123/Desktop/bw.jpg")
im2=Image.open("/home/rane123/Desktop/bw.jpg")
#rot_img = invert_image.transpose(Image.ROTATE_180)
    #rot_img.show()
croppedIm2 = invert_image.crop((x,y,x+w,y+h))
rot_img = croppedIm2.transpose(Image.ROTATE_180)
rot_img.save("/home/rane123/Desktop/bw4.jpg")
rot_img.show()
#rot_img1 = croppedIm2 .rotate(354)
    #rot_img1.show()
#croppedIm3= rot_img1.crop((50,50, 1800,640))
#diosdplecroppedIm3.show()
#croppedIm4= rot_img1.crop((250,620, 1800,720))
#croppedIm4.show()
text= pytesseract.image_to_string(rot_img,config='')
print (text)
#text3= pytesseract.image_to_string(croppedIm4,config='')
#print (text3)

#print("Before change:")
#data1=client.db_read(1,0,1)
#b=snap7.util.set_bool(data1,0,0,False)
#c=snap7.util.get_bool(data1,0,0)
#print(data1)#
    
f="/home/rane123/out.txt"
   
    
# with open(f) as f_obj:
#     name=f_obj.read()
#     print(name)
# if text2 in name:
#     print("identical")
# else:
#     print("not identical")
# 
# if a==text3:
#     print("ok")
#else:
#print("nok")