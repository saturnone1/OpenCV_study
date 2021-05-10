# Affine Transformations

* Translation, Rotation, Shear, Scale, Reflect Matrix 변환
* 평행선 변환. 도형의 평행선의 형태는 항상 유지된다.

## Theory
![Transformation](https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/2D_affine_transformation_matrix-ko-001.svg/350px-2D_affine_transformation_matrix-ko-001.svg.png)   
**Transformation Matrix**   

위와 같이 매우 많은 종류의 변환 Matrix가 존재한다. 이들은 2차원 Pixel들을 3차원 Matrix로 변환 시키는 장치로 보면 된다. 사용 방법은 다음과 같다.

![affine](https://people.gnome.org/~mathieu/libart/art-affine-matrix.png)   
**Usage**   

![3d](https://github.com/saturnone1/OpenCV_study/blob/f426e3a9fd8d0a36ae73c19b36e9ecc2765e1890/ImageProcessing/image/affine3d.png)   
**Affine Matrix**   

(x,y)의 픽셀을  (x,y,1)로 바꾸어 계산한 것을 볼 수 있다.   
첫 번째 사진의 Matrix들을 여러 개 Matrix Multiplication으로 곱하여 만들어낸 Matrix를 Affine Transformation Matrix라고 부르게 되며, 2차원 표현 방법도 존재한다.   

![2d](https://github.com/saturnone1/OpenCV_study/blob/f426e3a9fd8d0a36ae73c19b36e9ecc2765e1890/ImageProcessing/image/affine_2d.png)   
**2D Vector**   

평행선을 유지한다는 내용은, 다음과 같이 점들이 이루는 선들의 평행이 유지됨을 의미한다.   

![Affine](https://github.com/saturnone1/OpenCV_study/blob/f426e3a9fd8d0a36ae73c19b36e9ecc2765e1890/ImageProcessing/image/affine.png)   
**평행선 유지**   

참고: [Dark Programmer](https://darkpgmr.tistory.com/79)
