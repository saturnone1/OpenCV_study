# OpenCV_study (3.4 ver)

[OpenCV](https://docs.opencv.org/3.4/index.html)

## ARM 기반 Linux 시스템에서의 크로스 컴파일

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
 
## OpenCV with CUDA for Tegra Processor(3.1 over)(Nvidia Jetson)
  * **직접 소스코드 다운로드** [OpenCV downloads](http://opencv.org/releases.html)
  * Github 주소에서 Clone
  
  ```bash
  # Clone the opencv repository locally:
  $ git clone https://github.com/opencv/opencv.git
  ```
  
  3.1.0 version을 Clone하고자 한다면, 3.1.0 tag를 붙여 Checkout으로 버전 전환
  ```bash
  $ cd opencv
  $ git checkout -b v3.1.0 3.1.0
  ```
  
  * 요구 패키지 및 환경
  ```
  CMake 2.8.10 or newer
  CUDA toolkit 8.0 (7.0 or 7.5 may also be used)
  Build tools (make, gcc, g++)
  Python 2.6 or greater
  ```
  ```
  libglew-dev
  libtiff5-dev
  zlib1g-dev
  libjpeg-dev
  libpng12-dev
  libjasper-dev
  libavcodec-dev
  libavformat-dev
  libavutil-dev
  libpostproc-dev
  libswscale-dev
  libeigen3-dev
  libtbb-dev
  libgtk2.0-dev
  pkg-config
  ```
  위의 패키지들은 Ubuntu Linux 시스템의 universe repository에 있을 수 있다. 만약 Repository를 Enable하지 않으셨다면,
  다음과 같은 과정을 수행하면 됩니다.
  
  ```bash
  $ sudo apt-add-repository universe
  $ sudo apt-get update
  ```
  이제 Package
  
  ```bash
  $ sudo apt-get install \
    libglew-dev \
    libtiff5-dev \
    zlib1g-dev \
    libjpeg-dev \
    libpng12-dev \
    libjasper-dev \
    libavcodec-dev \
    libavformat-dev \
    libavutil-dev \
    libpostproc-dev \
    libswscale-dev \
    libeigen3-dev \
    libtbb-dev \
    libgtk2.0-dev \
    pkg-config
  ```
  
  Python Binding을 빌드 옵션에 넣는다면 다음을 설치하여야 합니다.
  
  ```bash 
  $ sudo apt-get install python-dev python-numpy python-py python-pytest 
  $ sudo apt-get install python3-dev python3-numpy python3-py python3-pytest #Python3
  ```
  
  
