import cv2,pytesseract,time,datetime,snap7,PIL
cap=cv2.VideoCapture(0)
from PIL import Image
import PIL.ImageOps
from picamera import PiCamera
import PIL.ImageOps 
x=990
y=400
w=960
h=500
buffersize=1
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1944)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,2592)
cap.set(cv2.CAP_PROP_BUFFERSIZE,buffersize)
text="AAA"
date_line=5
model1_list=[]
file_text=open('model1.txt','r')
for fl in file_text:
    model1_list.append(fl.strip())
bypass_char_list=[]
exception_text=open('exception_lines.txt','r')
for el in exception_text:
    bypass_char_list.append(el.strip())
print(model1_list)
client=snap7.client.Client()
client.connect("10.73.14.21",0,1)
print(bool(client.get_connected))
plc_db_no=67
###camera = PiCamera()
###camera.resolution=(2592,1944)
def get_require_image():
    #start=time.perf_counter()
    ###camera.start_preview()
    ###im=camera.capture("/home/rane123/Desktop/msil3.jpg")
    ###camera.stop_preview()
    count=0
    while count<=buffersize:
        ret,frame=cap.read()
        count=count+1
        
    ###col = Image.open("/home/rane123/Desktop/msil3.jpg")
    #col = col.transpose(Image.ROTATE_180)
#     x=770
#     y=600
#     w=700
#     h=380
    ###col = col.crop((x,y,x+w,y+h))
    ###col = col.transpose(Image.ROTATE_180)
    ###invert_image=PIL.ImageOps.invert(col)
    ###invert_image=invert_image .rotate(1)
    #frame=cv2.imread("/home/rane123/Desktop/msil3.jpg")
    #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    img=frame[y:y+h,x:x+w]
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #img=cv2.resize(img,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
    img=cv2.rotate(img,cv2.ROTATE_180)
    #img=cv2.Canny(img,100,200)
    #img=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    img=cv2.medianBlur(img,7)
    img=cv2.bitwise_not(img)
    
    #img=cv2.resize(crop_img_rotated,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
    #img=cv2.medianBlur(img,5)
    #img=cv2.bitwise_not(img)

    #cv2.imshow("capture",cv2.resize(frame,(800,600)))
    #pytesseract.clear()
#     return img
    #end=time.perf_counter()
    #print(cap.get(3),cap.get(4),end-start)
    #c=round(time.time())
    cv2.imwrite(f"/home/rane123/Desktop/f_im03.jpg",frame)
    a=0
    b=0
    w1=340
    s=23
    lh=24
    #for i in range(6):
     #   cv2.rectangle(img,(a,b),(a+w1,b+s+(lh*i)),(0,0,0),1)
    cv2.imwrite("/home/rane123/Desktop/s_im03.jpg",img)
    #frame=cv2.imread("/home/rane123/Desktop/s_im.jpg")
    #col = Image.open("/home/rane123/Desktop/s_im.jpg")
    #invert_image=PIL.ImageOps.invert(col)
#     return img
    ###invert_image.save("/home/rane123/Desktop/bw.jpg") 
    ###return invert_image
    return img

def validate_date(d,df):
    try:
        datetime.datetime.strptime(d,df)
        return True
    except Exception as e:
        print(e)
        return False
    
def get_text_result(image,model):
#     cv2.imshow("capture",cv2.resize(image,(800,600)))
#     cv2.waitKey(0)
    cc=r'-c tessedit_char_blacklist=abcdefghij!._klmnopqrstuvwxyz --psm 6 --oem 3'
    lable_text=pytesseract.image_to_string(image,config=cc)
    result_list=[]
    for i in range(len(model1_list)):
        result_list.append(False)
    cl=0
    
    #print(lable_text)
    label_text_list=[]
    for ll in lable_text.splitlines():
        lt=ll.strip()
        if lt!='':
            label_text_list.append(lt)
    flag=False
    bypass_char_flag=False
    index_list=[]
    cl=0
    l_ml=len(model1_list)
    for i in label_text_list:
        if i==model1_list[0]:
            flag=True
        if flag:
            if cl!=date_line: 
                if i==model1_list[cl]:
                    result_list[cl]=True
            else:
                result_list[cl]=validate_date(i,model1_list[cl].strip())
                
            if i in bypass_char_list:
                result_list[cl]=True
                bypass_char_flag=True
                index_list.append(bypass_char_list.index(i))
            print(i,model1_list[cl])
            cl=cl+1
            if cl==l_ml:
                break
            
#     for ll in lable_text.splitlines():
#         lt=ll.strip()
#         #print("t:",lt)
#         #print(lt==model1_list[0].strip())
#         if lt!='' and lt==model1_list[0].strip():
#             for lt in model1_list:
#                 
#                 #print(i)
#                 #print(i,cl)
#                 if i==cl:
#                     if i!=date_line:
#                         #print(lt,fl)
#                         if lt==fl.strip():
#                             #print(f"Line {i} same")
#                             result_list[i]=True
#                         else:
#                             #print(f"Line {i} not same")
#                             result_list[i]=False
#                     else:
# #                         print(ll)
# #                         ll="MEG :30/09/2022"
#                         #print(lt,fl)
#                         result_list[i]=validate_date(ll,fl.strip())
#             cl=cl+1
    print(result_list,index_list)
    if bypass_char_flag:
        with open("bypass_char_ok_file.txt","a") as f:
            f.write(lable_text)
            for i in index_list:
                f.write(f" el{i}")
            print("exceptional")        
    elif all(result_list):
        with open("ok_file.txt","a") as f:
            f.write(lable_text)
            
    else:
        with open("nok_file.txt","a") as f:
            f.write(lable_text)
    return all(result_list)

def plc_communication():
    while True:
        data=client.db_read(plc_db_no,0,1)
        model=client.db_read(plc_db_no,2,256)
        model=model[2:2+model[1]].decode()
        model=model.replace(" ","")
        print(model)
        plc_db_no
        #i="0"
        #i=input(" start: ")
        if snap7.util.get_bool(data,0,0):# or i=="1":
            start=time.perf_counter()
            snap7.util.set_bool(data,0,0,False)
            img=get_require_image()
            result=get_text_result(img,model)
            if result:
                #snap7.util.set_bool(data,0,1,True)
                print("label_text_ok")
            else:
                #snap7.util.set_bool(data,0,2,True)
                print("label_text_Nok")
            client.db_write(plc_db_no,0,data)
            end=time.perf_counter()
            print(round((end-start)*1000) ,"ms")
        time.sleep(.05)
plc_communication()

