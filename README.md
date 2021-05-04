# OpenCV_study

* OpenCV
[OpenCV_docs](https://docs.opencv.org/3.4/index.html)


OpenCV API 설명

1. cv Namespace 사용 가능

```cpp
#include "opencv2/core.hpp"
...
cv::Mat H = cv::findHomography(points1, points2, cv::RANSAC, 5);
...

```
