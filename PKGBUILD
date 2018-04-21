# Script generated with Bloom
pkgdesc="ROS - Contains nodelets for processing depth images such as those produced by OpenNI camera. Functions include creating disparity images and point clouds, as well as registering (reprojecting) a depth image into another camera frame."
url='http://ros.org/wiki/depth_image_proc'

pkgname='ros-lunar-depth-image-proc'
pkgver='1.12.21_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'ros-lunar-catkin'
'ros-lunar-cmake-modules'
'ros-lunar-cv-bridge'
'ros-lunar-eigen-conversions'
'ros-lunar-image-geometry'
'ros-lunar-image-transport'
'ros-lunar-message-filters'
'ros-lunar-nodelet'
'ros-lunar-rostest'
'ros-lunar-sensor-msgs'
'ros-lunar-stereo-msgs'
'ros-lunar-tf2'
'ros-lunar-tf2-ros'
)

depends=('boost'
'ros-lunar-cv-bridge'
'ros-lunar-eigen-conversions'
'ros-lunar-image-geometry'
'ros-lunar-image-transport'
'ros-lunar-nodelet'
'ros-lunar-tf2'
'ros-lunar-tf2-ros'
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

