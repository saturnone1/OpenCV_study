# Image Segmentation with Distance Transform and Watershed Algorithm
출저: [OpenCV_ImageSegmentaion](https://docs.opencv.org/3.4/d2/dbd/tutorial_distance_transform.html)   

코드와 추가적인 설명은 위의 자료를 바탕으로 구성되어 있습니다.   

## Delete Background with InRange masking
![before](https://docs.opencv.org/3.4/source.jpeg)
![after](https://docs.opencv.org/3.4/black_bg.jpeg)   

```cpp
    // 나중에 추출을 편하게 하기 위해, 배경을 흰색에서 검은색으로 변경
    // Distance Transform에서 더 나은 결과를 보여준다.
    Mat mask;
    inRange(src, Scalar(255, 255, 255), Scalar(255, 255, 255), mask);
    src.setTo(Scalar(0, 0, 0), mask);

    // 출력
    imshow("Black Background Image", src);
```
## Edge Detection with Apply Laplacian filter
10_Laplace에서 Laplacian Edge Detection을 배웠었다. 이 것을 활용하여 이미지에 가장자리 구분선을 만들어 줄 것이다.   
![laplace](https://docs.opencv.org/3.4/laplace.jpeg)
![filter](https://docs.opencv.org/3.4/sharp.jpeg)   

```cpp
    // Edge Detection을 하기 위한 Kerenel을 만든다
    Mat kernel = (Mat_<float>(3,3) <<
                  1,  1, 1,
                  1, -8, 1,
                  1,  1, 1); // an approximation of second derivative, a quite strong kernel
    // do the laplacian filtering as it is
    // well, we need to convert everything in something more deeper then CV_8U
    // because the kernel has some negative values,
    // and we can expect in general to have a Laplacian image with negative values
    // BUT a 8bits unsigned int (the one we are working with) can contain values from 0 to 255
    // so the possible negative number will be truncated
    Mat imgLaplacian;
    filter2D(src, imgLaplacian, CV_32F, kernel);
    Mat sharp;
    src.convertTo(sharp, CV_32F);
    Mat imgResult = sharp - imgLaplacian; //원래 색을 없애주면 검정색 구분선이 생긴다.

    // convert back to 8bits gray scale
    imgResult.convertTo(imgResult, CV_8UC3);
    imgLaplacian.convertTo(imgLaplacian, CV_8UC3);

    // imshow( "Laplace Filtered Image", imgLaplacian );
    imshow( "New Sharped Image", imgResult );
```

## Distacne Transform

![card](https://docs.opencv.org/3.4/bin.jpeg)
![tran](https://docs.opencv.org/3.4/dist_transf.jpeg)   
GrayScale된 소스 이미지의 각 픽셀에 대해 가장 가까운 0픽셀 까지의 거리를 계산합니다.   
이미지 픽셀값이 0인 경우의 Distance Transform 값은 분명히 0입니다

```cpp
//cpp
cv::distanceTransform(src,dst,labels,distanceType,maskSize,labelType)
```
```python
# python
cv.distanceTransform (src, distanceType, maskSize [,dst [,dstType]])-> dst
cv.distanceTransformWithLabels (src, distanceType, maskSize [, dst [, labels [, labelType]]]) -> dst, label
```
```
# Parameter

src	8-bit, single-channel (binary) source image.
dst	Output image with calculated distances. It is a 8-bit or 32-bit floating-point, single-channel image of the same size as src.
labels	Output 2D array of labels (the discrete Voronoi diagram). It has the type CV_32SC1 and the same size as src.
distanceType	Type of distance, see DistanceTypes
maskSize	Size of the distance transform mask, see DistanceTransformMasks. DIST_MASK_PRECISE is not supported by this variant. In case of the DIST_L1 or DIST_C distance type, the parameter is forced to 3 because a 3×3 mask gives the same result as 5×5 or any larger aperture.
labelType	Type of the label array to build, see DistanceTransformLabelTypes.
```

* labels 및 labelType은 거의 사용하지 않습니다.   
* distanceType의 종류는 다음과 같습니다.   
    |Type| Explan |
    |------------|---------------|
    |DIST_USER|User defined distance|   
    |DIST_L1|distance = &#124;x1-x2&#124; + &#124;y1-y2&#124;|   
    |DIST_L2|the simple euclidean distance|   
    |DIST_C|distance = max\(&#124;x1-x2&#124;,&#124;y1-y2&#124;\)|   
    |DIST_L12|L1-L2 metric: distance = 2\(sqrt\(1+x*x/2\) - 1\)\)|   
    |DIST_FAIR|distance = c^2\(\|x\|/c-log\(1+\|x\|/c\)\), c = 1.3998|   
    |DIST_WELSCH|distance = c^2/2(1-exp(-(x/c)^2)), c = 2.9846|   
    |DIST_HUBER|distance = \|x\|\<c \? x^2/2 : c\(\|x\|-c/2\), c=1.345|   

* masksize의 종류는 다음과 같습니다   
    |Type|Explan|
    |---|---|
    |DIST_MASK_3|mask=3|
    |DIST_MASK_5|mask=5|
    |DIST_MASK_PRECISE|

## Dilate로 각 카드의 최상위 부분을 수집
앞에서 했던 부분이기 때문에 넘어가겠다.    

![dilate](https://docs.opencv.org/3.4/peaks.jpeg)   

```cpp
    // Threshold to obtain the peaks
    // This will be the markers for the foreground objects
    threshold(dist, dist, 0.4, 1.0, THRESH_BINARY);

    // Dilate a bit the dist image
    Mat kernel1 = Mat::ones(3, 3, CV_8U);
    dilate(dist, dist, kernel1);
    imshow("Peaks", dist);
```

## findContours를 이용하여 

