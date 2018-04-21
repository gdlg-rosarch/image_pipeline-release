# Script generated with Bloom
pkgdesc="ROS - image_pipeline fills the gap between getting raw images from a camera driver and higher-level vision processing."
url='http://www.ros.org/wiki/image_pipeline'

pkgname='ros-lunar-image-pipeline'
pkgver='1.12.21_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-camera-calibration'
'ros-lunar-depth-image-proc'
'ros-lunar-image-proc'
'ros-lunar-image-publisher'
'ros-lunar-image-rotate'
'ros-lunar-image-view'
'ros-lunar-stereo-image-proc'
)

conflicts=()
replaces=()

_dir=image_pipeline
source=()
md5sums=()

prepare() {
    cp -R $startdir/image_pipeline $srcdir/image_pipeline
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

