# OpenCV_study (3.4 ver)

원본:: [OpenCV](https://docs.opencv.org/3.4/index.html)

## ARM 기반(Jetson) Linux 시스템에서의 크로스 컴파일

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
  위의 패키지들은 Ubuntu Linux 시스템의 universe repository에 있을 수 있습니다. 만약 Repository를 Enable하지 않으셨다면,
  다음과 같은 과정을 수행하면 됩니다.
  
  ```bash
  $ sudo apt-add-repository universe
  $ sudo apt-get update
  ```
  이제 Package를 설치합니다.
  
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
  
  * Build Area 생성
  ```bash
  #in opencv folder
  $ mkdir build
  $ cd build
  ```
  
  * 빌드를 위한 OpenCV 설정 CMAKE   
  
  **CMAKE_INSTALL_PREFIX는 /usr에서 원하는 어떤 폴더로도 가능합니다. 대신 위치를 기억하고 PATH 설정에 주의해야 합니다**   
  **각 파라미터의 의미는 꼭 숙지하시고 사용 여부와 버전을 맞추어야 합니다**   
  
  ```bash
  $ cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr/local \
    -DBUILD_PNG=OFF \
    -DBUILD_TIFF=OFF \
    -DBUILD_TBB=OFF \
    -DBUILD_JPEG=OFF \
    -DBUILD_JASPER=OFF \
    -DBUILD_ZLIB=OFF \
    -DBUILD_EXAMPLES=ON \
    -DBUILD_JAVA=OFF \
    -DBUILD_opencv_python2=ON \
    -DBUILD_opencv_python3=OFF \
    -DENABLE_PRECOMPILED_HEADERS=OFF \
    -DWITH_OPENCL=OFF \
    -DWITH_OPENMP=OFF \
    -DWITH_FFMPEG=ON \
    -DWITH_GSTREAMER=OFF \
    -DWITH_GSTREAMER_0_10=OFF \
    -DWITH_CUDA=ON \
    -DWITH_GTK=ON \
    -DWITH_VTK=OFF \
    -DWITH_TBB=ON \
    -DWITH_1394=OFF \
    -DWITH_OPENEXR=OFF \
    -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-10.2 \
    -DCUDA_ARCH_BIN=7.2 \
    -DCUDA_ARCH_PTX="" \
    -DINSTALL_C_EXAMPLES=ON \
    -DINSTALL_TESTS=OFF \
    -DOPENCV_TEST_DATA_PATH=../opencv_extra/testdata \
    ../opencv
  ```
  
  ```bash
  #OpenCV의 3.0 버전 이상에서 최대의 기능을 활용하기 위해서는 다음의 파라미터가 필수입니다.
  -DOPENCV_EXTRA_MODULES_PATH=<path-to-opencv_contrib>/modules
  ```
  
  * OpenCV 빌드   
  **-j% 의 숫자 부분은 빌드하는 Tegra 코어의 프로세서 수를 넘지 말아야 합니다. 빌드 멀티프로세싱을 몇 코어로 진행하느냐를 결정합니다**   
  ```bash
  $ sudo make -j6
  $ sudo make install
  ```
  
  * 빌드 파라미터에 대한 참고   
  **Python Binding을 하고자 한다면 이 사이트를 참조하십시오**   
  
  OpenCV Cmake Parameter:: [CMake_Parameter_Reference](https://docs.opencv.org/master/db/d05/tutorial_config_reference.html)
  
