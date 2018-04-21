# Script generated with Bloom
pkgdesc="ROS - Contains nodelets for processing depth images such as those produced by OpenNI camera. Functions include creating disparity images and point clouds, as well as registering (reprojecting) a depth image into another camera frame."
url='http://ros.org/wiki/depth_image_proc'

pkgname='ros-kinetic-depth-image-proc'
pkgver='1.12.22_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-cv-bridge'
'ros-kinetic-eigen-conversions'
'ros-kinetic-image-geometry'
'ros-kinetic-image-transport'
'ros-kinetic-message-filters'
'ros-kinetic-nodelet'
'ros-kinetic-rostest'
'ros-kinetic-sensor-msgs'
'ros-kinetic-stereo-msgs'
'ros-kinetic-tf2'
'ros-kinetic-tf2-ros'
)

depends=('boost'
'ros-kinetic-cv-bridge'
'ros-kinetic-eigen-conversions'
'ros-kinetic-image-geometry'
'ros-kinetic-image-transport'
'ros-kinetic-nodelet'
'ros-kinetic-tf2'
'ros-kinetic-tf2-ros'
)

conflicts=()
replaces=()

_dir=depth_image_proc
source=()
md5sums=()

prepare() {
    cp -R $startdir/depth_image_proc $srcdir/depth_image_proc
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

