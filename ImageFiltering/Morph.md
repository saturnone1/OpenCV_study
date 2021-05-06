# Enumeration   
Enumeration은 "상수" 집합을 정의하는 것을 뜻하며 이는 고유한 값으로 절대 변하지 않는 집합이다.

# Morph
모핑은 이미지 필터링의 기본으로 dilate와 erode가 있다.

# Morph Shapes

모핑을 하기 위해서는 필터링 할 영역을 지정하여야 한다.    
이는 바이너리 형태의 이미지에서 가운데 지점 픽셀 하나를 기준으로 잡은 후에 처리한다.   
가운데 지점 픽셀 값이 가지는 Shape에 해당하는 영역을 모두 그 픽셀값으로 바꾸거나 (dilate)   
가운데 지점이 가지는 Shape 영역에 다른 픽셀값이 하나라도 있으면 다른 픽셀값으로 바꾸는는 (erode) 방법이 존재한다.   

```cpp
enum  	cv::MorphShapes {
  cv::MORPH_RECT = 0, //사각형 형태 ㅁ
  cv::MORPH_CROSS = 1, //직교 형태 +
  cv::MORPH_ELLIPSE = 2 // 타원 형태 ㅇ
}
```
위를 structural element 즉, 구조화 요소라 합니다.

# Morph Types

```cpp
enum  	cv::MorphTypes {
  cv::MORPH_ERODE = 0, //침식
  cv::MORPH_DILATE = 1, //팽창
  cv::MORPH_OPEN = 2, //침식 후 팽창
  cv::MORPH_CLOSE = 3, //팽창 후 침식
  cv::MORPH_GRADIENT = 4, // 팽창된 부분과 침식된 부분의 차이를 출력한다 (팽창 - 침식)
  cv::MORPH_TOPHAT = 5, // src−open(src,element)
  cv::MORPH_BLACKHAT = 6, // close(src,element)−src
  cv::MORPH_HITMISS = 7 
}
```

* Opening
![Opening](https://docs.opencv.org/master/Morphology_2_Tutorial_Theory_Opening.png)
*dst=open(src,element)=dilate(erode(src,element))*   
- 화면에 보이는 미세하게 작은 물체를 없애는 데에 적합하다. (검은 배경에 하얀색 작은 물체)

* Closing
![Closing](https://docs.opencv.org/master/Morphology_2_Tutorial_Theory_Closing.png)
*dst=close(src,element)=erode(dilate(src,element))*
- 하얀 배경에 검정색 미세한 물체를 없애는 데에 적합하다.

* Morphological Gradient
![Morphological Gradient](https://docs.opencv.org/master/Morphology_2_Tutorial_Theory_Gradient.png)
*dst=morphgrad(src,element)=dilate(src,element)−erode(src,element)*
- 물체의 가장자리를 식별하는 데에 적합하다.

* Top Hat
![TopHat](https://docs.opencv.org/master/Morphology_2_Tutorial_Theory_TopHat.png)
*dst=tophat(src,element)=src−open(src,element)*
- 원본 이미지와 Opening된 이미지의 차이를 보여준다.

* Black Hat
![BlackHat](https://docs.opencv.org/master/Morphology_2_Tutorial_Theory_BlackHat.png) 
*https://docs.opencv.org/master/Morphology_2_Tutorial_Theory_BlackHat.png*
- 원본 이미지와 close 이미지의 차이를 보여준다.

* Hit or Miss

Morphological Opeartor들 즉, dilate, erode 두 가지로 결합한 다양한 연산을 했었다. 우리는 이 연산을 단순히 연속적으로 시행한 Opening, Closing 뿐 아니라, 각 연산의 교집합에 해당하는 부분만을 취할 것이다.   
이 방법론이 Hit or Miss 인 것이다.   
   
Hit-or-Miss 변환은 이진 이미지에서 패턴을 찾는 데 유용합니다. 특히, 이웃이 제 1 구조화 요소 (B1)의 모양과 일치하는 동시에 제 2 구조화 요소 (B2)의 모양과 일치하지 않는 픽셀을 찾습니다. 수학적으로 이미지 A에 적용되는 연산은 다음과 같이 표현할 수 있습니다.[HitOrMiss](https://docs.opencv.org/master/db/d06/tutorial_hitOrMiss.html)
   
*A⊛B=(A⊖B1)∩(Ac⊖B2)*
   
그러므로 Hit Or Miss 연산은 다음과 같은 세 과정을 포함합니다.

1. 구조화 요소 B1으로 A 이미지를 Erode합니다.
2. A의 Compliment 즉 Ac를 B2로 Erode합니다.
3. 1번과 2번의 결과에 AND 연산 합니다. 

![HitOrMiss1](https://docs.opencv.org/master/hitmiss_kernels.png)
**Structuring elements (kernels). Left: kernel to 'hit'. Middle: kernel to 'miss'. Right: final combined kernel**



