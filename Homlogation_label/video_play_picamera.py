from picamera import PiCamera
from PIL import Image
import PIL.ImageOps,pytesseract
camera = PiCamera()
camera.resolution=(2592,1944)
#camera.resolution=(500,500)
while True:
    camera.start_preview()
    im=camera.capture("/home/rane123/Desktop/msil3.jpg")
    camera.stop_preview()
    
    col = Image.open("/home/rane123/Desktop/msil3.jpg")
    col = col.transpose(Image.ROTATE_180)
    x=770
    y=600
    w=700
    h=380
    col = col.crop((x,y,x+w,y+h))
    invert_image=PIL.ImageOps.invert(col)
    invert_image=invert_image .rotate(2)
    invert_image.show()
    invert_image.save("/home/rane123/Desktop/bwc.jpg")
    text= pytesseract.image_to_string(invert_image,config='')
    print (text)
    break
#camera.start_preview()
