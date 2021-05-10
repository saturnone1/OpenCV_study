# Histogram Comparison
```cpp
//cpp
cv::compareHist(H1,H2,method)
```
```python
# python
cv.compareHist(H1, H2, method) -> retval
```
```
# Parameters
H1	First compared histogram.
H2	Second compared histogram of the same size as H1 .
method	Comparison method, see HistCompMethods
```

Historgram을 비교하기 위한 방법이다. 이는 영상 처리의 궁극적인 목적이라 할 수 있는 objectDetection을 하기 위한 초기 단계의 방법이라고 이해하면 된다. 이미지의 Channel별로 Histogram을 분석하면 화면 내에서 가장 많이 보이는 물체의 색분포를 알 수 있다.   

![method](https://github.com/saturnone1/OpenCV_study/blob/5e9cd9823bae2752f74a0b8cdb53eacdcd72d888/ImageProcessing/image/comparison.png)   
위는 Method 파라미터 네 가지 방법을 소개한다.    

# Example

![0](https://docs.opencv.org/3.4/Histogram_Comparison_Source_0.jpg)
![1](https://docs.opencv.org/3.4/Histogram_Comparison_Source_1.jpg)
![2](https://docs.opencv.org/3.4/Histogram_Comparison_Source_2.jpg)   
**Image Base/ Test1/ Test2**   

실습에서는 각기 다른 빛의 세기로 찍은 이미지에 대해 진행하였지만 중요치 않을 수 있다고 생각했다. 이 실험 내에서는 이미지를 HSV파일로 변환한 후에 H-S에 대해서만 진행하도록 Channel을 CalcHist에서 제한하기 때문이다. 그러나 결과를 보고 생각이 달라졌다.   

|Method|Base|Base-Half|Test1|Test2|
|-------------|----------|----------|---------|--------|
|*Correlation*|1.000000	0.880438|0.20457|0.0664547|0.0664547|
|*Chi-square*|0.000000|4.6834|2697.98|4763.8|
|*Intersection*|18.8947|13.022|5.44085|2.58173|
|*Bhattacharyya*|0.000000|0.237887|0.679826|0.874173|

위의 결과에 따르면 명도가 낮은 Test2가 BASE와 가장 상이하다는 결과가 나온다. 이는 어두운 곳에서 색의 명도 뿐 아니라 채도가 달라질 수 있기 때문을 의미하는 듯 하다.
