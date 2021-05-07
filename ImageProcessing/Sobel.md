# Sobel Derivative

![derivate](https://docs.opencv.org/3.4/Sobel_Derivatives_Tutorial_Theory_0.jpg)   

이미지의 픽셀 값의 각 좌표는 수치입니다. GrayScale로 변환했을 시에는 각 좌표가 0~255 사이의 값을 가집니다.   

여기서 고등학교 수준의 수학 개념이 필요합니다.   
```
첫번째 Pixel 값: 120   
두번째 Pixel 값: 150
세번재 pixel 값: 200
```

이라고 했을 때 각 *픽셀 값*을 *y좌표값*으로 설정하고, 첫번째 부터 세번째까지 *픽셀을 흩어나간 시간*을 *t*라고 하고 *x좌표값*이라 하면 각 좌표는 2 Dimension에서 **(t,pixel)** 형태를 갖습니다.   

이를 세 개의 pixel값만이 아닌, 여러개의 픽셀값으로 Line을 그리면 다음과 같습니다.   

![function](https://docs.opencv.org/3.4/Sobel_Derivatives_Tutorial_Theory_Intensity_Function.jpg)    

**x축: 시간(t) y축: 픽셀값**      

위와 같이 픽셀 값의 변화량이 가장 큰 지점이 분명히 존재하게 됩니다.   
**Sobel Derivative는 픽셀 값의 변화량이 가장 큰 지점을 가장자리**로 추정하는 것입니다.    
미분 결과는 다음과 같습니다.   

![funcDerivative](https://docs.opencv.org/3.4/Sobel_Derivatives_Tutorial_Theory_dIntensity_Function.jpg)   

## Sobel Operator

변화량이 큰 지점이 곧 가장자리라고 했습니다. Sobel은 이 변화량이 큰 지점을 Kernel로부터 output Image를 얻어 가장자리로 만들고자 합니다.   

* Sobel은 Discrete Differentiation Operator(추정 미분)입니다. 정확한 가장자리르 찾는데에는 어려움이 생길 수 밖에 없습니다.   
* Sobel Operator는 Gaussian Smoothing과 Differentiation을 포함합니다.   

### Formulation
1. Horizontal, Vertical에 각각 Kernel 적용하여 Gaussian output Image 출력
	* Horizontal   
	I: Image   
	![hor](https://github.com/saturnone1/OpenCV_study/blob/78a597d205987cbc8ed3b518d6d107eaf9c21dce/ImageProcessing/image/Sobel_hor.png)   
	* Vertical   
	![ver](https://github.com/saturnone1/OpenCV_study/blob/78a597d205987cbc8ed3b518d6d107eaf9c21dce/ImageProcessing/image/Sobel_ver.png)   
2. 결과 Gaussian output Image 생성: x,y 모두 고려한 방법, 두가지 중 한가지를 선택하여 연산   
![result](https://github.com/saturnone1/OpenCV_study/blob/78a597d205987cbc8ed3b518d6d107eaf9c21dce/ImageProcessing/image/Sobel_result.png)   
```cpp
cv::Sobel(src, dst, ddepth, dx, dy, ksize, scale, delta, borderType)
```
```
# Parameters
src	input image.
dst	output image of the same size and the same number of channels as src .
ddepth	output image depth, see combinations; in the case of 8-bit input images it will result in truncated derivatives.
dx	order of the derivative x.
dy	order of the derivative y.
ksize	size of the extended Sobel kernel; it must be 1, 3, 5, or 7.
scale	optional scale factor for the computed derivative values; by default, no scaling is applied (see getDerivKernels for details).
delta	optional delta value that is added to the results prior to storing them in dst.
borderType	pixel extrapolation method, see BorderTypes. BORDER_WRAP is not supported.
```
```
#부가 설명
ksize = CV_SCHARR 로 잡았을 때, 3x3의 SCHARR 커널이 적용됩니다.
또한 Ksize가 1일 때는 Kernel이 1x1 형태가 아닌 1x3 또는 3x1형태가 각 x,y에 적용됩니다.
```

## Scharr

Kernel Size가 3일 때, Sobel Kernel은 부정확성이 높아집니다. 당연한 것이, Sobel은 Derivatie 미분값을 근사하여 사용하기 때문입니다. 이는 다음의 **Scharr()** Function을 이용하면 해결됩니다. Kernel은 다음과 같습니다.   
![Scharr](https://github.com/saturnone1/OpenCV_study/blob/78a597d205987cbc8ed3b518d6d107eaf9c21dce/ImageProcessing/image/Scharr.png)   

```cpp
//아래 두 함수는 동일합니다
cv::Scharr(src, dst, ddepth, dx, dy, scale, delta, borderType)
cv::Sobel(src, dst, ddepth, dx, dy, CV_SCHARR, scale, delta, borderType)
```

#결과

![lena_line](https://docs.opencv.org/3.4/Sobel_Derivatives_Tutorial_Result.jpg)    



