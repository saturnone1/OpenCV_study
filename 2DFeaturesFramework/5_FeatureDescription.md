# Feature Description

![Description](https://docs.opencv.org/3.4/Feature_Description_BruteForce_Result.jpg)   

```python
# Python

#-- Step 1: SURF Detector를 이용하여, Keypoint를 만든 후 Descriptor 생성.
minHessian = 400
detector = cv.xfeatures2d_SURF.create(hessianThreshold=minHessian)
keypoints1, descriptors1 = detector.detectAndCompute(img1, None)
keypoints2, descriptors2 = detector.detectAndCompute(img2, None)

#-- Step 2: BruteForce Matcher와 Descriptor Vecotr와 Matching
# Since SURF is a floating-point descriptor NORM_L2 is used
matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_BRUTEFORCE)
matches = matcher.match(descriptors1, descriptors2)

#-- Draw matches
img_matches = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1]+img2.shape[1], 3), dtype=np.uint8)
cv.drawMatches(img1, keypoints1, img2, keypoints2, matches, img_matches)

#-- Show detected matches
cv.imshow('Matches', img_matches)

```

# create Matcher Type(DescriptioorMatcher의 파라미터에 사용)

* BruteForce(it uses L2)
* BruteForce-L1
* BruteForce-Hamming
* BruteForce-Hamming(2)
* FlannBased


## 작성자 첨언
논문을 읽을 순 없으니..... 사용법과 각 파라미터, 함수의 기능 자체를 이해하는 데에 집중하자.
