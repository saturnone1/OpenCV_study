# Making your own linear filters!

## Correlation
correlation은 Image와 Operator(Kernel)간의 모든 부분에 대한 동작을 이야기한다.   

## What is Kernel?
Anchor Point를 포함하여 둘러싼 Coefficient 수치를 가진 고정된 크기의 Array를 이야기한다. Anchor Point는 일반적으로 Center에 해당한다.   

![Kernel](https://docs.opencv.org/3.4/filter_2d_tutorial_kernel_theory.png)    

## What does correlation with a kernel work?

Correlation은 다음 순서를 통해 이루어진다.

1. 구하고자 하는 Pixel 위치를 Kernel의 Anchor point로 잡는다. Kernel 영역에 해당하는 다른 모든 Pixel들은 Image안에 위치하여야 한다.
2. Kernel Coefficient들을 각 Pixel Value와 곱하고 모두 더한다.
3. 결과를 Input Image의 *anchor*위치에 넣는다

## If You want to Normalize it.

Correlation의 평균값을 **2번**의 *Result*에 나누어 주면 된다.


