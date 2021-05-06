# Extract horizontal and vertical lines by using morphological operations
# Goal
* Erode, Dilate을 Binary가 아닌 GrayScale Image에 적용하는 방법   
* Horizontal, vertical Line을 추출하는 방법   

# Theory
앞에서 이야기 했기 때문에 추가적인 설명은 배제하고, 0과 1로만 이루어진 binary 이미지와 달리, GrayScale Image는 말 그대로 0~255사이의 값만을 가진 흑백 이미지입니다. 따라서 0과 1만으로는 판단하여 Dilation과 Erosion을 수행할 수 없고 Max, Min을 선택하여 처리하게됩니다.   

## Dilation
* Kernel 내 Max값을 가져다가 Anchor pixel 부분을 대체합니다.   
	![DilationBinary](https://docs.opencv.org/3.4/morph21.gif)   
	**Dilation on a Binary Image**   

	![DilationGray](https://docs.opencv.org/3.4/morph6.gif)   
	**Dilation on a Grayscale Image**   

## Erosion
* Kernel 내 Min값을 가져다가 Anchor Pixel 부분을 대체합니다.   
	![ErosionBinary](https://docs.opencv.org/3.4/morph211.png)   
	**Erosion on a Binary Image**   

	![ErosionGrayscale](https://docs.opencv.org/3.4/morph61.png)    
	**Erosion on a Grayscale Image**   

## Structuring Elements 구조화 요소 (Kernel)
* 일반적으로 모든 Filtering에서 가장 많이 보이는 매우 중요한 부분입니다.   
* Structural element는 0과 1로만 이루어진 binary Matrix이며, 지정해준 형태를 가집니다.   
* 당연하게도 픽셀 하나하나 필터링을 위해 Image Size 보다는 매우 작아야 합니다.   
* Matrix의 가운데 지점을 Pixel of Origin 이라고 부르며, 우리가 처리하고자 하는 픽셀의 위치에 해당합니다.   

	![StructuralElement](https://docs.opencv.org/3.4/morph12.gif)   
	**A Diamond-Shaped Structuring Element and its Origin**   

* 구조화 요소는 통상적으로 다음의 모양을 가집니다: Lines/ diamonds/ disks/ periodic lines/ circles/ sizes   
* Input Image를 처리하기에 알맞다고 생각하는 모양을 정하여 진행하시면 됩니다.   
* 예를 들어 Image의 Line을 찾고자 한다면, 직선 형태의 구조화 요소를 적용하시면 됩니다.   

## Line Filter 직선 형태의 구조화 요소 적용
* 원본 이미지   
	![ori](https://docs.opencv.org/3.4/src.png)      
   
* GrayScale   
	![Gray](https://docs.opencv.org/3.4/gray.png)    

```cpp
	cvtColor(src, gray, COLOR_BGR2GRAY);
```

* GrayScale to Binary   
	![Binary](https://docs.opencv.org/3.4/binary.png)   

```cpp
    // Apply adaptiveThreshold at the bitwise_not of gray, notice the ~ symbol
    Mat bw;
    adaptiveThreshold(~gray, bw, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, 15, -2);
```

* Structural Element   
	![SE](https://docs.opencv.org/3.4/linear_horiz.png)   

```cpp
    // Specify size on horizontal axis
    int horizontal_size = horizontal.cols / 30;
    // Create structure element for extracting horizontal lines through morphology operations
    Mat horizontalStructure = getStructuringElement(MORPH_RECT, Size(horizontal_size, 1));
    // Apply morphology operations
    erode(horizontal, horizontal, horizontalStructure, Point(-1, -1));
    dilate(horizontal, horizontal, horizontalStructure, Point(-1, -1));
```

	![SE_result](https://docs.opencv.org/3.4/horiz.png)   
	이미지의 수평 길이의 30분의 1로 쪼갠 사이즈의 element를 만들고, 그 element를 적용시킨 모습이다.   

	![SE_V](https://docs.opencv.org/3.4/linear_vert.png)   
	**위와 같은 수직선상으로도 가능하다**   

```cpp
    // Specify size on horizontal axis
    int horizontal_size = horizontal.cols / 30;
    // Create structure element for extracting horizontal lines through morphology operations
    Mat horizontalStructure = getStructuringElement(MORPH_RECT, Size(horizontal_size, 1));
    // Apply morphology operations
    erode(horizontal, horizontal, horizontalStructure, Point(-1, -1));
    dilate(horizontal, horizontal, horizontalStructure, Point(-1, -1));
```

	![SE_V_result](https://docs.opencv.org/3.4/vert.png)   
	수직으로 30분의 1로 쪼갠 element를 적용시켜 줄이 검은색 neighboor에 Filtering된 모습이다.   
