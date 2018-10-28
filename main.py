#coding=utf-8
import cv2
import time
import os


pixels = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"

def image2chars(img):
    res=[]

    height,width=img.shape
    for row in range(height):
        line=""
        for col in range(width):
            percent=img[row][col]/255
            index=int(percent*(len(pixels)-1))
            line+=pixels[index]+" "
        res.append(line)
    return res


def images2chars(imgs):
    video_chars=[]
    for img in imgs:
        video_chars.append(image2chars(img))
    return video_chars


def video2images(video_name,size,type):
    image_list=[]

    cap=cv2.VideoCapture(video_name)

    while cap.isOpened():
        ret,frame= cap.read()

        if ret:
            if type:
                gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

                img=cv2.resize(gray,size,interpolation=cv2.INTER_AREA)
            else:
                img=cv2.resize(gray,size,interpolation=cv2.INTER_AREA)

            image_list.append(img)
        else:
            break
        
    cap.release()

    return image_list


def play(video_chars):
    width,height=len(video_chars[0][0]),len(video_chars[0])

    for pic_i in range(len(video_chars)):
        for line_i in range(height):
            print(video_chars[pic_i][line_i])
        time.sleep(1/24)

        os.system("cls")


if __name__=="__main__":
    imgs=video2images("./test.flv",(64,48),1)
    video_chars=images2chars(imgs)
    play(video_chars)