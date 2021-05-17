# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

K = 10
iteration = 5
color_space = 0

def kmc(x):
    global K
    K = x

def iter(x):
    global iteration
    iteration = x

def color(x):
    global color_space
    color_space = x

#커맨드 라인 명령어 생성자
def makeTrackbar(name):
    cv.namedWindow(name)
    # create trackbars for color change
    cv.createTrackbar('KNumber',name,10,30, kmc)
    cv.createTrackbar('maxIter',name,5,30, iter)
    cv.createTrackbar('ColorSpace',name,0,2, color)

def seeTrackbar(name):
    cv.getTrackbarPos('KNumber',name)
    cv.getTrackbarPos('maxIter',name)
    cv.getTrackbarPos('ColorSpace',name)

def kmeans_clustering(img,K,iteration,color_space):
    shape = img.shape
    if color_space == 1:
        img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    elif color_space == 2:
        img = cv.cvtColor(img,cv.COLOR_BGR2LAB)

    #convert img to np.float32 and Flattening
    img = img.reshape((-1,3))
    img = np.float32(img)

    # Define criteria = ( type, max_iter(반복 회수) = 10 , epsilon(정확도) = 1.0 ) 
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, iteration, 1.0)
    ret,label,center=cv.kmeans(img,K,None,criteria,10,cv.KMEANS_PP_CENTERS) # do Algorihtm

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((shape))

    if color_space == 1:
        res2 = cv.cvtColor(res2,cv.COLOR_HSV2BGR)
    elif color_space == 2:
        res2 = cv.cvtColor(res2,cv.COLOR_LAB2BGR)

    return res2

def callback_does(img):
    global K, iteration, color_space
    img_result = kmeans_clustering(img,K,iteration,color_space)
    return img_result