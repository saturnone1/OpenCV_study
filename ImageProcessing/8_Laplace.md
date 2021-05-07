# Laplace Operator

```cpp
cv:Laplacian(src, dst, ddepth, ksize, scale, delta, borderType)
```
```python
cv.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst
```
```
# Parameters
src	Source image.
dst	Destination image of the same size and the same number of channels as src .
ddepth	Desired depth of the destination image.
ksize	Aperture size used to compute the second-derivative filters. See getDerivKernels for details. The size must be positive and odd.
scale	Optional scale factor for the computed Laplacian values. By default, no scaling is applied. See getDerivKernels for details.
delta	Optional delta value that is added to the results prior to storing them in dst .
borderType	Pixel extrapolation method, see BorderTypes. BORDER_WRAP is not supported.
```

* ksize == 1, Kernel: 
| 0  1  0 |
| 1 -4  1 |
| 0  1  0 |

# Theory

1. Sobel의 원리를 파헤치면서 1st Derivative가 최대점인 부분을 찾았다.   
![sobel](https://docs.opencv.org/3.4/Laplace_Operator_Tutorial_Theory_Previous.jpg)   
2. 만약 2nd Derivative라면?   
![2nd](https://docs.opencv.org/3.4/Laplace_Operator_Tutorial_Theory_ddIntensity.jpg)   
2nd Derivative는 **0**인 지점이다. 그러나 수학적인 문제가 생긴다. 2nd Derivative가 아니더라도 0인 지점이 있을 수 있는 것이다. 이 지점에 대해서는 따로 Filtering 작업을 해준다.   

## Laplacian Operator
자주 본 이계도 방정식이다.   넘기도록 하자.


# Result

![cow](https://docs.opencv.org/3.4/Laplace_Operator_Tutorial_Original_Image.jpg)   
**Input Image**

![result](https://docs.opencv.org/3.4/Laplace_Operator_Tutorial_Result.jpg)   
**Result: Better than 1st Derivate**

* 나무 뒤의 집은 어색할 정도로 강렬하게 표시되는데, 이는 집쪽의 대비가 더 심하기 때문이다.
* 2nd Derivative까지 갔기 때문에 Sobel보다 훨신 좋은 성능을 보인다
