# Feature Matching with FLANN
각 알고리즘의 성능 비교는 다음 논문에서 확인 할 수 있다.: [논문](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8346440)

```python

from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Code for Feature Matching with FLANN tutorial.')
parser.add_argument('--input1', help='Path to input image 1.', default='box.png')
parser.add_argument('--input2', help='Path to input image 2.', default='box_in_scene.png')
args = parser.parse_args()

# 이미지 로드
img1 = cv.imread(cv.samples.findFile(args.input1), cv.IMREAD_GRAYSCALE)
img2 = cv.imread(cv.samples.findFile(args.input2), cv.IMREAD_GRAYSCALE)
if img1 is None or img2 is None:
    print('Could not open or find the images!')
    exit(0)

#-- Step 1: SURF로 keypoint와 Descriptor 추출
minHessian = 400
detector = cv.xfeatures2d_SURF.create(hessianThreshold=minHessian)
keypoints1, descriptors1 = detector.detectAndCompute(img1, None)
keypoints2, descriptors2 = detector.detectAndCompute(img2, None)

#-- Step 2: Descriptor를 FLANN 기반 matcher를 활용하여 생성
# Since SURF is a floating-point descriptor NORM_L2 is used
matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)

# knnMatch를 이용하여 descriptor당 k개의 이웃 매칭점을 잡아낸다
# k개의 매칭점중 거리 distance가 짧은 것이 좋은 매칭점일 가능성이 높다
knn_matches = matcher.knnMatch(descriptors1, descriptors2, 2)

#-- Lowe의 비율 테스트 방식을 활용하여 매칭점 Thresholding
ratio_thresh = 0.7
good_matches = [m for m,n in matches if m.distance < ratio_thresh * n.distance]

#-- Draw matches
img_matches = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1]+img2.shape[1], 3), dtype=np.uint8)
cv.drawMatches(img1, keypoints1, img2, keypoints2, good_matches, img_matches, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

#-- Show detected matches
cv.imshow('Good Matches', img_matches)
cv.waitKey()
```
