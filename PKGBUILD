# Script generated with Bloom
pkgdesc="ROS - Single image rectification and color processing."
url='http://www.ros.org/wiki/image_proc'

pkgname='ros-lunar-image-proc'
pkgver='1.12.21_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'ros-lunar-camera-calibration-parsers'
'ros-lunar-catkin>=0.5.68'
'ros-lunar-cv-bridge'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-image-geometry'
'ros-lunar-image-transport'
'ros-lunar-nodelet'
'ros-lunar-nodelet-topic-tools'
'ros-lunar-roscpp'
'ros-lunar-rostest'
'ros-lunar-sensor-msgs'
)

depends=('ros-lunar-cv-bridge'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-image-geometry'
'ros-lunar-image-transport'
'ros-lunar-nodelet'
'ros-lunar-nodelet-topic-tools'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
)

conflicts=()
replaces=()

_dir=image_proc
source=()
md5sums=()

prepare() {
    cp -R $startdir/image_proc $srcdir/image_proc
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

