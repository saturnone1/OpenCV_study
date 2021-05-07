# Hough Line Transform

* Detect Straight Lines
* pre-processing 으로 Edge-Detection 먼저 수행하는 것이 필수적입니다.

# Theory

2차원에서, 한 점은 두 가지 방식으로 표현될 수 있습니다.   

```
a. Cartesian coordinate system: (h,v)   
b. Polar coordinate system: (r,θ)   
```

![system](https://docs.opencv.org/3.4/Hough_Lines_Tutorial_Theory_0.jpg)   

Hough Transform을 수행하기 위해, 위의 직선을 *Polar System*으로 표현합니다:   
우리는 어떤 점 (x,y)를 지나는 무수히 많은 직선을 표현할 수가 있는데 이는 다음과 같습니다.

**r = xcosθ + ysinθ**      
1. **In General: rθ = x0cosθ + y0sinθ**: (x0,y0)를 지나는 직선의 (rθ,θ)표현     
2. x0 = 8, y0 = 6일 때, 또한 (x0,y0)를 지나는 무수히 많은 직선들의 (r,θ)를 표현하면 다음과 같은 곡선이 생성됩니다   
![plane](https://docs.opencv.org/3.4/Hough_Lines_Tutorial_Theory_1.jpg)   

3. x1 = 4, y1 = 9 / x 2 = 12, y2 = 3 를 추가합니다.    
![plane2](https://docs.opencv.org/3.4/Hough_Lines_Tutorial_Theory_2.jpg)   

    세 곡선은 (0.925, 9.6)를 통과합니다. 이 의미는 각 점을 통과하는 직선들 중에 r = 9.25, θ = 9.6일때 만들어진 직선이 완벽히 동일함을 뜻합니다. 이는 또한 점 3개가 하나의 직선 위에 있다라는 뜻으로 해석할 수도 있습니다.


4. 많은 사람들이 3번째 단계까지는 이해하지만 이제 코드로 넘어가는 단계에서 이해하기 힘들어합니다. 저도 이 부분이 이해하기 힘들었고 특별한 설명이 없는 자료가 많습니다.    
이유는 수학적으로 구성된 1,2,3번까지는 x0 처럼 좌표를 특정한 후 같은 직선이 존재하는지 여부만 따졌기 때문입니다. 분명히 이미지는 많은 픽셀들이 존재하기 때문에 무한히 수행해야 할 것만 같고, 또한 Pixel Intensity(픽셀 크기, value) 값도 같은 색의 직선을 출력하기 위해서 필요할 것 같습니다.       

    위의 고민을 해결해 주는 것이 최상단에 적어놓은 "Edge Detection을 먼저 수행해야 한다"의 중요성입니다.   

    예를 들어, Canny Edge로 수행한 output Image는 cv::cvt를 수행하기 전에는 Binary Image입니다.
    Binary Image는 모든 Pixel Value가 0,1로 이루어져 있습니다.    

    따라서 코드 상에서는 Canny Edge로 만들어낸 Binary Image에서 1로 되어있는 픽셀들만 비교하여 그들이 직선상에 있는지만을 검출하게 됩니다.   

# Usage

* Hough Line
```cpp
//cpp
cv::HoughLines(image, lines, rho, theta, threshold, srn, stn, min_theta, max_theta)
```
```python
#python
cv.HoughLines(image, rho, theta, threshold[,lines[,srn[,stn[,min_theta[,max_theta]]]]]) -> lines
```
```
# Parameters
dst   Output of the edge detector. It should be a grayscale image (although in fact it is a binary one)
lines   A vector that will store the parameters (r,θ) of the detected lines
rho   The resolution of the parameter r in pixels. We use 1 pixel.
theta   The resolution of the parameter θ in radians. We use 1 degree (CV_PI/180)
threshold   The minimum number of intersections to "*detect*" a line
srn   For the multi-scale Hough transform, it is a divisor for the distance resolution rho   The coarse accumulator distance resolution is rho and the accurate accumulator resolution is rho/srn. If both srn=0 and stn=0 , the classical Hough transform is used. Otherwise, both these parameters should be positive.
stn: For the multi-scale Hough transform, it is a divisor for the distance resolution theta.
min_theta   For standard and multi-scale Hough transform, minimum angle to check for lines. Must fall between 0 and max_theta.
max_theta   For standard and multi-scale Hough transform, maximum angle to check for lines. Must fall between min_theta and CV_PI.
```

* Hough Line Probability

minLineLenght를 활용하여 짧은 라인은 무시합니다. 또한 한 Line에 여러 개의 Pixel이 있더라도, Pixel 하나가 다른 pixel들과 너무 멀리 떨어져 있다면 그 pixel은 무시됩니다.   
그냥 Hough Line을 쓰는 것보다 정확성과 성능이 좋고, Customizing하기 수월합니다.

```cpp
//cpp
cv::HoughLinesP(image,lines,rho,theta,threshold,minLineLength,maxLineGap)
```
```python
#python
cv.HoughLinesP(image, rho, theta, threshold[,lines[,minLineLength[,maxLineGap]]]) -> lines
```
```
# Parameters
image	8-bit, single-channel binary source image. The image may be modified by the function.
lines	Output vector of lines. Each line is represented by a 4-element vector (x1,y1,x2,y2) , where (x1,y1) and (x2,y2) are the ending points of each detected line segment.
rho	Distance resolution of the accumulator in pixels.
theta	Angle resolution of the accumulator in radians.
threshold	Accumulator threshold parameter. Only those lines are returned that get enough votes ( >threshold ).
minLineLength	Minimum line length. Line segments shorter than that are rejected.
maxLineGap	Maximum allowed gap between points on the same line to link them.
```

![image](https://docs.opencv.org/3.4/building.jpg)   
![Probablistic](https://docs.opencv.org/3.4/houghp.png)   

