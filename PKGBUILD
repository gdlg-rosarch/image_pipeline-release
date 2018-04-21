# Script generated with Bloom
pkgdesc="ROS - Stereo and single image rectification and disparity processing."
url='http://www.ros.org/wiki/stereo_image_proc'

pkgname='ros-kinetic-stereo-image-proc'
pkgver='1.12.22_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cv-bridge'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-image-geometry'
'ros-kinetic-image-proc'
'ros-kinetic-image-transport'
'ros-kinetic-message-filters'
'ros-kinetic-nodelet'
'ros-kinetic-rostest'
'ros-kinetic-sensor-msgs'
'ros-kinetic-stereo-msgs'
)

depends=('ros-kinetic-cv-bridge'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-image-geometry'
'ros-kinetic-image-proc'
'ros-kinetic-image-transport'
'ros-kinetic-message-filters'
'ros-kinetic-nodelet'
'ros-kinetic-sensor-msgs'
'ros-kinetic-stereo-msgs'
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

