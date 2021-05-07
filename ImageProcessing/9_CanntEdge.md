# Canny Edge Detector

* Low error rate: Edge를 찾는데 좋은 성능
* Good Localization: 실제 Edge 위치와 측정된 Canny Edge위치의 적은 차이
* Minimal response: Edge 한 개마다 단 한번의 Detector 동작


# Steps

1. 노이즈 필터링: Gaussian Filter 적용      	
   ![gaussian](https://github.com/saturnone1/OpenCV_study/blob/e4839960d7e5e62495bd27d1251a76e513c5924f/ImageProcessing/image/canny_gaussian.png)   
2. Intensity 측정. Sobel 방법 사용   
	![Sobel](https://github.com/saturnone1/OpenCV_study/blob/e4839960d7e5e62495bd27d1251a76e513c5924f/ImageProcessing/image/canny_sobel.png)   
	![result](https://github.com/saturnone1/OpenCV_study/blob/e4839960d7e5e62495bd27d1251a76e513c5924f/ImageProcessing/image/canny_result.png)   
4. **Non-Maximum suppression** 적용. Edge의 후보들 중에서 값이 낮게 측정된 것들을 없애버린다. Candidate Edge들 만이 남게 된다.   
5. **Hysteresis** 3번의 적용 원칙:
```
	a. Pixel Gradient(Sobel적용 값)이 upper Threshold보다 크다면, Edge로 승인된다.   
	b. Pixel Gradient(Sobel적용 값)이 lower Threshold보다 작다면, 탈락한다.   
	c. lower Threshold < Pixel Gradient < upper Threshold 라면, 이 픽셀 위치가 a번을 통과한 픽셀과 붙어 있을 경우에만 Edge로 승인된다.   
```


# Usage

```cpp
cv::Canny(image,threshold1,threshold2,apertureSize = 3 , L2gradient = false)

apertureSize: canny Edge에서 사용할 Sobel Gradient Size
L2gradient: (True: √g1^2 + g2^2)  (False: |g1|+|g2|)
```

```python
cv.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) -> edges
cv.Canny(dx, dy, threshold1, threshold2[, edges[, L2gradient]]) -> edges
```
