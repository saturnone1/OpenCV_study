# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser()
    #algorithm select 알고리즘 선택
    parser.add_argument('--alg', type = str, default = 'ORB', choices = ['ORB','SURF'], help = 'Select Algorithm: ORB, AKAZA, SURF, SIRF ... ')
    #matcher type select
    parser.add_argument('--mat', type = str, default = 'FLANN', choices = ['FLANN','BRUTE'], help = 'Select Matcher: BruteForce, FlannBased ...')
    
    args = parser.parse_args()
    algorithm = args.alg
    matcherType = args.mat

    img1 = cv.imread('image/woods3.jpg')
    img2 = cv.imread('image/woods4.jpg')
    gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY,0)
    gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY,0)
    print("Image Read Complete")

    # ORB, SURF
    if algorithm == 'ORB':
        detector = cv.ORB_create(nfeatures=500, WTA_K = 3)
    elif algorithm == 'SURF':
        detector = cv.xfeatures2d.SURF_create(hessianThreshold = 400)
    
    kp1, desc1 = detector.detectAndCompute(gray1, None)
    kp2, desc2 = detector.detectAndCompute(gray2, None)

    if matcherType == 'FLANN' and algorithm == 'ORB':
        #different parameter dictionary for algorithms
        if algorithm == 'ORB':
            index_params= dict(algorithm = 6, table_number = 6, key_size = 12, multi_probe_level = 1)
        elif algorithm == 'SURF':
            index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)

        #checking numbers 
        search_params = dict(checks=100)
        matcher = cv.FlannBasedMatcher(index_params,search_params)

    # SIFT,SURF: NORM_L1, NORM_L2 /  ORB WTA_K ==3 or 4: NORM_HAMMING, NORM_HAMMING2
    elif matcherType == 'BRUTE' and algorithm == 'ORB':
        matcher = cv.BFMatcher(cv.NORM_HAMMING2)
    elif matcherType == 'BRUTE' and algorithm == 'SURF':
        matcher = cv.BFMatcher(cv.NORM_L2, crossCheck = True)
    
    # KNN Match
    matches = matcher.knnMatch(desc1, desc2, k=2)
    print("Keypoint and Description and Macthing Complete")

    # Good Matching Point
    ratio_thresh = 0.75
    good_matches = [m for m,n in matches if m.distance < ratio_thresh * n.distance]

    result = cv.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=2)
    
    imgName = algorithm + "+" + matcherType
    cv.imshow(imgName,result)
    cv.waitKey()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()