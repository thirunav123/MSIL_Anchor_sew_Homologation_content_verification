import cv2,pytesseract,time,datetime,snap7

from PIL import Image
import PIL.ImageOps
from picamera import PiCamera


model_list=["028009300","028009400"]
date_line_list=[5,5]
model_dic={}
for index_i,i in enumerate(model_list):
    file_text=open(f'{i}.txt','r')
    temp_list=[]
    for fl in file_text:
        temp_list.append(fl.strip().replace(" ",""))
    file_text=open(f'exception_{i}.txt','r')
    temp_list_e=[]
    for fl in file_text:
        temp_list_e.append(fl.strip().replace(" ",""))
    model_dic[i]=[date_line_list[index_i],temp_list,temp_list_e]
#print(model_dic)
client=snap7.client.Client()
client.connect("10.73.14.21",0,1)
print(bool(client.get_connected))
plc_db_no=67

cap=cv2.VideoCapture(0)

x=450
y=50
w=530
h=270
buffersize=1
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_BUFFERSIZE,buffersize)

# x=1000
# y=400
# w=950
# h=500
# buffersize=1
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1944)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,2592)
# cap.set(cv2.CAP_PROP_BUFFERSIZE,buffersize)

# camera = PiCamera()
# camera.resolution=(2592,1944)

def get_require_image():
    count=0
    while count<=buffersize+1:
        ret,frame=cap.read()
        count=count+1
    img=frame[y:y+h,x:x+w]
    #img=cv2.fastNlMeansDenoisingColored(img,None,10,10,7,15)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #img=cv2.resize(img,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
    img=cv2.rotate(img,cv2.ROTATE_180)
    #img=cv2.Canny(img,100,200)
    #img=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    img=cv2.medianBlur(img,3)
    
    #img=cv2.GaussianBlur(img,(3,3),0)
    img=cv2.bitwise_not(img)
    #cv2.imwrite(f"/home/rane123/Desktop/f_im03.jpg",frame)
    cv2.imwrite("/home/rane123/Desktop/s_im03.jpg",img)
    return img

# def require_img_s():
#     camera.start_preview()
#     camera.capture("/home/rane123/Desktop/msil3.jpg")
#     camera.stop_preview()
#     col = Image.open("/home/rane123/Desktop/msil3.jpg")
#     col = col.crop((x,y,x+w,y+h))
#     col = col.transpose(Image.ROTATE_180)
#     invert_image=PIL.ImageOps.invert(col)
#     invert_image=invert_image .rotate(1)
#     invert_image.save("/home/rane123/Desktop/bw.jpg") 
#     return invert_image

def validate_date(d,df):
    try:
        datetime.datetime.strptime(d,df)
        return True
    except Exception as e:
        print(e)
        return False
    
def get_text_result(image,model):
    #cc=r"-c tessedit_char_blacklist=abcdefghij.,_klmnopqrstuvwxyz --oem 3 --psm 6"
    cc=r"-c tessedit_char_whitelist=ABCDEF0OGHIJKLMNPQRST:123456789-/ --oem 3 --psm 6"
    #cc=r"--oem 3 --psm 6"
    lable_text=pytesseract.image_to_string(image,config=cc)
    result_list=[]
    for i in range(len(model_dic[model][1])):
        result_list.append(False)
    cl=0
    lable_text_list=[]
    for ll in lable_text.splitlines():
        lt=ll.strip().replace(" ","")
        if lt!='':
            lable_text_list.append(lt)
    flag=False
    bypass_char_flag=False
    exceptional_index_list=[]
    exceptional_file_index_list=[]
    cl=0
    l_ml=len(model_dic[model][1])
    print(lable_text)
    for i in lable_text_list:
        if i==model_dic[model][1][0] or i in model_dic[model][2] :
            flag=True
        if flag:
            if cl!=model_dic[model][0]: 
                if i==model_dic[model][1][cl]:
                    result_list[cl]=True
                    #print(i,True)
            else:
                r=validate_date(i,model_dic[model][1][cl].strip())
                result_list[cl]=r
                print(i,r)
                
            if i in model_dic[model][2]:
                result_list[cl]=True
                bypass_char_flag=True
                exceptional_index_list.append(cl)
                exceptional_file_index_list.append(model_dic[model][2].index(i))
            #print(i,model_dic[model][1][cl])
            cl=cl+1
            if cl==l_ml:
                break
    print(result_list,exceptional_index_list,exceptional_file_index_list)
    if bypass_char_flag:
        with open(f"{model}_ok_with_exception.txt","a") as f:
            f.write(lable_text)
            for i,j in zip(exceptional_index_list,exceptional_file_index_list):
                f.write(f"\n ell{i} using efl{j} ")
            print("exceptional")        
    elif all(result_list):
        with open(f"{model}_ok.txt","a") as f:
            f.write(lable_text)
            
    else:
        with open(f"{model}_nok.txt","a") as f:
            f.write(lable_text)
    return all(result_list)

def plc_communication():
    tc,ok_c,nok_c,retry_ok_c=0,0,0,0
    while True:
        data=client.db_read(plc_db_no,0,1)
        plc_db_no
        #i="0"
        #i=input(" start: ")
        if snap7.util.get_bool(data,0,0):# or i=="1":
            start=time.perf_counter()
            snap7.util.set_bool(data,0,0,False)
            model=client.db_read(plc_db_no,2,256)
            model=model[2:2+model[1]].decode()
            model=model.replace(" ","")
            print("model:",model)
            img=get_require_image()
            #img=require_img_s()
            result=get_text_result(img,model)
            if result:
                ok_c=ok_c+1
                snap7.util.set_bool(data,0,1,True)
                print(f"{model}_lable_text_ok")
            else:
                #snap7.util.set_bool(data,0,2,True)
                print(f"{model}_lable_text_Nok")
                img=get_require_image()
                result=get_text_result(img,model)
                if result:
                    print(f"{model}_lable_text_retry_ok")
                    retry_ok_c=retry_ok_c+1
                else:
                    print(f"{model}_lable_text_Nok")
                    nok_c=nok_c+1   
                
            client.db_write(plc_db_no,0,data)
            end=time.perf_counter()
            tc=tc+1
            print(f"{round((end-start)*1000)}ms Total:{tc} Ok:{ok_c},Retry ok: {retry_ok_c},Nok:{nok_c}")
            
        time.sleep(.05)
plc_communication()

