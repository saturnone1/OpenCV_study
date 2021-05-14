# Creating your own corner detector

![harris](https://docs.opencv.org/3.4/My_Harris_corner_detector_Result.jpg)
![tomasi](https://docs.opencv.org/3.4/My_Shi_Tomasi_corner_detector_Result.jpg)   

* OpenCV 함수 cv::cornerEigenValsAndVecs를 사용하여 고유 값과 고유 벡터를 찾아 픽셀이 모서리인지 확인합니다.
* OpenCV 함수 cv::cornerMinEigenVal을 사용하여 모서리 감지를위한 최소 고유 값을 찾습니다.
* 위의 두 기능을 사용하여 자체 버전의 Harris 감지기와 Shi-Tomasi 감지기를 구현합니다.

## cornerEigenValsAndVecs()

Corner Detection을 위해 EigenValue와 EigenVector를 이미지에 대해 계산합니다.   

```cpp
//cpp
cv::cornerEigenValsAndVecs(src,dst,blockSize,ksize,borderType)
```
```python
# python
cv.cornerEigenValsAndVecs(src, blockSize, ksize[, dst[, borderType]]) -> dst
```

모든 픽셀 p에 대해서, cornerEigenValsAndVecs 함수는 Blocksize x Blocksize 이웃 S(p)를 고려합니다. 그것은 Covariation Matrix라는 공분산 행렬을 이웃 S(p) 대해 미분하여 만들어 냅니다.     

```
# Parameter

src	Input single-channel 8-bit or floating-point image.
dst	Image to store the results. It has the same size as src and the type CV_32FC(6) .
blockSize	Neighborhood size (see details below).
ksize	Aperture parameter for the Sobel operator.
borderType	Pixel extrapolation method. See BorderTypes. BORDER_WRAP is not supported.

```

## cornerMinEigenVal()

Corner Detection을 위해서, Gradient Matrix의 Minimal Eigenvalue를 계산합니다. 위의 EigenValAndVec과 비슷해 보이지만, Covariance Matrix의 미분에서 최소의 Eigen Value만들 계산하고 저장합니다.

```cpp
//cpp
cv::cornerMinEigenVal(src,dst,blockSize,ksize=3,borderType)
```
```python
# python
cv.cornerMinEigenVal(src, blockSize[, dst[, ksize[, borderType]]]) -> dst
```
```
# Parameters

src	Input single-channel 8-bit or floating-point image.
dst	Image to store the minimal eigenvalues. It has the type CV_32FC1 and the same size as src .
blockSize	Neighborhood size (see the details on cornerEigenValsAndVecs ).
ksize	Aperture parameter for the Sobel operator.
borderType	Pixel extrapolation method. See BorderTypes. BORDER_WRAP is not supported.
```
