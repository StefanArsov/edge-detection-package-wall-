# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:32:56 2019

@author: Stefan
"""
import glob
import cv2
import numpy as np
pw=[]
im1=[cv2.imread(file) for file in glob.glob('C:/Users/Stefan/Desktop/package_wall/PackageWall/packageWallAnnotationVisualization/*.bmp')]
sliki=[cv2.imread(file) for file in glob.glob('C:/Users/Stefan/Desktop/sivi_sliki/*.bmp')]
for b in range(len(im1)):
    for i in range(144):
         
        for j in range(176):
       
            if ((im1[b][i,j,1]!=im1[b][i,j,0]) and (im1[b][i,j,1]!=im1[b][i,j,2]) and (im1[b][i,j,2]==im1[b][i,j,0])):
           
                pw.append(1)
            else:
                pw.append(0)


pw=np.asarray(pw)
pw=pw.reshape(len(im1),144,176)
import matplotlib
A=[]
for broj in range(2):
   for i in range(2,142):
       for j in range(2,174):
           pp=np.sum(pw[broj][i-2:i+3,j-2:j+3])
           if pp!=0:
               A.append(sliki[broj][i-2:i+3,j-2:j+3,:])
#for i in range(len(im1)):
    #matplotlib.image.imsave('slika'+str(i)+'.jpg', pw[i,:,:])
