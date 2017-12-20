#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import tkinter.filedialog
import sys,os,traceback
import requests
import cv2
from PIL import Image, ImageTk  
import tkinter.messagebox
import faceswapper as face
headimg = ''  
faceimg = ''  
def headimgselect():
    selectFileName = tkinter.filedialog.askopenfilename(title='选择文件',filetypes=[("jpg格式","jpg")])#选择文件
    global headimg
    headimg = selectFileName

def faceimgselect():
    selectFileNameq = tkinter.filedialog.askopenfilename(title='选择文件',filetypes=[("jpg格式","jpg")])#选择文件
    global faceimg
    faceimg = selectFileNameq



def faceswap():
    global headimg
    global faceimg
    head,face_path,out=headimg,faceimg,os.path.dirname(os.path.realpath(sys.argv[0]))+'/output.jpg'
    swapper=face.Faceswapper([head])
    output_im=swapper.swap(os.path.split(head)[-1],face_path)#返回的numpy数组
    swapper.save(out,output_im)
    # print(headimg)
    # print (__file__)
    # print (os.path.realpath(__file__))
    # print ('using sys.executable:', repr(os.path.dirname(os.path.realpath(sys.executable))))
    # print ('using sys.argv[0]:',    repr(os.path.dirname(os.path.realpath(sys.argv[0]   ))))
    # print (sys.argv[0])
    # print (sys.path[0])
    show()

def biggest(a,b,c):
    # 先比较a和b
    if a>b:
        maxnum = a
    else:
        maxnum = b
    # 再比较maxnum和c
    if c>maxnum:
        maxnum=c
    return maxnum

def show():
    top1=Toplevel()
    global headimg
    global faceimg
    image1 = Image.open(headimg) 
    img1 = ImageTk.PhotoImage(image1)

    image2 = Image.open(faceimg) 
    img2 = ImageTk.PhotoImage(image2)
    image = Image.open(os.path.dirname(os.path.realpath(sys.argv[0]))+'/output.jpg') 
    img = ImageTk.PhotoImage(image)
    maxnum = biggest(image.height,image1.height,image2.height)
    canvas1 = Canvas(top1, width = image.width+image1.width+image2.width ,height = maxnum, bg = 'white')
    canvas1.create_image(0,0,image = img1,anchor="nw")
    canvas1.create_image(image1.width,0,image = img2,anchor="nw")
    canvas1.create_image(image1.width+image2.width,0,image = img,anchor="nw")
    canvas1.pack()   
    top1.mainloop()

root = Tk()
root.title('面部替换')
root.geometry('+500+300')
e1 = Entry(root,width=30)
e1.grid(row=0, column=0)


btn1 = Button(root,text=' 头部图 ', command=headimgselect).grid(row=1, column=0,padx=2,pady=5)
btn2 = Button(root,text=' 面部图 ', command=faceimgselect).grid(row=2, column=0,padx=2,pady=5)
btn3 = Button(root,text=' 替换   ', command=faceswap).grid(row=3, column=0,pady=5)

mainloop()