# Finding contours 윤곽선 검출

![fish](https://docs.opencv.org/3.4/Find_Contours_Original_Image.jpg)
![contour](https://docs.opencv.org/3.4/Find_Contours_Result.jpg)   

위와 같은 더 자세한 윤곽선을 얻고자 할 때 사용합니다.   
CannyEdge에서 끝나지 않고 CannyEdge로부터 만들어지는 Binary 이미지를 사용하여 Contours를 실행하는데, 우리는 이 Contours를 이용하여 Object Detection에 활용할 수 있기 때문입니다.   
CannyEdge 처럼 단순히 이미지의 모든 가장자리를 표현하는데 그치지 않고, 마치 등고선과 같이 가장자리를 구분하는 알고리즘을 수행합니다. 각 가장자리는 Hierarchy 계층 구조를 가지게 되며, 결국 각 가장자리는 구분되고 그것이 이미지 상에 보이는 물체의 특징이 되는 것입니다.   

코드를 보면 이해가 더 쉽습니다.   

# findContours

```cpp
//cpp
cv::findContours(image, contours,hierarchy,mode,method,offset=Point())
```
```python
# python
cv.findContours(image, mode, method[, contours[, hierarchy[, offset]]]) -> image, contours, hierarchy
```
```
# Parameters
image	소스 이미지, 8-bit single-channel이어야만 합니다. 0이 아닌 모든 픽셀들은 1로 취급되며, 0인 픽셀들은 그대로 가지기 때문에 Binary 이미지로 변환되게 됩니다. compare, inRange, threshold , adaptiveThreshold, Canny 등 Gray이미지나 단 Channel 이미지를 가져다가 만들어낸 Binary 이미지를 넣어주는 것이 좋습니다. mode 파라미터가 RETR_CCOMP, RETR_FLOODFILL라면 소스 이미지는 32-bit integer 이미지 여도 됩니다.(CV_32SC1).
contours	측정한 Contour들을 저장합니다. 각 contour는 Vector Point 형태로 저장됩니다.(e.g. std::vector<std::vector<cv::Point> >)
hierarchy	4개로 표현된 Vecotr를 output 합니다.(e.g. std::vector<cv::Vec4i>) 각 Contour들의 네트워크 정보를 담습니다. Contour의 수 만큼 많은 요소가 있습니다. i번째 Contour,즉 contours[i]는 hierarchy[i][0] , hierarchy[i][1] , hierarchy[i][2] , and hierarchy[i][3]는 0으로 설정됩니다. 동일한 계층 수준, 각각 첫 번째 하위 윤곽선 및 상위 윤곽선에서 다음 및 이전 윤곽선의 윤곽선에있는 인덱스를 기반으로합니다. 윤곽선 i에 다음, 이전, 상위 또는 중첩 윤곽선이 없으면 hierarchy [i]의 해당 요소는 음수가됩니다.
mode	검색 모드입니다. 추가적으로 설명합니다.
method	Contour 근사 방법을 선택합니다. 추가적으로 설명합니다.
offset	모든 윤곽 점이 이동되는 선택적 오프셋입니다. 이는 이미지 ROI에서 윤곽선을 추출한 다음 전체 이미지 컨텍스트에서 분석해야하는 경우에 유용합니다.
```

# Draw Contours
```cpp
//cpp
cv::drawContours(image,contours,contourldx,color,thickness,lineType,hierarchy,maxLevel,offset)
```
```python
# python
cv.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) -> image
```
```
# Parameters

image	destination image
contours	모든 입력 윤곽. 각 윤곽선은 점 벡터로 저장됩니다.
contourIdx	그릴 윤곽을 나타내는 매개 변수입니다. 음수이면 모든 윤곽선이 그려집니다.
color	윤곽선의 색상.
thickness	윤곽선이 그려지는 선의 두께입니다. 음수이면 (예 : thickness = FILLED ) 윤곽선 내부가 그려집니다.
lineType	라인 연결. LineTypes 참조
hierarchy	계층에 대한 선택적 정보입니다. 윤곽선 중 일부만 그리려는 경우에만 필요합니다 (maxLevel 참조).
maxLevel	그려진 윤곽선의 최대 수준. 0이면 지정된 윤곽만 그려집니다. 1이면 이 함수는 윤곽선과 모든 중첩 윤곽선을 그립니다. 2인 경우 함수는 윤곽선, 모든 중첩 윤곽선, 모든 중첩된 윤곽선 등을 그립니다. 이 매개변수는 사용 가능한 계층이 있는 경우에만 고려됩니다.
offset	선택적 윤곽 이동 매개 변수. 그려진 모든 윤곽선을 지정된만큼 이동 offset=(dx,dy)
```

# RetrivalModes 검색 모드
Contour시 사용할 검색 알고리즘을 선택합니다.   
findcontour()에서 mode에 넣으면 됩니다.   
(Python 예: cv.RETR_EXTERNAL)   

* RETR_EXTERNAL: 극단적인 외부 윤곽만 검색합니다. hierarchy[i][2]=hierarchy[i][3]=-1모든 윤곽에 대해 설정 됩니다.    
* RETR_LIST: hierarchy 관계를 설정하지 않고 모든 윤곽선을 검색합니다.   
* RETR_CCOMP: 모든 윤곽선을 검색하여 2 단계 계층 구조로 구성합니다. 최상위 수준에는 구성 요소의 외부 경계가 있습니다. 두 번째 수준에는 구멍의 경계가 있습니다. 연결된 구성 요소의 구멍 내부에 다른 윤곽선이있는 경우에도 여전히 최상위 수준에 배치됩니다.    
* RETR_TREE: 모든 윤곽선을 검색하고 중첩 된 윤곽선의 전체 계층 구조를 재구성합니다.   
* RETR_FLOODFILL: 


# ContourApproximationModes 근사 방법
Contour시에 사용할 알고리즘입니다. Contour 처리 방식에 영향을 줍니다   
findcontour()의 method 파라미터입니다.   

* CHAIN_APPROX_NONE: 절대적으로 모든 윤곽점을 저장합니다. 즉, 등고선의 2개의 후속점 (x1, y1) 및 (x2, y2)는 수평, 수직 또는 대각선 인접 요소가됩니다. 즉, max(abs(x1-x2), abs(y2-y1)) == 1.   
	- 모든 인접한 점을 저장하기 때문에 선형으로 나타납니다

* CHAIN_APPROX_SIMPLE: 수평, 수직 및 대각선 세그먼트를 압축하고 끝점 만 남깁니다. 예를 들어, 직립 직사각형 윤곽은 4 개의 포인트로 인코딩됩니다.

* CHAIN_APPROX_TC89_L1: Teh-Chin 체인 근사 알고리즘의 특징 중 하나를 적용합니다.
* CHAIN_APPROX_TC89_KCOS: Teh-Chin 체인 근사 알고리즘의 특징 중 하나를 적용합니다.

```
TenChin Algorithm: C-H Teh and Roland T. Chin. On the detection of dominant points on digital curves. Pattern Analysis and Machine Intelligence, IEEE Transactions on, 11(8):859–872, 1989.
```

# LineTypes 선 형태
선의 모양을 결정합니다. Contour뿐 아니라 많이 사용됩니다.    

* FILLED 
* LINE_4 : 4-connected line
* LINE_8 : 8-connected line
* LINE_AA: antialiased line





