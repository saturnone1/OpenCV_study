# !/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

K = 10
iteration = 30
color_space = 1

def kmeans_clustering(img,K,iteration):
    shape = img.shape
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

    return res2

def histogram(img1,img2):
    hist1 = cv.calcHist([img1],[0,1], None, [180,256], [0,180,0, 256])
    hist2 = cv.calcHist([img2],[0,1], None, [180,256], [0,180,0, 256])
    cv.normalize(hist1, hist1, 0, 1, cv.NORM_MINMAX)
    cv.normalize(hist2, hist2, 0, 1, cv.NORM_MINMAX)

    return hist1,hist2

def main():
    global K, iteration, color_space, seeTrackbar
    img1 = cv.imread('image/tw3.jpg', cv.IMREAD_COLOR)
    img2 = img1[img1.shape[1]/10:img1.shape[1]*11/10,img1.shape[0]/4: img1.shape[0]*2/4].copy()
    height, width , channels = img1.shape
    #img2 = cv.resize(img2, dsize = (width, height), interpolation=cv.INTER_LINEAR_EXACT)

    '''
    #트랙바 생성
    makeTrackbar('clustering')
    '''
    
    '''
    while True:
        if cv.waitKey(1) & 0xFF == 27:
            break
            

    # 키 입력 시 종료
    if seeTrackbar == 0:
        '''

    if color_space == 1:
        img1 = cv.cvtColor(img1,cv.COLOR_BGR2HSV)
        img2 = cv.cvtColor(img2,cv.COLOR_BGR2HSV)
    elif color_space == 2:
        img1 = cv.cvtColor(img1,cv.COLOR_BGR2LAB)
        img2 = cv.cvtColor(img2,cv.COLOR_BGR2LAB)
    else:
        img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
        img2 = cv.cvtColor(img2,cv.COLOR_BGR2RGB)

    #클러스터링 수행
    img_result1 = kmeans_clustering(img1,K,iteration)
    img_result2 = kmeans_clustering(img2,K,iteration)

    if color_space == 1:
        img_result1 = cv.cvtColor(img_result1,cv.COLOR_HSV2RGB)
        img_result2 = cv.cvtColor(img_result2,cv.COLOR_HSV2RGB)
    elif color_space == 2:
        img_result1 = cv.cvtColor(img_result1,cv.COLOR_LAB2RGB)
        img_result2 = cv.cvtColor(img_result2,cv.COLOR_LAB2RGB)

    #histogram
    hist1,hist2 = histogram(img_result1,img_result2)
    #hist1,hist2 = histogram(img1,img2)

    #두 이미지 연결 및 출력
    plt.subplot(221),plt.imshow(img_result1),plt.title('Start Kmeans')
    plt.subplot(222),plt.imshow(img_result2),plt.title('Compare Kmeans')

    #plt.subplot(221),plt.imshow(img1),plt.title('Start')
    #plt.subplot(222),plt.imshow(img2),plt.title('Compare')

    plt.subplot(223),plt.plot(hist1,color='r')
    plt.subplot(224),plt.plot(hist2,color='b')

    plt.show()

if __name__ == '__main__':
    main()