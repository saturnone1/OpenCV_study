# Enumeration   
Enumeration은 "상수" 집합을 정의하는 것을 뜻하며 이는 고유한 값으로 절대 변하지 않는 집합이다.

# Morph
모핑은 이미지 필터링의 기본으로 dilate와 erode가 있다.

# Morph Shapes

모핑을 하기 위해서는 필터링 할 영역을 지정하여야 한다.    
이는 바이너리 형태의 이미지에서 1인 부분을 가운데 지점으로 잡은 후에 처리한다.   
가운데 지점 1이 가지는 Shape에 해당하는 영역을 모두 1로 처리하거나 (dilate)   
가운데 지점이 가지는 Shape 중에서 0이 하나라도 있으면 0으로 처리하는 (erode) 방법이 존재한다.   

```cpp
enum  	cv::MorphShapes {
  cv::MORPH_RECT = 0, //사각형 형태 ㅁ
  cv::MORPH_CROSS = 1, //직교 형태 +
  cv::MORPH_ELLIPSE = 2 // 타원 형태 ㅇ
}
```

# Morph Types

```cpp
enum  	cv::MorphTypes {
  cv::MORPH_ERODE = 0, //침식
  cv::MORPH_DILATE = 1, //팽창
  cv::MORPH_OPEN = 2, 
  cv::MORPH_CLOSE = 3,
  cv::MORPH_GRADIENT = 4,
  cv::MORPH_TOPHAT = 5,
  cv::MORPH_BLACKHAT = 6,
  cv::MORPH_HITMISS = 7
}
```


