# Histogram Calculation

다음과 같은 image가 있다고 가정합니다   
![image](https://docs.opencv.org/3.4/Histogram_Calculation_Theory_Hist0.jpg)   
이를 histogram으로 표현하기 위해서 히스토그램 분류 그래프의 개수를 정해주어야 합니다. 이를 **bin**이라 부릅니다.   

**[0,255]=[0,15]∪[16,31]∪....∪[240,255]**   
**range=bin1∪bin2∪....∪binn=15**   

위와 같이 분류를 했을 때, 그려낸 히스토그램은 다음과 같습니다.   
![his](https://docs.opencv.org/3.4/Histogram_Calculation_Theory_Hist1.jpg)   

용어의 의미를 알아봅니다.   
1. dims: Data의 Parameter 수 입니다. 위의 사진과 예시에서는 Pixel Value(Intensity)만을 Data로 쓰기 때문에 **dims=1** 입니다.   
2. bins: 분류할 영역의 수 입니다. 위의 예시에서는 16개의 bin 즉 **bins=16**입니다.   
3. range: 측정할 값의 범위를 정해놓습니다. **range=[0,255]**   

## Split

Multi-channel array(RGB)를 Single-channel(R/G/B)로 바꾸어 준다.   

```cpp
//cpp
cv::split(src,mvbegin)
```
```python
#python
cv.split(m[,mv])->mv
```

## CalcHist
**!주의!**   
각 파라미터의 사용에 관해 자세히 읽어보고 사용해서 기대한 결과를 낼 수 있습니다.

```cpp
//cpp
cv::calcHist(images, nimages, channels, mask, hist, dims, histSize,ranges, uniform = true, accumulate = false)
```
```python
#python
cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) -> hist
```

```
# Parameters
images	Source arrays. They all should have the same depth, CV_8U, CV_16U or CV_32F , and the same size. Each of them can have an arbitrary number of channels.
nimages	Number of source images.
channels	List of the dims channels used to compute the histogram. The first array channels are numerated from 0 to images[0].channels()-1 , the second array channels are counted from images[0].channels() to images[0].channels() + images[1].channels()-1, and so on.
mask	Optional mask. If the matrix is not empty, it must be an 8-bit array of the same size as images[i] . The non-zero mask elements mark the array elements counted in the histogram.
hist	Output histogram, which is a dense or sparse dims -dimensional array.
dims	Histogram dimensionality that must be positive and not greater than CV_MAX_DIMS (equal to 32 in the current OpenCV version).
histSize	Array of histogram sizes in each dimension.
ranges	Array of the dims arrays of the histogram bin boundaries in each dimension. When the histogram is uniform ( uniform =true), then for each dimension i it is enough to specify the lower (inclusive) boundary L0 of the 0-th histogram bin and the upper (exclusive) boundary UhistSize[i]−1 for the last histogram bin histSize[i]-1 . That is, in case of a uniform histogram each of ranges[i] is an array of 2 elements. When the histogram is not uniform ( uniform=false ), then each of ranges[i] contains histSize[i]+1 elements: L0,U0=L1,U1=L2,...,UhistSize[i]−2=LhistSize[i]−1,UhistSize[i]−1 . The array elements, that are not between L0 and UhistSize[i]−1 , are not counted in the histogram.
uniform	Flag indicating whether the histogram is uniform or not (see above).
accumulate	Accumulation flag. If it is set, the histogram is not cleared in the beginning when it is allocated. This feature enables you to compute a single histogram from several sets of arrays, or to update the histogram in time.
```

## Normalize

[0,255]범위로 다시 넣기위한 Normalize 작업이 필요하다    

```cpp
//cpp
cv::normalize(b_hist, b_hist, 0, histImage.rows, NORM_MINMAX, -1, Mat() );
```
```python
# python
cv.normalize(src, dst[, alpha[, beta[, norm_type[, dtype[, mask]]]]]) -> dst
```
```
# Parameter
b_hist: Input array
b_hist: Output normalized array (can be the same)
0 and histImage.rows: For this example, they are the lower and upper limits to normalize the values of r_hist
NORM_MINMAX: Argument that indicates the type of normalization (as described above, it adjusts the values between the two limits set before)
-1: Implies that the output normalized array will be the same type as the input
Mat(): Optional mask
```

![image](https://docs.opencv.org/3.4/Histogram_Calculation_Original_Image.jpg)   
![hist](https://docs.opencv.org/3.4/Histogram_Calculation_Result.jpg)   
