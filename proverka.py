# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:51:24 2019

@author: Stefan
"""
import pandas as pd
import numpy as np
import cv2
import glob
from sklearn.model_selection import train_test_split

#images1=[cv2.imread(file) for file in glob.glob('C:/Users/Stefan/Desktop/PackageWallStuff/MaskiOdDosegasniAnotacii/*.bmp')]
#images1=list(np.float_(images))
images1=[cv2.imread(file) for file in glob.glob('E:/fax/package_wall/PackageWall/packageWallAnnotationVisualization/*.bmp')]
sliki=[cv2.imread(file) for file in glob.glob('E:/fax/sivi_sliki/*.bmp')]
X_train,X_test,X1_train,X1_test=train_test_split(sliki,images1,test_size=0.15)
X_train,X_val,X1_train,X1_val=train_test_split(X_train,X1_train,test_size=0.15)
pom=[]
A=[]
B=[]
glavno=[]
#tr=images1[3][75:80,40:44,:]


for broj in range(len(X1_train)):
   for i in range(144):
       for j in range(176):
            if ((X1_train[broj][i,j,1]!=X1_train[broj][i,j,0]) and (X1_train[broj][i,j,1]!=X1_train[broj][i,j,2]) and (X1_train[broj][i,j,2]==X1_train[broj][i,j,0])):
                pom.append(1)
                
            else:
                pom.append(0)

val=[]
for broj in range(len(X1_val)):
   for i in range(144):
       for j in range(176):
            if ((X1_val[broj][i,j,1]!=X1_val[broj][i,j,0]) and (X1_val[broj][i,j,1]!=X1_val[broj][i,j,2]) and (X1_val[broj][i,j,2]==X1_val[broj][i,j,0])):
                val.append(1)
                
            else:
                val.append(0)
#A.append(X_train[broj][i-2:i+3,j-2:j+3,:])
pom1=np.asarray(pom) 
pom1=pom1.reshape(len(X1_train),144,176)
val=np.asarray(val)
val=val.reshape(len(X1_val),144,176)
#tr=pom1[2][2:7,5:10]
for broj in range(len(X1_train)):
   for i in range(2,142):
       for j in range(2,174):
           #pp=np.sum(pom1[broj][i-2:i+3,j-2:j+3])
           #if pp!=0:
               #A.append(X_train[broj][i-2:i+3,j-2:j+3,:])
           if pom1[broj][i,j]==1:
               A.append(X_train[broj][i-2:i+3,j-2:j+3,:])
 
A_val=[]
for broj in range(len(X1_val)):
   for i in range(2,142):
       for j in range(2,174):
           #pp=np.sum(pom1[broj][i-2:i+3,j-2:j+3])
           #if pp!=0:
               #A.append(X_train[broj][i-2:i+3,j-2:j+3,:])
           if val[broj][i,j]==1:
               A_val.append(X_val[broj][i-2:i+3,j-2:j+3,:])          
import random
for l in range(6*len(A)):
    br=random.randint(0,len(X1_train)-1)
    x=random.randint(4,140)
    y=random.randint(4,170)
    pp=np.sum(pom1[br][x-2:x+3,y-2:y+3])
    if pp==0:
        B.append(X_train[br][x-2:x+3,y-2:y+3,:])
B_val=[]
for l in range(5*len(A_val)):
    br=random.randint(0,len(X1_val)-1)
    x=random.randint(4,140)
    y=random.randint(4,170)
    pp=np.sum(val[br][x-2:x+3,y-2:y+3])
    if pp==0:
        B_val.append(X_val[br][x-2:x+3,y-2:y+3,:])

#B=B+nn
y1=[]
x1=A+B;
xp_val=A_val+B_val
xp_val=np.asarray(xp_val)
yp_val=[]
for i in range(len(A)):
    y1.append(1)
for i in range(len(B)):
    y1.append(0)
for i in range(len(A_val)):
    yp_val.append(1)
for i in range(len(B_val)):
    yp_val.append(0)

from keras.utils import to_categorical
y1=to_categorical(y1,num_classes=2,dtype='int32')
yp_val=to_categorical(yp_val,num_classes=2,dtype='int32')
x1=np.asarray(x1)
#X_train=np.asarray(X_train)
#X_test=np.asarray(X_test)

p1=[]
for broj in range(len(X1_test)):
   for i in range(2,142):
       for j in range(2,174):
            if ((X1_test[broj][i,j,1]!=X1_test[broj][i,j,0]) and (X1_test[broj][i,j,1]!=X1_test[broj][i,j,2]) and (X1_test[broj][i,j,2]==X1_test[broj][i,j,0])):
                p1.append(1)
                
            else:
                p1.append(0)

p1=np.asarray(p1) 
y_true=p1.reshape(len(X1_test),140,172)
y_true=to_categorical(y_true,num_classes=2,dtype='int32')


for broj in range(len(X_test)):
   for i in range(2,142):
       for j in range(2,174):
           glavno.append(X_test[broj][i-2:i+3,j-2:j+3,:])

glavno=np.asarray(glavno)           
import matplotlib.pyplot as plt
plt.figure(1)
plt.imshow(images1[3])
plt.imshow(pom1[3])




#images1=images1/np.linalg.norm(images1,ord=1,axis=1,keepdims=True)
#pom=np.reshape(images1, (120,76032))
#np.savetxt('sli.csv', images1, delimiter=',')
#prva=images1[1:95]
#prva=prva/np.linalg.norm(prva,ord=1,axis=1,keepdims=True)
#print(prva)
#druga=images1[96:120]