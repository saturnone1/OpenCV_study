# Shi-Tomasi corner detector
![Shi-Tomasi](https://docs.opencv.org/3.4/good_features_to_track_Shi_Tomasi.jpg)   

```cpp
//cpp
cv::goodFeaturesToTrack(image,corners,qualityLevel,minDistance,mask,blockSize=3,useHarrisDetector=false,k)
```
```python
# python
cv.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]]) -> corners
cv.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, mask, blockSize, gradientSize[, corners[, useHarrisDetector[, k]]]) -> corners
```

이 함수는 이미지 또는 지정된 이미지 영역에서 가장 눈에 띄는 모서리를 찾습니다.   
* 함수는 cornerMinEigenVal 또는 cornerHarris를 사용하여 모든 소스 이미지 픽셀에서 모서리 품질 측정 값을 계산합니다 .   
* 함수는 비 최대 억제를 수행합니다 ( 3 x 3 인접 지역의 로컬 최대 값 이 유지됨).   
* **QualityLevel*max(xy)qualityMeasureMap(x,y)**보다 작은 minimal eigenvalue는 없앤다.   
* 나머지 모서리는 품질 측정에 따라 내림차순으로 정렬됩니다.   

```
# Parameters
image	Input 8-bit or floating-point 32-bit, single-channel image.
corners	Output vector of detected corners.
maxCorners	Maximum number of corners to return. If there are more corners than are found, the strongest of them is returned. maxCorners <= 0 implies that no limit on the maximum is set and all detected corners are returned.
qualityLevel	Parameter characterizing the minimal accepted quality of image corners. The parameter value is multiplied by the best corner quality measure, which is the minimal eigenvalue (see cornerMinEigenVal ) or the Harris function response (see cornerHarris ). The corners with the quality measure less than the product are rejected. For example, if the best corner has the quality measure = 1500, and the qualityLevel=0.01 , then all the corners with the quality measure less than 15 are rejected.
minDistance	Minimum possible Euclidean distance between the returned corners.
mask	Optional region of interest. If the image is not empty (it needs to have the type CV_8UC1 and the same size as image ), it specifies the region in which the corners are detected.
blockSize	Size of an average block for computing a derivative covariation matrix over each pixel neighborhood. See cornerEigenValsAndVecs .
useHarrisDetector	Parameter indicating whether to use a Harris detector (see cornerHarris) or cornerMinEigenVal.
k	Free parameter of the Harris detector.
```
