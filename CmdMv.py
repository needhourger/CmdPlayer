# -*- coding:utf-8 -*-
import cv2
import sys
import os
import time
pixels = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"

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

def draw(video_chars):
    for value in video_chars:
        print(value)
    os.system("cls")
        

def play(video_name,size,speed):
    cap=cv2.VideoCapture(video_name)

    if not(cap.isOpened()):
        print ("Error file name!")
        sys.exit(0)
    
    video_chars=[]
    while cap.isOpened():
        ret,frame=cap.read()
        
        if ret:
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            image=cv2.resize(gray,size,interpolation=cv2.INTER_AREA)
            draw(image2chars(image))
            
        else:
            print("[ERROR] failed to read video file!")
            break

    cap.release()

def main(argv):
    try:
        video_name=""
        video_name=str(argv[0])
        if video_name=="0":
            video_name=0
        height=int(argv[1])
        width=int(argv[2])
    except:
        print("Usage: example.py [video_name] height width")
        sys.exit(0)
    speed=1
    play(video_name,(height,width),speed)


if __name__=="__main__":
    main(sys.argv[1:])

