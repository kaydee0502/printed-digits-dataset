#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:18:10 2021

@author: kaydee
"""

import matplotlib.pyplot as plt
import cv2
import os

def removeNoise(img):
    r,mask = cv2.threshold(img,10,255,cv2.THRESH_BINARY)
    eout = cv2.bitwise_and(mask,img)
    return eout


for i in range(1,10):
    cwd = "assets/"+str(i)
    for f in os.listdir(cwd):
        
        fig, ax = plt.subplots(1,2)
        img = cv2.imread(cwd+"/"+f)
        img = removeNoise(img)
        ax[0].imshow((img == 0).astype("int")*255)
        ax[1].imshow(img)
        
        cv2.imwrite(cwd+"/"+f,img)
        plt.show()