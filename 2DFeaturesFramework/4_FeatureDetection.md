# FeatureDetection
![Keypoints1](https://docs.opencv.org/3.4/Feature_Detection_Result_a.jpg)
![Keypoints2](https://docs.opencv.org/3.4/Feature_Detection_Result_b.jpg)   

* cv::FeatureDetector 함수를 이용하여 Interest Point를 찾아냅니다:   
	* cv::xfeatures2d::SURF, cv::xfeatures2d::SURF::detect를 이용한 detection과정 진행.   
	* cv::drawKeypoints를 이용하여 detected Point를 visualize   

* **주의** SURF feature를 이용하기 위해서는 OpenCV contrib module을 이용하여야 합니다. (대안으로는 ORB, KAZE, ...등) 3.0 버전 이후부터 Contrib Module이 존재합니다.   


# Theory
From: [FeatureDetection_OpenCV](https://docs.opencv.org/3.4/d7/d66/tutorial_feature_detection.html)   

```python
# python

#-- Detect the keypoints using SURF Detector
minHessian = 400
detector = cv.xfeatures2d_SURF.create(hessianThreshold=minHessian)
keypoints = detector.detect(src)

#-- Draw keypoints
img_keypoints = np.empty((src.shape[0], src.shape[1], 3), dtype=np.uint8)
cv.drawKeypoints(src, keypoints, img_keypoints)

#-- Show detected (drawn) keypoints
cv.imshow('SURF Keypoints', img_keypoints)
```

# Usage

SURF이외의 알고리즘은 다음을 참고하시기 바랍니다. [Feature2D](https://docs.opencv.org/3.4/d0/d13/classcv_1_1Feature2D.html#a5968e9bc8497a8eb845272b9442559f3)   

* create()
```cpp
//cpp
cv::xfeatures2d::SURF::create(hessianThreshold, nOctaves, nOctavelayers, extended, upright)
```
```python
# python
cv.xfeatures2d.SURF_create([, hessianThreshold[, nOctaves[, nOctaveLayers[, extended[, upright]]]]]) -> retval
```
```
# Parameter


hessianThreshold	Threshold for hessian keypoint detector used in SURF.
nOctaves	Number of pyramid octaves the keypoint detector will use.
nOctaveLayers	Number of octave layers within each octave.
extended	Extended descriptor flag (true - use extended 128-element descriptors; false - use 64-element descriptors).
upright	Up-right or rotated features flag (true - do not compute orientation of features; false - compute orientation).
```

* detect()
```cpp
//cpp
cv:Feature2D::detect(image,keypoints,mask)
```
```python
# python
cv.Feature2D.detect(image[,mask]) -> keypoints
```
```
# Parameter

image	Image.
keypoints	The detected keypoints. In the second variant of the method keypoints[i] is a set of keypoints detected in images[i] .
mask	Mask specifying where to look for keypoints (optional). It must be a 8-bit integer matrix with non-zero values in the region of interest.
```

* 위 두 메소드를 제외한 다른 Class Reference Method들 또한 상위의 링크를 참고하시면 됩니다.
