# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:25:28 2019

@author: Stefan
"""
import cv2
import numpy
import glob
import pylab as plt

folders = glob.glob('C:/Users/Stefan/Desktop/PackageWallStuff/MaskiOdDosegasniAnotacii/*')
imagenames__list = []
for folder in folders:
    for f in glob.glob(folder+'/*.bmp'):
        imagenames__list.append(f)

read_images = []        

for image in imagenames__list:
    read_images.append(cv2.imread(image, cv2.IMREAD_GRAYSCALE))
