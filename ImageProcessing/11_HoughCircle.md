# Hough Circle Transform

```cpp
//cpp
cv::HoughCircles(image,circles,method,dp,minDist,param1,param2,minRadius,maxRadius)
```
```python
#python
cv.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) -> circles
```
```bash
# Pararmeters

image	8-bit, single-channel, grayscale input image.
circles	Output vector of found circles. Each vector is encoded as 3 or 4 element floating-point vector (x,y,radius) or (x,y,radius,votes) .
method	Detection method, see HoughModes. Currently, the only implemented method is HOUGH_GRADIENT
dp	Inverse ratio of the accumulator resolution to the image resolution. For example, if dp=1 , the accumulator has the same resolution as the input image. If dp=2 , the accumulator has half as big width and height.
minDist	Minimum distance between the centers of the detected circles. If the parameter is too small, multiple neighbor circles may be falsely detected in addition to a true one. If it is too large, some circles may be missed.
param1	First method-specific parameter. In case of HOUGH_GRADIENT , it is the higher threshold of the two passed to the Canny edge detector (the lower one is twice smaller).
param2	Second method-specific parameter. In case of HOUGH_GRADIENT , it is the accumulator threshold for the circle centers at the detection stage. The smaller it is, the more false circles may be detected. Circles, corresponding to the larger accumulator values, will be returned first.
minRadius	Minimum circle radius.
maxRadius	Maximum circle radius. If <= 0, uses the maximum image dimension. If < 0, returns centers without finding the radius.
```

# Theory

Line에서 사용된 *(r,θ)*와는 다르게, Cirle에서는 아래의 세 parameter들이 사용된다:   

**C:(xcenter,ycenter,r)**   

![houghcircle](https://docs.opencv.org/3.4/Hough_Circle_Tutorial_Theory_0.jpg)   

## What does this program do? (실행 방법)

1. 이미지 로드 및 노이즈 제거를 위한 blur적용    
2. *Hough Circle*알고리즘 적용   

![CircleEx](https://docs.opencv.org/3.4/Hough_Circle_Tutorial_Result.png)   
