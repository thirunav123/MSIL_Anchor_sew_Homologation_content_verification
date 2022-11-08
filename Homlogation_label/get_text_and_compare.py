import cv2,pytesseract,time,datetime,snap7,PIL
#cap=cv2.VideoCapture(0)
from PIL import Image
import PIL.ImageOps
from picamera import PiCamera
import PIL.ImageOps 
x=800
y=600
w=700
h=380
buffersize=2
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
#cap.set(cv2.CAP_PROP_BUFFERSIZE,buffersize)
text="AAA"
model1_list=[]
file_text=open('model1.txt','r')
date_line=5
for fl in file_text:
    model1_list.append(fl)

client=snap7.client.Client()
client.connect("10.73.14.21",0,1)
print(bool(client.get_connected))
plc_db_no=67
camera = PiCamera()
camera.resolution=(2592,1944)
def get_require_image():
    start=time.perf_counter()
    camera.start_preview()
    im=camera.capture("/home/rane123/Desktop/msil3.jpg")
    camera.stop_preview()
    #ret,frame=cap.read()
    col = Image.open("/home/rane123/Desktop/msil3.jpg")
    col = col.transpose(Image.ROTATE_180)
    x=770
    y=600
    w=700
    h=380
    col = col.crop((x,y,x+w,y+h))
    invert_image=PIL.ImageOps.invert(col)
    invert_image=invert_image .rotate(2)
    #frame=cv2.imread("/home/rane123/Desktop/msil3.jpg")
    #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    #crop_img_rotated=cv2.rotate(frame,cv2.ROTATE_180)
    #crop_img_rotated=crop_img_rotated[y:y+h,x:x+w]

    #img=cv2.medianBlur(crop_img_rotated,3)
    #img=cv2.bitwise_not(crop_img_rotated)
    #img=cv2.threshold(crop_img_rotated,80,255,cv2.THRESH_BINARY)[1]
    #img=cv2.resize(crop_img_rotated,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
    #img=cv2.medianBlur(img,5)
    #img=cv2.bitwise_not(img)

    #cv2.imshow("capture",cv2.resize(frame,(800,600)))
    #pytesseract.clear()
#     return img
    #end=time.perf_counter()
    #print(cap.get(3),cap.get(4),end-start)
    #c=round(time.time())
    #cv2.imwrite(f"/home/rane123/Desktop/f_im.jpg",frame)
    a=0
    b=0
    w1=340
    s=23
    lh=24
    #for i in range(6):
     #   cv2.rectangle(img,(a,b),(a+w1,b+s+(lh*i)),(0,0,0),1)
    #cv2.imwrite("/home/rane123/Desktop/s_im.jpg",img)
    #frame=cv2.imread("/home/rane123/Desktop/s_im.jpg")
    #col = Image.open("/home/rane123/Desktop/s_im.jpg")
    #invert_image=PIL.ImageOps.invert(col)
#     return img
    return invert_image

def validate_date(d,df):
    try:
        datetime.datetime.strptime(d,df)
        return True
    except Exception as e:
        #print(e)
        return False
    
def get_text_result(image,model):
#     cv2.imshow("capture",cv2.resize(image,(800,600)))
#     cv2.waitKey(0)
    lable_text=pytesseract.image_to_string(image,config=r'--oem 3 --psm 6')# -c tessedit_char_whitelist= 0123456789:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result_list=[]
    for i in range(len(model1_list)):
        result_list.append(False)
    cl=0
    print(lable_text)
    for ll in lable_text.splitlines():
        lt=ll.strip()
        #print("t:",lt)
        print(lt==model1_list[0].strip())
        if lt!='' and lt==model1_list[0].strip():
            for i,fl in enumerate(model1_list):
                #print(i)
                #print(i,cl)
                if i==cl:
                    if i!=date_line:
                        #print(lt,fl)
                        if lt==fl.strip():
                            #print(f"Line {i} same")
                            result_list[i]=True
                        else:
                            #print(f"Line {i} not same")
                            result_list[i]=False
                    else:
#                         print(ll)
#                         ll="MEG :30/09/2022"
                        #print(lt,fl)
                        result_list[i]=validate_date(ll,fl.strip())
            cl=cl+1
    print(result_list)
    return all(result_list)

def plc_communication():
    while True:
        data=client.db_read(plc_db_no,0,1)
        model=client.db_read(plc_db_no,0,1)
        #i="0"
        i=input(" start: ")
        if snap7.util.get_bool(data,0,0) or i=="1":
            start=time.perf_counter()
            snap7.util.set_bool(data,0,0,False)
            img=get_require_image()
            result=get_text_result(img,model)
            if result:
                snap7.util.set_bool(data,0,1,True)
                print("label_text_ok")
            else:
                snap7.util.set_bool(data,0,2,True)
                print("label_text_Nok")
            #client.db_write(plc_db_no,0,data)
            end=time.perf_counter()
            print(round((end-start)*1000) ,"ms")
        time.sleep(.1)
plc_communication()
