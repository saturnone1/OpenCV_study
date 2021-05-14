# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
import argparse

def nothing(x):
    pass

#커맨드 라인 명령어 생성자
def Trackbar():
    cv.namedWindow("KMeansClustering")
    # create trackbars for color change
    cv.createTrackbar('KNumber',"KMeansClustering",2,100,nothing)
    cv.createTrackbar('maxIter',"KMeansClustering",5,50,nothing)
    cv.createTrackbar('ColorSpace',"KMeansClustering",0,2,nothing)

def main():
    img = cv.imread('image/iu1.jpg')
    #TrackBar 생성
    Trackbar()
    
    while(1):
        K = cv.getTrackbarPos('KNumber',"KMeansClustering") # K number of colors
        iteration = cv.getTrackbarPos('maxIter',"KMeansClustering")
        color_space = cv.getTrackbarPos('ColorSpace',"KMeansClustering")
        
        imghsv = img
        if color_space == 1:
            imghsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
        elif color_space == 2:
            imghsv = cv.cvtColor(img,cv.COLOR_BGR2LAB)

        #convert img to np.float32 and Flattening
        img_reshaped = imghsv.reshape((-1,3))
        img_reshaped = np.float32(img_reshaped)

        # Define criteria = ( type, max_iter(반복 회수) = 10 , epsilon(정확도) = 1.0 ) 
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, iteration, 1.0)
        ret,label,center=cv.kmeans(img_reshaped,K,None,criteria,10,cv.KMEANS_PP_CENTERS) # do Algorihtm

        # Now convert back into uint8, and make original image
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((img.shape))

        img_show = res2
        if color_space == 1:
            img_show = cv.cvtColor(res2,cv.COLOR_HSV2BGR)
        elif color_space == 2:
            img_show = cv.cvtColor(res2,cv.COLOR_LAB2BGR)
        
        #원본 이미지와 결합
        addimg = cv.hconcat([img,img_show])

        cv.imshow("KMeansClustering",addimg)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break

    cv.destroyAllWindows()

if __name__ == "__main__":
    main()