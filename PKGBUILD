# Script generated with Bloom
pkgdesc="ROS - A simple viewer for ROS image topics. Includes a specialized viewer for stereo + disparity images."
url='http://www.ros.org/wiki/image_view'

pkgname='ros-kinetic-image-view'
pkgver='1.12.22_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('gtk2'
'ros-kinetic-camera-calibration-parsers'
'ros-kinetic-catkin'
'ros-kinetic-cv-bridge>=1.11.13'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-image-transport'
'ros-kinetic-message-filters'
'ros-kinetic-message-generation'
'ros-kinetic-nodelet'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-rostest'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-stereo-msgs'
)

depends=('gtk2'
'ros-kinetic-camera-calibration-parsers'
'ros-kinetic-cv-bridge>=1.11.13'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-image-transport'
'ros-kinetic-message-filters'
'ros-kinetic-nodelet'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-std-srvs'
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
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
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

