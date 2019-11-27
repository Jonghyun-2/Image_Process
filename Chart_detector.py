
#initialize
import pandas as pd
import cv2
import numpy as np
import glob
import pytesseract as OCR
import matplotlib.pyplot as plt

def onMouse(event,x,y,flags,params):
    global ix,iy,fx,fy
    global button_data
    global rect_mode,filter_mode
    global th_val
    buttonLoc()
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if (x in but1_x) & (y in but1_y):  
            print("Name button click")
            button_data= "Name func"
            
        elif (x in but2_x) & (y in but2_y): 
            print("Age button click")
            button_data = "Age func"
            
        elif (x in but3_x) & (y in but3_y):
            print("Disease button click")
            button_data = "Disease func"
            
        elif (x in but4_x) & (y in but4_y):
            print("symptom1 button click")
            button_data = "symptom1 func"
            
        elif (x in but5_x) & (y in but5_y):
            print("symptom2 button click")
            button_data = "symptom2 func"
            
        elif (x in but6_x) & (y in but6_y):
            print("symptom3 button click")
            button_data = "symptom3 func"
            
        elif (x in but7_x) & (y in but7_y):
            #이미지를 읽어온후 맨 처음 데이터를 읽어오는 모드
            global user_input_img,imgs_path,img_path
            img_path = input('Image path : ')
            imgs_path = glob.glob(img_path+"\\*.PNG")
            # 이미지 없을때 예외처리
            if len(imgs_path) <= 0:
                print("img not exist")
            for i in range(len(imgs_path)):
                print("Load img : " ,imgs_path[i])
            else:
                user_input_img = cv2.imread(imgs_path[0])
                # backgrnd에서 이미지의 영역을 570*480크기로 맞춰놨기 때문에 영상의 크기도 맞게 설정해놔야함
                user_input_img = cv2.resize(user_input_img,(570,480))
                user_input_img = cv2.cvtColor(user_input_img,cv2.COLOR_RGB2GRAY)
                backgrnd[120:600,270:840] = user_input_img
            
        elif (x in but8_x) & (y in but8_y):
            print("Otsu func")
            global otsu_img
            
            #이미지 일련처리를 할때 user가 otsu를 선택했는지 threshold값을 직접 지정했는지 보기위함
            filter_mode = "otsu"
            
            ret, otsu_img = cv2.threshold(user_input_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            backgrnd[120:600,270:840] = otsu_img
            
        elif (x in but9_x) & (y in but9_y):
            global user_th_img
            #이미지 일련처리를 할때 user가 otsu를 선택했는지 threshold값을 직접 지정했는지 보기위함 
            filter_mode = "th"
            user_threshold = int(input('Threshold : '))
            #이미지 일련처리를 할때 사용하기위한 threshold value
            th_val = user_threshold 
            ret, user_th_img = cv2.threshold(user_input_img, user_threshold, 255, cv2.THRESH_BINARY) #cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
            backgrnd[120:600,270:840] = user_th_img
            
#         elif (x in but10_x) & (y in but10_y):
#             #위의 신상정보들을 다 입력한 후 run버튼을 누르면 일련적으로 처리됨
#             print("Run func")
#             button_data = "run func"
            
#         elif (x in but11_x) & (y in but11_y):
#             print("?")
        else :
            print("out of box")
            
    if event == cv2.EVENT_RBUTTONDOWN:
        ix,iy = x,y
        print("start point : ",ix,iy,end = " : ")       

    elif event == cv2.EVENT_RBUTTONUP:
        fx,fy= x,y
        #마우스를 땠을경우 rect_mode를 true값으로 받아 영역을 캡처 하도록함
        rect_mode = True
        print("end point : ",fx,fy)
        cv2.rectangle(backgrnd,(ix,iy),(fx,fy),(100),2)

    return

def buttonLoc():
    global but1_x,but1_y,but2_x,but2_y,but3_x,but3_y,but4_x,but4_y,but5_x,but5_y,but6_x,but6_y,but7_x,but7_y,but8_x,but8_y,but9_x,but9_y,but10_x,but10_y
           
    # Name button
    but1_x = range(50,150) 
    but1_y = range(150,180)
    # Age button
    but2_x = range(50,150)
    but2_y = range(200,230)
    # Disease button
    but3_x = range(50,150)
    but3_y = range(250,280)    
      # symptom1 button
    but4_x = range(50,190)
    but4_y = range(300,330)  
      # symptom2 button
    but5_x = range(50,190)
    but5_y = range(350,380)  
      # symptom3 button
    but6_x = range(50,190)
    but6_y = range(400,430)  
      # image path
    but7_x = range(400,560)
    but7_y = range(10,40)  
       # threshold
    but8_x = range(350,450)
    but8_y = range(60,90)  
       # filtering
    but9_x = range(550,650)
    but9_y = range(60,90)  
       # run
#     but10_x = range(780,880)
#     but10_y = range(650,680)
#        # ?
#     but11_x = range(630,730)
#     but11_y = range(650,680)
    return
   
def putText(input_img):
    scale = 0.8
    font = 2
    cv2.putText(input_img,"Name",(but1_x[10],but1_y[-1]),font,scale,(0,0,0))
    cv2.putText(input_img,"Age",(but2_x[10],but2_y[-1]),font,scale,(0,0,0))
    cv2.putText(input_img,"Disease",(but3_x[5],but3_y[-1]),font,scale,(0,0,0))
    cv2.putText(input_img,"symptom1",(but4_x[5],but4_y[-1]),font,scale,(0,0,0))
    cv2.putText(input_img,"symptom2",(but5_x[5],but5_y[-1]),font,scale,(0,0,0))
    cv2.putText(input_img,"symptom3",(but6_x[5],but6_y[-1]),font,scale,(0,0,0))
    cv2.putText(input_img,"Image path",(but7_x[5],but7_y[-1]),font,scale,(0,0,0))
    cv2.putText(input_img,"Otsu",(but8_x[5],but8_y[-1]),font,scale,(0,0,0))
    cv2.putText(input_img,"Threshold",(but9_x[5],but9_y[-1]),font,scale,(0,0,0))
#     cv2.putText(input_img,"Run",(but10_x[25],but10_y[-1]),font,scale,(0,0,0))
#     cv2.putText(input_img,"?",(but11_x[25],but11_y[-1]),font,scale,(0,0,0))
    return input_img

def rec_draw():
    cv2.rectangle(backgrnd,(50,150),(150,180),(100),-1) #name
    cv2.rectangle(backgrnd,(50,200),(150,230),(100),-1) #Age
    cv2.rectangle(backgrnd,(50,250),(150,280),(100),-1) #Disease
    cv2.rectangle(backgrnd,(50,300),(190,330),(100),-1) #symptom1
    cv2.rectangle(backgrnd,(50,350),(190,380),(100),-1) #symptom2
    cv2.rectangle(backgrnd,(50,400),(190,430),(100),-1) #symptom3
    cv2.rectangle(backgrnd,(400,10),(560,40),(100),-1) #image path
    cv2.rectangle(backgrnd,(350,60),(450,90),(100),-1) #Otsu
    cv2.rectangle(backgrnd,(550,60),(670,90),(100),-1) #filtering
    #cv2.rectangle(backgrnd,(780,650),(880,680),(100),-1) #Run
    cv2.rectangle(backgrnd,(270,120),(840,600),(100),-1) #image place
    # cv2.rectangle(backgrnd,(580,120),(840,450),(150,150,150),-1) #list place
    return
#ocr을 통한 데이터와 dataframe을 파라미터로 전달받아 각자 name, age 등의 정보를 입력
#맨처음의 정보를 받을때
def getData(OCR2str_data,df):
    
    if button_data=="Name func":
        df.loc[0,'Name']=OCR2str_data
        
    elif button_data=="Age func":
        df.loc[0,'Age']=OCR2str_data
        
    elif button_data=="Disease func":
        df.loc[0,'Disease']=OCR2str_data
        
    elif button_data=="symptom1 func":
        df.loc[0,'Symptom1']=OCR2str_data
        
    elif button_data=="symptom2 func":
        df.loc[0,'Symptom2']=OCR2str_data
        
    elif button_data=="symptom3 func":
        df.loc[0,'Symptom3']=OCR2str_data
        
    return df
#유저가 각각 위치 정보를 입력했을때 그 위치에 해당하는 영역을 crop한후 OCR을 통해 나온 데이터를 위의
#getData를 통해 만들어진 df에 입력한후 반환
def addData(index_num, df,img,name_area,age_area,disease_area,symptom1_area,symptom2_area,symptom3_area):
    print(index_num,"th img processing...")
    crop_area = img[name_area[1]:name_area[3],name_area[0]:name_area[2]]
    name = OCR.image_to_string(crop_area,lang='eng')
    
    crop_area = img[age_area[1]:age_area[3],age_area[0]:age_area[2]]
    age = OCR.image_to_string(crop_area,lang='eng')
    
    crop_area = img[disease_area[1]:disease_area[3],disease_area[0]:disease_area[2]]
    disease = OCR.image_to_string(crop_area,lang='eng')
    
    crop_area = img[symptom1_area[1]:symptom1_area[3],symptom1_area[0]:symptom1_area[2]]
    symptom1 = OCR.image_to_string(crop_area,lang='eng')
    
    crop_area = img[symptom2_area[1]:symptom2_area[3],symptom2_area[0]:symptom2_area[2]]
    symptom2 = OCR.image_to_string(crop_area,lang='eng')
    
    crop_area = img[symptom3_area[1]:symptom3_area[3],symptom3_area[0]:symptom3_area[2]]
    symptom3 = OCR.image_to_string(crop_area,lang='eng')
    
    df.loc[index_num,'Name']=name
    df.loc[index_num,'Age']=age
    df.loc[index_num,'Disease']=disease
    df.loc[index_num,'Symptom1']=symptom1
    df.loc[index_num,'Symptom2']=symptom2
    df.loc[index_num,'Symptom3']=symptom3
    print(index_num,name,age,disease,symptom1,symptom2,symptom3)
    #name_data = 
    #OCR2str_data = OCR.image_to_string(crop_area,lang='eng')
    return df



global backgrnd

backgrnd = np.ones((700,1000), dtype = np.uint8)*255
buttonLoc()
rec_draw()
backgrnd = putText(backgrnd)
rect_mode = False

df=pd.DataFrame(columns=['Name', 'Age','Disease','Symptom1','Symptom2','Symptom3'])
cv2.namedWindow('Chart Detection') 
cv2.setMouseCallback('Chart Detection',onMouse) 
button_mode = None
cv2.imshow("Chart Detection", backgrnd)

while(1): 
    cv2.imshow('Chart Detection',backgrnd) 
    if rect_mode == True:
        if button_data == "Name func":
            
            crop_area = backgrnd[iy:fy,ix:fx]
            #이미지가 나오는 120,270의 좌표만큼 빼줘야 다른 이미지의 원본영상위의 크기가 나옴
            name_area = [ix-270,iy-120,fx-270,fy-120]
            OCR2str_data = OCR.image_to_string(crop_area,lang='eng')
            print(OCR2str_data)
            #OCR2str_data = 'hong'
            df=getData(OCR2str_data,df)
            rect_mode = False
            
        elif button_data == "Age func":    
            crop_area = backgrnd[iy:fy,ix:fx]
            age_area = [ix-270,iy-120,fx-270,fy-120]
            OCR2str_data = OCR.image_to_string(crop_area)
            print(OCR2str_data)
            #OCR2str_data = '100'
            df=getData(OCR2str_data,df)
            rect_mode = False
            
        elif button_data == "Disease func":
            crop_area = backgrnd[iy:fy,ix:fx]
            disease_area = [ix-270,iy-120,fx-270,fy-120]
            OCR2str_data = OCR.image_to_string(crop_area,lang='eng')
            print(OCR2str_data)
            #OCR2str_data = 'cold'
            df=getData(OCR2str_data,df)
            rect_mode = False
            
        elif button_data == "symptom1 func":
            crop_area = backgrnd[iy:fy,ix:fx]
            symptom1_area = [ix-270,iy-120,fx-270,fy-120]
            OCR2str_data = OCR.image_to_string(crop_area,lang='eng')
            print(OCR2str_data)
            #OCR2str_data = '37.4'
            df=getData(OCR2str_data,df)
            rect_mode = False
            
        elif button_data == "symptom2 func":
            crop_area = backgrnd[iy:fy,ix:fx]
            symptom2_area = [ix-270,iy-120,fx-270,fy-120]
            OCR2str_data = OCR.image_to_string(crop_area,lang='eng')
            print(OCR2str_data)
            #OCR2str_data = 'Yes'
            df=getData(OCR2str_data,df)
            rect_mode = False
            
        elif button_data == "symptom3 func":
            crop_area = backgrnd[iy:fy,ix:fx]
            symptom3_area = [ix-270,iy-120,fx-270,fy-120]
            OCR2str_data = OCR.image_to_string(crop_area,lang='eng')
            print(OCR2str_data)
            #OCR2str_data = 'No'
            df=getData(OCR2str_data,df)
            rect_mode = False
    if cv2.waitKey(20) & 0xFF == 32: # enter Space
        print(name_area,age_area,disease_area,symptom1_area,symptom2_area,symptom3_area)
        for i in range(len(imgs_path)):
            index_num = i+1
            # index_num이 3인데 i 최대가 2일경우 에러발생 ==> 예외처리
            if index_num == len(imgs_path):
                break
            img = cv2.imread(imgs_path[index_num])
            img = cv2.resize(img,(570,480))
            img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            if filter_mode == 'otsu':
                ret,img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            elif filter_mode == 'th':
                ret,img = cv2.threshold(img, th_val, 255, cv2.THRESH_BINARY)

            df= addData(index_num,df,img,name_area,age_area,disease_area,symptom1_area,symptom2_area,symptom3_area)
        print(df)
        print("save scv file...")
        df.to_csv(img_path+'\\data_info.csv',sep=',')
        print("Done")                   
        break
    if cv2.waitKey(20) & 0xFF == 27: # enter ESC 
        break     

cv2.destroyAllWindows()
