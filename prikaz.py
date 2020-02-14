# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:58:52 2019

@author: Stefan
"""
import numpy as np
import matplotlib.pyplot as plt
plt.figure(1)
#plt.imshow(y_true[1,:,:,0])
pom11=[]
for k in range(len(X_test)):
   for i in range(140):
       for j in range(172):
           if h1[k,i,j,1]>0.9:
               pom11.append(1)
           else:
               pom11.append(0)

pom11=np.asarray(pom11)
pom11=pom11.reshape(len(X1_test),140,172)

#plt.imshow(pom11[1,:,:])