# Harris Corner Detector
![image](https://docs.opencv.org/3.4/Harris_Detector_Original_Image.jpg)
![corner](https://docs.opencv.org/3.4/Harris_Detector_Result.jpg)   

## What is a feature?

* 컴퓨터 비전에서 일반적으로 우리는 서로 다른 프레임 간의 일치 지점을 찾아야합니다. 왜? 두 이미지가 서로 어떻게 관련되어 있는지 알면 두 이미지를 모두 사용 하여 정보를 추출 할 수 있기 때문입니다.   
* **Matching Point**란 일반적으로 우리가 이미지에서 인식할 수 있는 장면의 *characteristics*특성을 의미합니다. 우리는 이것을 Feature라고 부릅니다.   
* 그렇다면 어떤 특성이 Feature이 될 수 있을까요? 다른 물체와 구분되는 *uniquely recognizable*이어야 합니다.   

## Types of Image Features: Feature의 종류

* Edges
* Corners (interest points)
* Blobs (regions of interest)

## Why is a corner so special?

* 왜냐하면 두 모서리의 교차점이므로 이 두 모서리의 방향이 변경 되는 지점을 나타냅니다 . 따라서 이미지의 기울기(양방향)는 편차가 크므로 이를 감지하는 데 사용할 수 있습니다.

## How does it work?

* Corner를 찾아봅시다. Corner들은 이미지 기울기의 변화를 나타내기 때문에, 우리는 이 "변화"에 중점을 두면 됩니다.


## Usage

```cpp
cv::cornerHarris(src,dst,blockSize,ksize,k,borderType)
```
```python
cv.cornerHarris(src, blockSize, ksize, k[, dst[, borderType]]) -> dst
```
```
# Parameter
src	Input single-channel 8-bit or floating-point image.
dst	Image to store the Harris detector responses. It has the type CV_32FC1 and the same size as src .
blockSize	Neighborhood size (see the details on cornerEigenValsAndVecs ).
ksize	Aperture parameter for the Sobel operator.
k	Harris detector free parameter. See the formula above.
borderType	Pixel extrapolation method. See BorderTypes. BORDER_WRAP is not supported.
```
