# Thresholding
Threshold는 '기준'이라고 생각하면 됩니다.   

```cpp
cv2::threshold(src,dst,thresh,maxval,type)
```
```python
cv.threshold(src,thresh,maxval,type[,dst]) -> retval, dst
```
```python
# Type Parameter
	0: Binary
	1: Binary Inverted
	2: Threshold Truncated
	3: Threshold to Zero
	4: Threshold to Zero Inverted
```

* Simple Segmentation Method   
* object Pixel과 Background Pixel의 Intensity에 기반한 알고리즘입니다.   
* 각 픽셀의 Intensity Value(화소 강도)를 Threshold와 비교하여 수행합니다.   
* 화소 강도는 0~255 값입니다.   

# Types of Thresholding

![Base](https://docs.opencv.org/3.4/Threshold_Tutorial_Theory_Base_Figure.png)   
	**Red:Pixel Value / Blue: Threshold Line**   

## Threshold Binary

![Binary](https://docs.opencv.org/3.4/Threshold_Tutorial_Theory_Binary.png)   
![binary2](https://github.com/saturnone1/OpenCV_study/blob/244e4d845e6cdb6d687dfa9612342134f24d33cf/ImageProcessing/image/Threshold_Binary.png)   
	* src(x,y) 즉, 이미지 픽셀값(intensity)이 *Thresh*보다 높으면 새로운 Pixel Intensity가 *MaxVal*로 설정된다 MaxVal은 0~255 기준으로 255이다.   
	* 반대로 낮으면, 0으로 바꾼다   

## Threshold Binary, Inverted

![Binary_Inverted](https://docs.opencv.org/3.4/Threshold_Tutorial_Theory_Binary_Inverted.png)   
![binarayInverted](https://github.com/saturnone1/OpenCV_study/blob/244e4d845e6cdb6d687dfa9612342134f24d33cf/ImageProcessing/image/Threshold_binary_Inverted.png)   
	* 말 그대로 Binary의 반대이다.

## Truncate

![Truncate](https://docs.opencv.org/3.4/Threshold_Tutorial_Theory_Truncate.png)   
![Truncate2](https://github.com/saturnone1/OpenCV_study/blob/244e4d845e6cdb6d687dfa9612342134f24d33cf/ImageProcessing/image/Threshold_Truncate.png)   
	* Threshold보다 높은 부분을 Threshold로 바꾼다

## Threshold to Zero

![Zero](https://docs.opencv.org/3.4/Threshold_Tutorial_Theory_Zero.png)   
![zero](https://github.com/saturnone1/OpenCV_study/blob/244e4d845e6cdb6d687dfa9612342134f24d33cf/ImageProcessing/image/Threshold_zero.png)   
	* Threshold보다 높은 부분만 그대로 두고 나머지를 0으로 바꾼다

## Threshold to Zero, Inverted

![ZeroInverted](https://docs.opencv.org/3.4/Threshold_Tutorial_Theory_Zero_Inverted.png)   
![zeroinverted](https://github.com/saturnone1/OpenCV_study/blob/244e4d845e6cdb6d687dfa9612342134f24d33cf/ImageProcessing/image/Threshold_Zero_Inverted.png)   
	* Threshold보다 높은 부분만 0으로 만들고 나머지는 그대로 둔다

#### 의문점

Threshold to Max는 왜 없는가...?   

# Thresholding Operations using in Range   
Thresholding은 단순히 Threshold line을 기준으로 나누는 것이 아닌 범위를 잡는 것도 포괄한다.
범위를 잡는 방법으로서, cv::threshold가 아닌 cv::inRange를 사용한다.   

```cpp
cv::inRange(src, lowerb, upperb, dst)
```
```python
cv.inRange(src, lowerb, upperb[, dst]) -> dst
```
```
# Parameters
src	first input array.
lowerb	inclusive lower boundary array or a scalar.
upperb	inclusive upper boundary array or a scalar.
dst	output array of the same size as src and CV_8U type.
```
* Lowerb : 
* Upperb : 

![HSV](https://docs.opencv.org/3.4/Threshold_inRange_HSV_colorspace.jpg)   

* HSV 를 사용하는 것이, 색 범위를 잡는데 RGB보다 유리하다.   
* HSV는 Hue: 색조 / Saturation: 채도 / Value: 명도   

![RGB](https://docs.opencv.org/3.4/Threshold_inRange_RGB_colorspace.jpg)   

* RGB는 위와 같이 Red/Green/Blue 각각의 색 분포를 조절하는 데에는 유리하지만, 전반적인 색 분포를 조절하는데에는 어려움이 있다.   
* 색의 표현을 바꿔주기 위해서 다음의 function을 이용하자.   
```cpp
cv::cvtColor
```




