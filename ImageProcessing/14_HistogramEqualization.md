# Histogram Equalization
```cpp
//cpp
cv::equalizeHist(src,dst)
```
```python
#python
cv.equalizeHist(src[,dst])->dst
```

## What is an Image Histogram?
* 히스토그램은 도수를 그래프 표로 나타낸 것이다.
* 이미지의 픽셀 값의 분포를 나타낸 히스토그램은 다음과 같다.

![histogram](https://docs.opencv.org/3.4/Histogram_Equalization_Theory_0.jpg)   

## What is Histogram Equalization?
* Histogram Equalization은 Intensity가 높은 부분을 낮은 부분으로 분포를 넓히는 알고리즘이다.   
* 이를 통해 이미지의 Contrast(대비)를 높일 수 있다.   

![intensity](https://docs.opencv.org/3.4/Histogram_Equalization_Theory_1.jpg)   


## How does it work?
* Equalization은 기본적으로 Mapping 방식을 포함한다. 특정 Intensity 값을 규칙에 따라 퍼지도록 조절하여야 하기 때문이다. 
* Remapping 과정은 반드시 Cumulative distribution function(CDF)를 통해 수행되어야 한다.

![cumulative](https://docs.opencv.org/3.4/Histogram_Equalization_Theory_2.jpg)   
**누적 분포 함수**

누적 분포 함수 CDF는 위와 같다. 그럼 이 누적분포를 어떻게 사용하는가? 간단하다. 0~255의 각 Intensity 마다 누적 분포가 정해질 것이고, 누적분포 확률을 각 Intensity(pixel Value)에 곱해준 후에 0~255의 값 안으로 Normalize해 주면 완성된다. 그것을 표현한 식이 다음과 같다.   

**equalized(x,y)=H′(src(x,y))**    


