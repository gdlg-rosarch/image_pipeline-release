# Script generated with Bloom
pkgdesc="ROS - A simple viewer for ROS image topics. Includes a specialized viewer for stereo + disparity images."
url='http://www.ros.org/wiki/image_view'

pkgname='ros-lunar-image-view'
pkgver='1.12.21_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('gtk2'
'ros-lunar-camera-calibration-parsers'
'ros-lunar-catkin'
'ros-lunar-cv-bridge>=1.11.13'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-image-transport'
'ros-lunar-message-filters'
'ros-lunar-message-generation'
'ros-lunar-nodelet'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rostest'
'ros-lunar-sensor-msgs'
'ros-lunar-std-srvs'
'ros-lunar-stereo-msgs'
)

depends=('gtk2'
'ros-lunar-camera-calibration-parsers'
'ros-lunar-cv-bridge>=1.11.13'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-image-transport'
'ros-lunar-message-filters'
'ros-lunar-nodelet'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-std-srvs'
)

conflicts=()
replaces=()

_dir=image_view
source=()
md5sums=()

prepare() {
    cp -R $startdir/image_view $srcdir/image_view
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

