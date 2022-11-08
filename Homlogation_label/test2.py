from PIL import Image
import pytesseract

def text_extraction():
    global flag1,flag2
    while True:
                a=input()
                invert_image=Image.open("/home/rane123/Desktop/bw.jpg")
                rot_img = invert_image.transpose(Image.ROTATE_180)
                #rot_img.show()
                croppedIm2 = rot_img.crop((800,1680, 3000,2500))
                #croppedIm2.show()
                rot_img1 = croppedIm2 .rotate(354)
                #rot_img1.show()
                croppedIm3= rot_img1.crop((50,50, 1800,640))
                croppedIm3.show()
                croppedIm4= rot_img1.crop((250,620, 1800,720))
                croppedIm4.show()
                text2= pytesseract.image_to_string(croppedIm3,config='')
                print (text2)
                text3= pytesseract.image_to_string(croppedIm4,config='')
                print (text3)

            #f="/home/rane123/out.txt"
           
            
            #with open(f) as f_obj:
            #    name=f_obj.read()
            #    print(name)
text_extraction()