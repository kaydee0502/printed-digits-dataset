#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:56:20 2021

@author: kaydee
"""

from PIL import Image, ImageTk
import requests
import matplotlib.pyplot as plt
import numpy as np
import cv2
from tkinter import Tk,Canvas

win = Tk() 
win.geometry("600x400")  
win.resizable(0, 0)  
win.title("Scientific Calculator")

im = Image.open(requests.get("https://www.metalevel.at/sudoku/solved.png", stream=True).raw)
plt.imshow(im)

im = im.resize((252,252))

img = np.array(im)


img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
inv_img = 255 - img
#plt.imshow(inv_im)
cells = []

for r in range(0,252,28):
    for c in range(0,252,28):
        im = inv_img[r:r+28][:,c:c+28]
        pad = np.zeros(im.shape,dtype="uint8")
        pad[2:26][:,2:26] = im[2:26][:,2:26]
        im = pad.copy()
        centroid = pad[5:20][:,5:20]
        plt.imshow(pad)
        
            
        plt.title(sum(centroid.ravel()))
        contours, hierarchy = cv2.findContours(im,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(im, contours, -1, (0,255,0), 3)
        
        
        t = im.copy()
        t2 = im.copy() * 0
        maxc = max(contours, key = cv2.contourArea)
        
        cv2.drawContours(t2, [maxc], -1, 255, 2)

        
        
        cv2.fillPoly(t2, pts =[maxc], color=255)
        im = cv2.bitwise_and(t,t2)
        #plt.imshow(im)
        cells.append(im)
       

        plt.show()



img =  ImageTk.PhotoImage(image=Image.fromarray(cells[0]))
canvas = Canvas(win,width=300,height=300)
canvas.pack()
canvas.create_image(20,20, anchor="nw", image=img)

    





