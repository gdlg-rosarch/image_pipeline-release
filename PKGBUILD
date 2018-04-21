# Script generated with Bloom
pkgdesc="ROS - Stereo and single image rectification and disparity processing."
url='http://www.ros.org/wiki/stereo_image_proc'

pkgname='ros-lunar-stereo-image-proc'
pkgver='1.12.21_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-cv-bridge'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-image-geometry'
'ros-lunar-image-proc'
'ros-lunar-image-transport'
'ros-lunar-message-filters'
'ros-lunar-nodelet'
'ros-lunar-rostest'
'ros-lunar-sensor-msgs'
'ros-lunar-stereo-msgs'
)

depends=('ros-lunar-cv-bridge'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-image-geometry'
'ros-lunar-image-proc'
'ros-lunar-image-transport'
'ros-lunar-message-filters'
'ros-lunar-nodelet'
'ros-lunar-sensor-msgs'
'ros-lunar-stereo-msgs'
)

conflicts=()
replaces=()

_dir=stereo_image_proc
source=()
md5sums=()

prepare() {
    cp -R $startdir/stereo_image_proc $srcdir/stereo_image_proc
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

