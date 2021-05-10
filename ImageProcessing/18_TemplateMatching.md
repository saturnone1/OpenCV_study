# Template Matching

```cpp
//cpp
cv::matchTemplate(image,templ,result,method,mask=noArray())
```
```python
# python
cv.matchTemplate(image, templ, method[, result[, mask]]) -> result
```
```
# Parameter

image	Image where the search is running. It must be 8-bit or 32-bit floating-point.
templ	Searched template. It must be not greater than the source image and have the same data type.
result	Map of comparison results. It must be single-channel 32-bit floating-point. If image is W×H and templ is w×h , then result is (W−w+1)×(H−h+1) .
method	Parameter specifying the comparison method, see TemplateMatchModes
mask	Mask of searched template. It must have the same datatype and size with templ. It is not set by default. Currently, only the TM_SQDIFF and TM_CCORR_NORMED methods are supported.
```

## What is template matching?

Template image(patch)로 설정한 이미지와 비슷한(match)부분을 찾습니다.   

## How does it work?

* Source image(I): 우리가 Template과 대조시켜 원하는(match) 부분을 찾아야 하는 이미지   
* Template image(T): Patch, Source Image와 비교할 목표가 되는 이미지   

![doge](https://docs.opencv.org/3.4/Template_Matching_Template_Theory_Summary.jpg)   

* Matching Area를 찾기 위해서, 다음과 같이 Source Image를 Template을 Sliding 시켜 찾아내야 합니다.   
![slide](https://docs.opencv.org/3.4/Template_Matching_Template_Theory_Sliding.jpg)   

* 계속 sliding(기준 Pixel위치를 바꿈)하면서, 이미지 비교를 통해 "Good" or "Bad"로 나누는 것처럼 하여도 된다.(빠르다)   
* 다음과 같이 전체 이미지 픽셀 위치에 대해 Good or Bad를 수치로 만들고, 그 수치 데이터를 이미지화 할 수도 있다.(느리다)   

![im](https://docs.opencv.org/3.4/Template_Matching_Template_Theory_Result.jpg)   

위의 이미지는 수치화 하는 Method 중에서 TM_CCORR_NORMED 방법으로 이미지화 한 것이다. 위의 이미지에서 보이는 것처럼, 빨간 색으로 표시한 부분이 가장 흰색의 픽셀 값을 가진다. 저 이미지 처럼 Template의 왼쪽 위 픽셀을 기준으로 만들어진 이미지이기 때문에, 실제 동일한 사진의 위치는 검은색 상자에 해당한다.    
이미지에서 가장 큰 값의 위치를 찾고자 하면, minMaxLoc()을 사용하면 된다.   

## How does the mask work?

1. source 이미지 (I) : template 이미지와 일치하는 항목을 찾을 것으로 예상되는 이미지   
2. templaye 이미지 (T) : source 와 비교할 patch 이미지   
3. mask 이미지 (M) : Template을 Masking하는 마스크의 회색 음영 이미지    

* 현재 두 가지 Method 만이 Mask를 허용합니다: TM_SQDIFF 및 TM_CCORR_NORMED   
* Mask는 Template과 크기가 같아야 합니다.   
* Mask는 CV_8U 또는 CV_32F 깊이와 템플릿 이미지와 동일한 수의 채널을 가져야합니다. CV_8U의 경우 Mask 값은 Binary, 즉 0과 0이 아닌 값으로 처리됩니다. CV_32F의 경우 값은 [0..1] 범위에 속해야하며 템플릿 픽셀에 해당 마스크 픽셀 값이 곱해집니다. 샘플의 입력 이미지는 CV_8UC3 유형이므로 마스크도 컬러 이미지로 읽습니다.   

![mask](https://docs.opencv.org/3.4/Template_Matching_Mask_Example.jpg)   

# OpenCV에서 사용할 수 있는 Matching Method는 무엇입니까?

다음의 Matching Method 중에서 골라서 사용하시면 됩니다.   

![matchingmethod](https://github.com/saturnone1/OpenCV_study/blob/360422f39e2b3336af23c6d539ca47e039199d82/ImageProcessing/image/templateMatching.png)   
