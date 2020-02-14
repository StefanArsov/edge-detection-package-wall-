# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:00:06 2019

@author: Stefan
"""
import glob
import cv2
sliki=[cv2.imread(file) for file in glob.glob('E:/fax/sivi_sliki/*.bmp')]
sl1=[cv2.imread(file) for file in glob.glob('E:/fax/package_wall/PackageWall/edgeAnnotationVisualization/*.bmp')]
nn=[]
for i in range(2,142):
   for j in range(2,174):
       if ((sl1[0][i,j,1]!=sl1[0][i,j,0]) and (sl1[0][i,j,1]!=sl1[0][i,j,2]) and (sl1[0][i,j,2]==sl1[0][i,j,0])):
                nn.append(sliki[0][i-2:i+3,j-2:j+3,:])
       if ((sl1[7][i,j,1]!=sl1[7][i,j,0]) and (sl1[7][i,j,1]!=sl1[7][i,j,2]) and (sl1[7][i,j,2]==sl1[7][i,j,0])):    
                nn.append(sliki[7][i-2:i+3,j-2:j+3,:])
       if ((sl1[9][i,j,1]!=sl1[9][i,j,0]) and (sl1[9][i,j,1]!=sl1[9][i,j,2]) and (sl1[9][i,j,2]==sl1[9][i,j,0])):    
                nn.append(sliki[7][i-2:i+3,j-2:j+3,:])
       
for i in range(50,110):
   for j in range(50,130):
       nn.append(sliki[6][i-2:i+3,j-2:j+3,:])

nn.append(sliki[2][139:144,86:91,:])
nn.append(sliki[3][95:100,76:81,:])
nn.append(sliki[3][118:123,76:81,:])
nn.append(sliki[3][72:77,90:95,:])
nn.append(sliki[3][52:57,90:95,:])

