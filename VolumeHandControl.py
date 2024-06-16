import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
# macOS 平台 修改mac电脑音量
import os
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Setting camera dimenensions
wCam, hCam = 640,480

# Initializing the Camera
cap = cv2.VideoCapture(1)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

#Initializing the hand detector
detectror = htm.handDetector(detectionCon=0.7)

#windows 音量控制模块 参考：https://pypi.org/project/pycaw/ Usage or python获取并修改电脑音量:https://www.cnblogs.com/yunhgu/p/14980109.html
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = interface.QueryInterface(IAudioEndpointVolume)
#
# volRange = volume.GetVolumeRange()
# minVol = volRange[0]
# maxVol = volRange[1]
# volume.SetMasterVolumeLevel(-20.0, None)
vol = 0
volBar = 400
volPer = 0
#参考：
def set_volume_macos(volume):
    os.system(f"osascript -e 'set volume output volume {volume}'")

def get_volume_macos():
    output = os.popen("osascript -e 'output volume of (get volume settings)'").read()
    volume = int(output.strip())
    return volume

while True:
    success, img = cap.read()
    if  not success:
        break
    #detecting hands
    img = detectror.findHands(img)
    lmList = detectror.findPosition(img,draw=False)
    if len(lmList) != 0:
        #print(lmList[4],lmList[8])
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]
        cv2.circle(img,(x1,y1),15,(255,0,0),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(255,0,0),cv2.FILLED)
        cx,cy = (x1 + x2) // 2,(y1 + y2)//2
        cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)
        #第二个点和第8个点的直线
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
        #计算（x1,y1）,(x2,y2)两点之间距离
        length = math.hypot(x2-x1,y2-y2)
        # Hand Range 50 -300
        # Volume range -65 - 0
        vol = np.interp(length,[10,180],[-65,0])
        volBar = np.interp(length,[10,180],[400,150])
        volPer = np.interp(length,[10,180],[0,100])
        # print(int(length),vol,volPer,volBar)
        #setting the volume
        print(f"length:{length},vol:{vol},volBar:{volBar},volPer:{volPer}")
        set_volume_macos(int(volPer))
        print(get_volume_macos())
        if(length < 50):
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED) #小于50时，改为绿色
    #drawing the volume bar
    cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv2.rectangle(img,(50,int(volBar)),(85,400),(255,0,0),cv2.FILLED)
    cv2.putText(img,f'{int(volPer)}%' ,(40,450),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),2)
    #计算fps
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    # displaying the fps on the image
    cv2.putText(img,f'FPS:{int(fps)}',(40,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    #show the image
    cv2.imshow("Img",img)
    if(cv2.waitKey(1) & 0xFF ==ord('1')):
        break

cap.release()
cv2.destroyAllWindows()

# 安装三方类库：https://cloud.tencent.com/developer/article/2121534
# 项目来源：https://www.google.com/search?q=compute+vision+VolumeHandControl&oq=compute+vision+VolumeHandControl&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAHSAQgyNjgxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8#fpstate=ive&ip=1&vld=cid:acb1b89c,vid:9iEPzbG-xLE,st:0

