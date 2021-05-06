# Image Pyramids

* Use the OpenCV functions pyrUp() and pyrDown() to downsample or upsample a given image.

# Theory

* Upsize, Downsize 두 가지를 수행.   
* 흔히 아는 Sampling 수준의 화질 보정은 되지 않는다.    


# Image Pyramid

## Gaussian Pyramid

* 맨 아래 있는 판이 기존 이미지라고 생각했을 때, 사이즈를 줄일수록 이미지 픽셀이 줄어든다.   
![Pyramid](https://docs.opencv.org/3.4/Pyramids_Tutorial_Pyramid_Theory.png)   

* Gi 번째 image에서 Gi+1번째로 작은 이미지를 만들 때, 다음과 같은 Gaussian Kernel을 적용한다.   


위의 Kernel은 Even-Number의 row와 column을 지운다.

# Example

다음과 같은 Image를 가지고 설명을 이어간다.   
![dog](https://docs.opencv.org/3.4/Pyramids_Tutorial_Original_Image.jpg)   

## DownSampling

```cpp
pyrDown( src, src, Size( src.cols/2, src.rows/2 ) );
```
![dogdown](https://docs.opencv.org/3.4/Pyramids_Tutorial_PyrDown_Result.jpg)   
	* 사이즈를 줄인 모습이다.
## UpSampling
```cpp
pyrUp( src, dst, Size( src.cols*2, src.rows*2 );
```
![dogup](https://docs.opencv.org/3.4/Pyramids_Tutorial_PyrUp_Result.jpg)   
	* DownSampling 사진에서 연속적으로 Upsampling을 수행했다. down된 이미지 그대로 추론 없이 픽셀을 채워넣었기 때문에 원본과 같아질 수 없다.


* Parameter들이 매우 직관적이므로 설명은 넘어가도록 하겠다.   




