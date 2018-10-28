import cv2
import sys
import os
import threading
import queue
import time

pixels = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"
global video_chars
video_chars=queue.Queue()

def image2chars(image):
    ret=[]
    height,width=image.shape
    for row in range(height):
        line=""
        for col in range(width):
            percent=image[row][col]/255
            index=int(percent*(len(pixels)-1))
            line+=pixels[index]+" "
        ret.append(line)
    return ret

def video2images(video_name,size):
    cap=cv2.VideoCapture(video_name)

    if not(cap.isOpened()):
        print("Error file name!")
        sys.exit(0)

    i=0
    global fps
    fps=cap.get(5)
    #print(fps)
    #os.system("pause")

    while cap.isOpened():
        ret,frame=cap.read()
        if ret:
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            image=cv2.resize(gray,size,interpolation=cv2.INTER_AREA)
            video_chars.put(image2chars(image))
            #print("x")
                
        else:
            print("Error when reading freame")
            break
    cap.release()


def draw():
    
    while True:

        for value in video_chars.get():
            print(value)
        time.sleep(0.01)
        os.system("cls")
        


def main(argv):
    try:
        video_name=str(argv[0])
        if video_name=="0":
            video_name=0
        height=int(argv[1])
        width=int(argv[2])
        size=(height,width)
    except:
        print("Usage: CmdPlayer.py <video_name> <height> <width>")
        print("Warning: Don't set a large size")
        sys.exit(0)
    global thread_convent
    global thread_draw
    thread_convent=threading.Thread(target=video2images,args=(video_name,size,))
    thread_draw=threading.Thread(target=draw)
    #thread_draw.setDaemon()
    #thread_convent.setDaemon()
    thread_draw.start()
    thread_convent.start()
    time.sleep(5)
    
    #for t in [thread_convent,thread_draw]:
    #    t.start()
    #for t in [thread_convent,thread_draw]:
    #    t.join()
    thread_convent.join()
    thread_draw.join()





if __name__=="__main__":
    main(sys.argv[1:])