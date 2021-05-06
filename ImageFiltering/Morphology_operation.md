# Extract horizontal and vertical lines by using morphological operations
# Goal
* Erode, Dilate을 Binary가 아닌 GrayScale Image에 적용하는 방법   
* Horizontal, vertical Line을 추출하는 방법   

# Theory
앞에서 이야기 했기 때문에 추가적인 설명은 배제하고, 0과 1로만 이루어진 binary 이미지와 달리, GrayScale Image는 말 그대로 0~255사이의 값만을 가진 흑백 이미지입니다. 따라서 0과 1만으로는 판단하여 Dilation과 Erosion을 수행할 수 없고 Max, Min을 선택하여 처리하게됩니다.   

## Dilation
* Kernel 내 Max값을 가져다가 Anchor pixel 부분을 대체합니다.
