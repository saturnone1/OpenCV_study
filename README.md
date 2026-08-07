# OpenCV_study (3.4)

Study notes on OpenCV 3.4, written while working through the official documentation.
Source: [OpenCV 3.4 docs](https://docs.opencv.org/3.4/index.html).

> **Archived.** These notes target OpenCV 3.4 and a Jetson/CUDA 10.2 era toolchain. Much
> of the build guidance below no longer applies to OpenCV 4.x. Kept for reference.

## Contents

| Directory | Topics |
|---|---|
| `ImageProcessing/` | Smoothing, morphology, sampling, thresholding, custom kernels, Sobel, Laplace, Canny, Hough line/circle, remapping, affine transforms, histogram equalisation/calculation/comparison, back projection, template matching, contours, image segmentation (21 notes) |
| `2DFeaturesFramework/` | Harris corner detector, Shi-Tomasi corners, writing a custom corner detector, feature detection, description and matching — plus runnable Python test code under `testcode/` |
| `ObjectClassify/` | Object classification notes |

## API notes

The `cv` namespace is available directly:

```cpp
#include "opencv2/core.hpp"
...
cv::Mat H = cv::findHomography(points1, points2, cv::RANSAC, 5);
```

See the [OpenCV transition guide](https://docs.opencv.org/3.4/db/dfa/tutorial_transition_guide.html)
for moving code between major versions.

---

# Build notes

## Cross-compiling for ARM Linux (Jetson)

Requirements:

- Linux
- CMake 2.6+
- A cross-compilation toolchain

```bash
sudo apt-get install gcc-arm-linux-gnueabi
sudo apt-get install gcc-arm-linux-gnueabihf
```

- Python 2.6+
- pkgconfig

Optional, for armeabi(hf): ffmpeg or libav development packages (`libavcodec-dev`,
`libavformat-dev`, `libswscale-dev`); GTK+ 2.x or newer including headers
(`libgtk2.0-dev`); libdc1394 2.x; `libjpeg-dev`, `libpng-dev`, `libtiff-dev`,
`libjasper-dev`.

Applying the toolchain at configure time:

```bash
cmake [other parameters] -DSOFTFP=ON \
  -DCMAKE_TOOLCHAIN_FILE=<opencv source dir>/platforms/linux/arm-gnueabi.toolchain.cmake \
  <opencv source dir>

# Example
cmake -DCMAKE_TOOLCHAIN_FILE=../arm-gnueabi.toolchain.cmake ../../..
```

## OpenCV with CUDA on Tegra (NVIDIA Jetson, 3.1+)

Get the sources — either a [release download](http://opencv.org/releases.html) or a clone:

```bash
git clone https://github.com/opencv/opencv.git
```

To build a specific version, check out its tag:

```bash
cd opencv
git checkout -b v3.1.0 3.1.0
```

### Requirements

```
CMake 2.8.10 or newer
CUDA toolkit 8.0 (7.0 or 7.5 also work)
Build tools (make, gcc, g++)
Python 2.6 or greater
```

Packages:

```
libglew-dev      libtiff5-dev     zlib1g-dev      libjpeg-dev
libpng12-dev     libjasper-dev    libavcodec-dev  libavformat-dev
libavutil-dev    libpostproc-dev  libswscale-dev  libeigen3-dev
libtbb-dev       libgtk2.0-dev    pkg-config
```

Some of these live in Ubuntu's *universe* repository. If it is not enabled:

```bash
sudo apt-add-repository universe
sudo apt-get update
```

Then install:

```bash
sudo apt-get install \
  libglew-dev libtiff5-dev zlib1g-dev libjpeg-dev libpng12-dev \
  libjasper-dev libavcodec-dev libavformat-dev libavutil-dev \
  libpostproc-dev libswscale-dev libeigen3-dev libtbb-dev \
  libgtk2.0-dev pkg-config
```

For Python bindings:

```bash
sudo apt-get install python-dev python-numpy python-py python-pytest
sudo apt-get install python3-dev python3-numpy python3-py python3-pytest   # Python 3
```

### Configure

```bash
mkdir build && cd build
```

`CMAKE_INSTALL_PREFIX` can be any directory under `/usr` — just remember where it went and
set `PATH` accordingly. Know what each parameter does before enabling it, and match the
versions to what is actually installed.

```bash
cmake \
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

To get the full feature set on OpenCV 3.0+, this parameter is required:

```bash
-DOPENCV_EXTRA_MODULES_PATH=<path-to-opencv_contrib>/modules
```

### Build

Keep `-j` at or below the Tegra's core count — it sets the build parallelism.

```bash
sudo make -j6
sudo make install
```

Parameter reference:
[CMake configuration reference](https://docs.opencv.org/master/db/d05/tutorial_config_reference.html).
