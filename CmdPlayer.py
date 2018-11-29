import cv2
import sys
import multiprocessing
import time
import os
import win32api
import win32console
import pydub
from pydub.playback import play
import ctypes



#载入调用c函数的动态链接库
Drawdll=ctypes.cdll.LoadLibrary("./CmdDraw.dll")

#字符集
pixels = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"

#反向字符集
#pixels = "$#@&%ZYXWVUTSRQPONMLKJIHGFEDCBA098765432?][}{/\)(><zyxwvutsrqponmlkjihgfedcba*+1!:`'-,. "

#获取字符集长度
length=len(pixels)

#字符帧存储队列  进程共享用
q=multiprocessing.Queue()

#视频帧转换到字符帧
def image2chars(image):
    ret=[]
    height,width=image.shape
    for i in range(height):
        line=""
        for j in range(width):
            percent=image[i][j]/255
            index=int(percent*(length-1))
            line+=pixels[index]
        ret.append(line)
    return ret

#转换进程函数
def video2chars(q,video_name,size):
    cap=cv2.VideoCapture(video_name)
    while cap.isOpened():
        ret,frame=cap.read()
        if ret:
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            image=cv2.resize(gray,size,interpolation=cv2.INTER_AREA)
            
            q.put(image2chars(image))
        else:
            print("Error when reading frame")
            break
    cap.release()


#字符帧打印进程函数
def draw(q,fps,width,height):
    Drawdll.console_init(height,width)
    runtime=0
    delay=0.98/fps
    #delay=1/(fps+(width*height/1000))
    while True:
        start=time.time()
        for value in q.get():
            print(value)
        print("fps=%f   runtime=%f"%(fps,runtime))
        end=time.time()
        runtime=start-end
        if (delay+runtime>0):
            time.sleep(delay+runtime)
        Drawdll.gotoxy(0,0)

#获取视频音轨
def Getbacksound(video_name):
    temp=video_name.split('.',1)
    file_name=temp[0]+".mp3"
    #print(file_name)
    if os.path.isfile(file_name):
        return file_name

    cmd="ffmpeg -i "+video_name+" -f mp3 -vn "+file_name
    os.system(cmd)
    return file_name

#音轨播放
def musicplay(music_name):
    #print(music_name)
    sound=pydub.AudioSegment.from_file(str(music_name),format="mp3")
    play(sound)

#获取视频fps
def Getfps(video_name):
    cap=cv2.VideoCapture(video_name)
    if not(cap.isOpened()):
        print("Can't find the mv!")
        sys.exit(0)
    
    ret=cap.get(5)
    cap.release()
    return ret

#主程序
#name=""
if __name__ == "__main__":
    
    try:
        video_name=str(sys.argv[1])
        if video_name=="0":
            video_name=0
        height=int(sys.argv[2])
        width=int(sys.argv[3])
        music_boot=str(sys.argv[4])
        size=(height,width)
    except:
        print("Usage: CmdPlayer.py <video_name> <width> <height> <music_setting on|off>")
        print("Tips:size 128:64 is recommend")
        sys.exit(0)
    
    fps=Getfps(video_name)
    
    music_name=""
    if music_boot=="on" :
        music_name=Getbacksound(video_name)
        #print(music_name)

    #多进程
    p1=multiprocessing.Process(target=video2chars,args=(q,video_name,size))
    p2=multiprocessing.Process(target=draw,args=(q,fps,width,height))
    if music_boot=="on":
        p3=multiprocessing.Process(target=musicplay,args=(music_name,))
    #进程启动
    p1.start()
    time.sleep(1)
    p2.start()
    if music_boot=="on":
        p3.start()
    #进程join
    p1.join()
    p2.join()
    if music_boot=="on":
        p3.join()



