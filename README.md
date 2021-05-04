# OpenCV_study (3.4 ver)

[OpenCV](https://docs.opencv.org/3.4/index.html)

# ARM 기반 Linux 시스템에서의 크로스 컴파일

* 요구 환경

  Linux   
  CMake 2.6 이상   
  Cros Compile Tool   
  ```bash
  $ sudo apt-get install gcc-arm-linux-gnueabi
  $ sudo apt-get install gcc-arm-linux-gnueabihf
  ```
  Python 2.6 이상   
  pkgconfig 설치   

  [optional] ffmpeg or libav development packages for armeabi(hf): libavcodec-dev, libavformat-dev, libswscale-dev;   
  [optional] GTK+2.x or higher, including headers (libgtk2.0-dev) for armeabi(hf);   
  [optional] libdc1394 2.x;   
  [optional] libjpeg-dev, libpng-dev, libtiff-dev, libjasper-dev for armeabi(hf)   

* 빌드 시 Cross Compile 적용 방법

  ```bash
  cmake [기타 파라미터] -DSOFTFP=ON -DCMAKE_TOOLCHAIN_FILE=<OpenCV 소스 디렉터리 PATH>/platforms/linux/arm-gnueabi.toolchain.cmake    <OpenCV 소스 디렉터리 PATH>

  Example: cmake -DCMAKE_TOOLCHAIN_FILE=../arm-gnueabi.toolchain.cmake ../../..
  ```
 
# OpenCV with CUDA (3.1 over)


