# Remapping

## What is Remapping?

* 이미지의 한 위치에서 새로운 이미지의 위치로 각 픽셀들을 옮기는 작업.   
* 처리 과정에 따라 Non-Integer를 Interpolation하여 Integer로 바꾸어 주어야만 한다. 항상 결과 이미지와 1대1 대응이 되는 것이 아니기 때문이다.   
* 다음과 같은 표현이 가능하다. *g(x,y)=f(h(x,y))* (g:Remapped Image, f:source image, h: mapping function)   
* 임의의 규칙성에 따라 픽셀 위치를 바꾸어주는 과정이기 때문에 개발자의 생각에 따라 다양한 방법이 존재한다.   

## Example

**h(x,y)=(I.cols−x,y)**   

![remapping](https://docs.opencv.org/3.4/Remap_Tutorial_Theory_0.jpg)   
**Non Remapped**      

![remapping2](https://docs.opencv.org/3.4/Remap_Tutorial_Theory_1.jpg)   
**Remapped**      


