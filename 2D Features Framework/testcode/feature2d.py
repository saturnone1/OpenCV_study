# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
import argparse

#알고리즘 생성
def keyDetect(algorithm, gray1,gray2):
    # ORB, SURF
    if algorithm == 'ORB':
        detector = cv.ORB_create(nfeatures=1000, WTA_K = 3)
    elif algorithm == 'SURF':
        detector = cv.xfeatures2d.SURF_create(hessianThreshold = 200)

    kp1, desc1 = detector.detectAndCompute(gray1, None)
    kp2, desc2 = detector.detectAndCompute(gray2, None)

    print("Descriptor Type:%s Shape:%s", type(desc1), desc1.shape)
    return kp1,kp2, desc1,desc2

#Matcher 생성
def setMatcher(algorithm, matcherType):
    if matcherType == 'FLANN':
        #different parameter dictionary for algorithms
        if algorithm == 'ORB':
            index_params= dict(algorithm = 6, table_number = 6, key_size = 12, multi_probe_level = 2)
        elif algorithm == 'SURF':
            index_params = dict(algorithm = 1, trees = 5)

        #checking numbers 
        search_params = dict(checks=10)
        matcher = cv.FlannBasedMatcher(index_params,search_params)

    # SIFT,SURF: NORM_L1, NORM_L2 /  ORB WTA_K ==3 or 4: NORM_HAMMING, NORM_HAMMING2
    elif matcherType == 'BRUTE' and algorithm == 'ORB':
        matcher = cv.BFMatcher(cv.NORM_HAMMING2)
    elif matcherType == 'BRUTE' and algorithm == 'SURF':
        matcher = cv.BFMatcher(cv.NORM_L2, crossCheck = False)
    return matcher

#매칭 결과를 knn에 적용한 후 좋은 매칭 결과만 반환
def match_knn(matcher, desc1, desc2):
    print("Macthing Complete")

    # KNN Match
    matches = matcher.knnMatch(desc1, desc2, k=2)

    # Good Matching Point
    ratio_thresh = 0.7
    good_matches = [m for m,n in matches if m.distance < ratio_thresh * n.distance]

    return good_matches

#이미지 입력 및 HSV 변환
def setImg(img1,img2):
    hsv1 = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
    hsv2 = cv.cvtColor(img2, cv.COLOR_BGR2HSV)
    
    hsv_split1 = cv.split(hsv1)
    hsv_split2 = cv.split(hsv2)
    print("Image Read Complete: HSV Array")

    return hsv_split1, hsv_split2

#커맨드 라인 명령어 생성자
def commandparser():
    parser = argparse.ArgumentParser()
    #algorithm select 알고리즘 선택
    parser.add_argument('--alg', type = str, default = 'ORB', choices = ['ORB','SURF'], help = 'Select Algorithm: ORB, AKAZA, SURF, SIRF ... ')
    #matcher 선택
    parser.add_argument('--mat', type = str, default = 'FLANN', choices = ['FLANN','BRUTE'], help = 'Select Matcher: BruteForce, FlannBased ...')

    args = parser.parse_args()
    algorithm = args.alg
    matcherType = args.mat

    return algorithm,matcherType

#H,S,V 개별 keypoint와 descriptor 결합
def hsv_combine(hsv1, hsv2, algorithm):
    kp1R = np.array([])
    kp2R = np.array([])
    desc1R = np.array([])
    desc2R = np.array([])

    for i in range(len(hsv1)-1):
        #Keypoint, Descriptor 생성
        kp1,kp2,desc1,desc2 = keyDetect(algorithm,hsv1[i],hsv2[i]) 
        if i == 0:
            kp1R = kp1
            kp2R = kp2
            desc1R = desc1
            desc2R = desc2
        else :
            kp1R = np.append(kp1R, kp1, axis = 0)
            kp2R = np.append(kp2R, kp2, axis = 0)
            desc1R = np.vstack([desc1R, desc1])
            desc2R = np.vstack([desc2R, desc2])

    desc1R = np.delete(desc1R,0,0)
    desc2R = np.delete(desc2R,0,0)

    kp1R = kp1R.tolist()
    kp2R = kp2R.tolist()

    return kp1R, kp2R, desc1R, desc2R

def main():
    img1 = cv.imread('image/iu1.jpg')
    img2 = cv.imread('image/iu2.jpg')

    #커맨드 입력 파서
    algorithm, matcherType = commandparser()

    #HSV 분할 Array
    hsv1, hsv2 = setImg(img1,img2)

    #HSV에서 개별로 keypoing, description을 생성 후 결합
    kp1,kp2,desc1,desc2 = hsv_combine(hsv1,hsv2,algorithm)

    #Matcher생성 및 matching
    matcher = setMatcher(algorithm, matcherType)

    #Matching 중에서 걸러냄
    good_matches = match_knn(matcher,desc1,desc2)

    #draw Match
    result = cv.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=2)

    #이미지 출력
    imgName = algorithm + "+" + matcherType
    cv.imshow(imgName,result)
    cv.waitKey()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()