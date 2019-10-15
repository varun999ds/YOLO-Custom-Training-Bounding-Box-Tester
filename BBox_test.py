#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 13:49:33 2019

@author: amvar
"""

import cv2
import argparse
import numpy as np
import glob
import os

if not os.path.exists('input/'):
    os.mkdir('input/')

if not os.path.exists('output/'):
    os.mkdir('output/')





# Darw a rectangle surrounding the object and its class name 
def draw_pred(img, label, confidence, x, y, x_plus_w, y_plus_h):



    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), (0,255,255), 2)

    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2)



c=0
for i in glob.glob('input/*.jpg'):
    img=cv2.imread(i)
    W=img.shape[1]
    H=img.shape[0]
    #print(W,H)
    
    with open('{}'.format(i).replace('jpg','txt'), 'r+') as f:
        for obj in f.readlines():
            #print(obj)
            #print(obj.split(' ')[0])
            
            x=float(obj.split(' ')[1])*W
            y=float(obj.split(' ')[2])*H
            w=float(obj.split(' ')[3])*W
            h=float(obj.split(' ')[4])*H
            print(x/W,y/H,w/W,h/H)
            x=int(x-(w/2))
            y=int(y-h/2)
            w=int(w)
            h=int(h)
            #print(x/W,y/H,w/W,h/H)
            label=obj.split(' ')[0]
            draw_pred(img, label, 0.9999, x,(y), x+w, y+h)
        
            
            print(obj)
        
        cv2.imwrite('output/{}.jpg'.format(c), img)
        c+=1
#        cv2.imshow(img)








    




'''Changing the value of classid from 15 to 0'''

for i in glob.glob('labels/'):
    with open(i, 'r+') as f:
        line=f.readlines()
        splitted=line.split(' ')
        splitted[0]=0
        newline = ' '.join(splitted)
        f.writelines(newline)











int((obj[4].lstrip()).split('.')[0])
 int('20.0')
# Define a window to show the cam stream on it
 
 
 
 
 
 '''YOLO ANNOTATION FORMAT'''
 #<object-class-id> <center-x> <center-y> <width> <height>
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
