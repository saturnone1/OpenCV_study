# Convex Hull
![Original](https://docs.opencv.org/3.4/Hull_Original_Image.jpg)
![Result](https://docs.opencv.org/3.4/Hull_Result.jpg)

```cpp
//cpp
cv:convexHull(point, hull, clockwise, returnPoints)
```
```python
# python
cv.convexHull(points[,hull[,clockwise[,returnPoints]]]) -> hull
```

점 집합의 볼록 껍질을 찾습니다.   
cv::convexHull 함수는 **_O(NlogN)_** 복잡도를 갖는 Sklansky 알고리즘을 사용하여 2D점 집합의 볼록 껍질을 찾습니다 .    

* Parameter   
```
point	std :: vector 또는 Mat에 저장된 입력 2D point set .
hull	볼록 껍질을 출력합니다. 인덱스로 구성된 정수 벡터 또는 점으로 구성된 벡터입니다. 첫 번째 경우, 선체 요소는 원래 배열에있는 볼록 선체 점의 0 기반 인덱스입니다 (볼록 선체 점 집합은 원래 점 집합의 하위 집합이므로). 두 번째 경우 선체 요소는 볼록 선체 점 자체입니다.
clockwise	방향 플래그. 참이면 출력 볼록 껍질이 시계 방향으로 향합니다. 그렇지 않으면 시계 반대 방향입니다. 가정 된 좌표계에는 오른쪽을 가리키는 X 축과 위쪽을 가리키는 Y 축이 있습니다.
returnPoints	작동 플래그. 행렬의 경우 플래그가 참이면 함수는 볼록 껍질 점을 반환합니다. 그렇지 않으면 볼록 껍질 점의 인덱스를 반환합니다. 출력 배열이 std :: vector이면 플래그가 무시되고 출력은 벡터 유형에 따라 달라집니다. std :: vector <int>는 returnPoints = false를 의미하고, std :: vector <Point>는 returnPoints = true를 의미합니다.
```

* Note   
point와 hull은 다른 Array이어야만 합니다. 내부 프로세싱은 지원하지 않습니다.

* Usage   
```cpp
//다음과 같이 모든 contour에 대해 hull을 만들어 주어야 합니다.
    for( size_t i = 0; i < contours.size(); i++ )
    {
        convexHull( contours[i], hull[i] );
    }
```

# Creating Bounding boxes and circles for contours
![img](https://docs.opencv.org/3.4/Bounding_Rects_Circles_Source_Image.jpg)
![res](https://docs.opencv.org/3.4/Bounding_Rects_Circles_Result.jpg)   

### Bounding Rect
점 집합의 오른쪽 위 경계 사각형 또는 회색조 이미지의 0이 아닌 픽셀을 계산합니다.   
이 함수는 지정된 점 집합 또는 회색조 이미지의 0이 아닌 픽셀에 대해 가장 위쪽을 기준으로 경계 사각형을 계산하고 반환합니다.    

```cpp
cv::boundingRect(array)
```
```python
cv.boundingRect(array) -> retval
```
* Array에는 GrayScale image 혹은 2D Point set(std::vector or MAT)이 들어가면 됩니다.   

### Enclosing Circle
2D 점 세트를 둘러싸는 최소 영역의 원을 찾습니다.   
이 함수는 반복 알고리즘을 사용하여 2D point set을 최소로 둘러싸는 원을 찾습니다.   

```cpp
//cpp
cv::minEnclosingCircle(points,center,radius)
```
```python
# python
cv.minEnclosingCircle(points) -> center, radius
```

* Parameters   
```
points 2D Point들의 집합입니다. 
center 원의 가운데 점을 출력합니다.
radius 원의 반지름을 출력합니다.
```

# Creating Bounding rotated boxes and ellipses for contours

![img](https://docs.opencv.org/3.4/Bounding_Rotated_Ellipses_Source_Image.jpg)
![result](https://docs.opencv.org/3.4/Bounding_Rotated_Ellipses_Result.jpg)   

```cpp
//cpp
cv::minAreaRect(points)
```
```python
# python
cv.minAreaRect(points)->retval
```

## minAreaRect
입력 된 2D Point Set을 둘러싸는 최소 영역의 회전 된 직사각형을 찾습니다.   
이 함수는 지정된 점 집합에 대해 최소 영역 경계 사각형 (회전 가능)을 계산하고 반환합니다. 개발자는 데이터가 포함 된 Mat 요소 경계에 가까울 때 반환 된 RotatedRect에 음수 인덱스가 포함될 수 있음을 명심해야합니다.

```cpp
cv:fitEllipse(points)
```
```python
# python
cv.fitEllipse(points)->retval
```

## fitEllipse
2D Point Set 주위에 타원을 맞춥니다.   
이 함수는 2D 점 집합에 가장 적합한 타원을 계산합니다(최소 제곱 의미에서). 타원이 새겨진 회전된 사각형을 반환합니다. 개발자는 반환된 ellipse/rotatedRect 데이터에 포함된 Mat 요소의 경계에 가까운 데이터 포인트로 인해 음수 인덱스가 포함될 수 있다는 점을 염두에 두어야합니다.   

* Note   
위 두 방식은 음수 인덱스가 나올 수 있다는 점과, 회전된 정도를 모르기 때문에 사용이 어렵다.

# Image Moments
![image](https://docs.opencv.org/3.4/Moments_Source_Image.jpg)
![contour](https://docs.opencv.org/3.4/Moments_Result1.jpg)
![cli](https://docs.opencv.org/3.4/Moments_Result2.jpg)   

## Moments
다각형 또는 래스터화 된 모양의 세 번째 순서까지 모든 순간을 계산합니다.   
이 함수는 벡터 모양 또는 래스터화 된 모양의 모멘트를 최대 3차까지 계산합니다. 결과는 cv:: Moments 구조로 반환됩니다 .   

```cpp
//cpp
cv::moments(array, binaryImage)
```
```python
# python
cv.moments(array[,binaryImage])->retval
```

* Parameter
```
array 래스터 이미지(단일 채널, 8-bit 또는 부동 소수점 2D배열) 또는 배열 ( 1×N 또는 N×1 )의 2D 점(Point 또는 Point2f).
binaryImage	true이면 0이 아닌 모든 이미지 픽셀이 1로 처리됩니다. 매개 변수는 이미지에만 사용됩니다.
```

* Note
Python 방식의 등고선 Moment 계산에만 적용 가능: 입력 배열의 numpy 유형은 np.int32 또는 np.float32 여야합니다. 

## Contour Area
```cpp
//cpp
cv::contourArea(contour, oriented)
```
```python
# python
cv.contourArea(contour[,oriented]) -> retval
```

이 함수는 등고선 영역을 계산합니다. moments와 마찬가지로 면적은 Green 공식을 사용하여 계산됩니다. 따라서 drawContours 또는 fillPoly를 사용하여 윤곽선을 그리는 경우 반환되는 영역과 0이 아닌 픽셀의 수가 다를 수 있습니다. 또한 이 기능은 자기 내부에 교차선이 있는 등고선에 대해 잘못된 결과를 제공합니다.    

* Parameter
```
contour	std :: vector 또는 Mat에 저장된 2D 점 (등고선 꼭지점)의 입력 벡터입니다 .
oriented	방향 영역 플래그. 참이면 함수는 윤곽선 방향 (시계 방향 또는 시계 반대 방향)에 따라 부호있는 영역 값을 반환합니다. 이 기능을 사용하면 영역의 부호를 사용하여 윤곽선의 방향을 결정할 수 있습니다. 기본적으로 매개 변수는 false이며 절대 값이 리턴됨을 의미합니다.
```

## ArcLength
```cpp
//cpp
cv::arcLength(curve,closed)
```
```python
# python
cv.arcLength(curve,closed)->retval
```

윤곽선 둘레 또는 곡선 길이를 계산합니다. 이 함수는 곡선 길이 또는 닫힌 윤곽선 둘레를 계산합니다.

* Parameter
```
curve	std :: vector 또는 Mat에 저장된 2D 점의 입력 벡터입니다 .
closed	곡선이 닫혔는지 여부를 나타내는 플래그입니다.
```

# Point Polygon Test
![polygon](https://docs.opencv.org/3.4/pointpolygon.png)   

윤곽선 지점 테스트를 수행합니다. 이 함수는 점이 윤곽선 내부, 외부 또는 가장자리에 있는지 (또는 꼭지점과 일치하는지) 여부를 결정합니다. 이에 따라 양수 (내부), 음수 (외부) 또는 0 (가장자리) 값을 반환합니다. measureDist = false이면 반환 값은 각각 +1, -1 및 0입니다. 그렇지 않은 경우 반환 값은 점과 가장 가까운 윤곽 모서리 사이의 부호있는 거리입니다.   

각 이미지 픽셀이 윤곽선에 대해 테스트되는 함수의 샘플 출력은 위 이미지를 참조하십시오.   

```cpp
//cpp
cv::pointPolygonTest(contour,pt,measureDist)
```
```python
# python
cv.pointPolygonTest(contour,pt,measureDist)->retval
```

* Parameter
```
contour
pt
measuredist
```
