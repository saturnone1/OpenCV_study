# Back Projection
* calcBackProject()
```cpp
//cpp
cv::calcBackProject(images,nimages,channels,hist,backProject,ranges,scale=1, uniform=true)
```
```python
cv.calcBackProject(images, channels, hist, ranges, scale[, dst]) -> dst
```
```bash
# Parameteres
images	Source arrays. They all should have the same depth, CV_8U, CV_16U or CV_32F , and the same size. Each of them can have an arbitrary number of channels.
nimages	Number of source images.
channels	The list of channels used to compute the back projection. The number of channels must match the histogram dimensionality. The first array channels are numerated from 0 to images[0].channels()-1 , the second array channels are counted from images[0].channels() to images[0].channels() + images[1].channels()-1, and so on.
hist	Input histogram that can be dense or sparse.
backProject	Destination back projection array that is a single-channel array of the same size and depth as images[0] .
ranges	Array of arrays of the histogram bin boundaries in each dimension. See calcHist .
scale	Optional scale factor for the output back projection.
uniform	Flag indicating whether the histogram is uniform or not (see above).
```
* mixChannels()
```cpp
//cpp
cv::mixChannels(src,nsrcs,dst,ndst,fromTo,npairs)
```
```python
# python
cv.mixChannels(	src, dst, fromTo) -> dst
```
```bash
# Parameters

src	input array or vector of matrices; all of the matrices must have the same size and the same depth.
nsrcs	number of matrices in src.
dst	output array or vector of matrices; all the matrices must be allocated; their size and depth must be the same as in src[0].
ndsts	number of matrices in dst.
fromTo	array of index pairs specifying which channels are copied and where; fromTo[k*2] is a 0-based index of the input channel in src, fromTo[k*2+1] is an index of the output channel in dst; the continuous channel numbering is used: the first input image channels are indexed from 0 to src[0].channels()-1, the second input image channels are indexed from src[0].channels() to src[0].channels() + src[1].channels()-1, and so on, the same scheme is used for the output image channels; as a special case, when fromTo[k*2] is negative, the corresponding output channel is filled with zero .
npairs	number of index pairs in fromTo.

```

* 백 프로젝션이란 무엇이며 왜 유용한가
* OpenCV 함수 cv :: calcBackProject 를 사용하여 역 투영을 계산하는 방법
* OpenCV 함수 cv :: mixChannels를 사용하여 이미지의 여러 채널을 혼합하는 방법

## What is Back Projection
* Back Prokection 은 주어진 이미지의 픽셀이 Histogram 모델의 픽셀 분포에 얼마나 잘 맞는지 기록하는 방법입니다.
* Back Projection의 경우 특징을 선택한 후에 히스토그램 모델을 계산 한 다음 이전에 저장해 둔 특징을 사용하여 이미지에서이 해당 특징에 해당하는 지점들을 찾습니다.
* 적용 예 : 피부색 히스토그램 (예 : Hue-Saturation 히스토그램)이있는 경우이를 사용하여 이미지에서 피부색 영역을 찾을 수 있습니다.

## How does it work?
* 다음의 피부 모습을 봅시다
* 아래 이미지를 기반으로 피부 색에 해당하는 Histogram을 얻었다고 가정합니다. HSV 이미지에서 추출한 부분은 Hue-Saturation입니다. 특정한 위치의 H-S를 선택하면 그 부분이 피부 색조의 기준이 될 겁니다.   

![hand1](https://docs.opencv.org/3.4/Back_Projection_Theory0.jpg)   
위 이미지에서 mask를 적용하여 피부 색조에 해당하는 다음 부분만을 추출합니다. 아래의 추출한 히스토그램이 *Model Histogram*입니다.   
![histo1](https://docs.opencv.org/3.4/Back_Projection_Theory1.jpg)   

* 이제 아래와 같은 다른 손 이미지 (테스트 이미지)가 있다고 가정 해 봅시다.(해당 히스토그램 포함):

![hand2](https://docs.opencv.org/3.4/Back_Projection_Theory2.jpg)   
1[histo2](https://docs.opencv.org/3.4/Back_Projection_Theory3.jpg)   

* 이제 우리가 원하는 것은 *Model Histogram*을 이용하여, 테스트 이미지에서 피부 영역을 감지하는 것입니다. 단계는 다음과 같습니다.
1. 테스트 이미지의 각 픽셀 데이터를 수집하고 해당 픽셀의 해당 Model Histogram bin 위치를 찾습니다.   
2. 해당 bin에서 Model Histogram 조회 후, 그 위치의 bin 값을 읽습니다.   
3. 이 bin 값을 새 이미지 ( BackProjection )에 저장합니다. 또한 먼저 Model Histogram을 Normalize 하여 테스트 이미지의 출력을 볼 수 있도록 고려할 수 있습니다.   
4. 위의 단계를 적용하면 테스트 이미지에 대해 다음과 같은 BackProjection 이미지를 얻습니다.   

![backpropa](https://docs.opencv.org/3.4/Back_Projection_Theory4.jpg)   

5. 통계 측면에서 BackProjection에 저장된 값은 우리가 사용하는 모델 히스토그램을 기반으로 테스트 이미지의 픽셀이 피부 영역에 속할 확률을 나타냅니다. 예를 들어, 테스트 이미지에서 밝은 영역은 피부 영역일 가능성이 더 높은 반면(위의 사진처럼) 어두운 영역은 가능성이 적습니다. ("어두운 영역"은 그림자 부분을 이야기합니다. 그림자는 이 인식 방법에 영향을 미칩니다)   
